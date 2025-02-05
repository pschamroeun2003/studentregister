<?php

namespace App\Filament\Resources;

use App\Filament\Resources\ParkingLogResource\Pages;
use App\Models\ParkingLog;
use App\Models\Parkingslots;
use App\Models\Vehicle;
use Barryvdh\DomPDF\Facade\Pdf;
use Carbon\Carbon;
use Filament\Forms;
use Filament\Forms\Form;
use Filament\Resources\Resource;
use Filament\Tables;
use Filament\Tables\Table;
use Filament\Tables\Columns\TextColumn;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\DateTimePicker;
use Illuminate\Database\Eloquent\Builder;
use Filament\Forms\Components\Grid;
class ParkingLogResource extends Resource
{
    protected static ?string $model = ParkingLog::class;

    protected static ?string $navigationIcon = 'heroicon-o-rectangle-stack';

public static function form(Form $form): Form
{
    return $form
        ->schema([
            Grid::make(3)
                ->schema([
                    Select::make('vehicle_id')
                        ->label('Vehicle')
                        ->options(Vehicle::pluck('license_plate', 'id'))
                        ->searchable()
                        ->reactive()
                        ->afterStateUpdated(function ($state, $set) {
                            $vehicle = Vehicle::find($state);
                            $fee = 0;
                            if ($vehicle) {
                                $fee = $vehicle->vehicle_type === 'Car' ? 2000 : ($vehicle->vehicle_type === 'Motorbike' ? 1000 : 0);
                            }
                            $set('fee_paid', $fee);
                        })
                        ->required(),
                    DateTimePicker::make('entry_time')
                        ->label('Entry Time')
                        ->default(Carbon::now())
                        ->required(),
                    DateTimePicker::make('exit_time')
                        ->label('Exit Time')
                        ->nullable(),
                    Forms\Components\TextInput::make('fee_paid')
                        ->label('Fee Paid (៛)')
                        ->numeric()
                        ->step(0.01)
                        ->nullable()
                        ->columnSpan(2)
                        ->formatStateUsing(function ($state) {
                            return number_format($state, 0, '.', ',') . ' ៛';
                        }),
                    Forms\Components\TextInput::make('secret_key')
                        ->label('Secret Key')
                        ->default(fn () => \Illuminate\Support\Str::random(10)) // Generate a random key
                        ->readOnly(),
                ]),
        ]);
}


    public static function table(Table $table): Table
    {
        return $table
            ->columns([
                TextColumn::make('vehicle.license_plate')
                    ->label('Vehicle')
                    ->sortable()
                    ->searchable(),

                TextColumn::make('entry_time')
                    ->label('Entry Time')
                    ->dateTime()
                    ->sortable(),

                TextColumn::make('exit_time')
                    ->label('Exit Time')
                    ->dateTime()
                    ->sortable()
                    ->placeholder('Still Parked'),

                TextColumn::make('fee_paid')
                    ->label('Fee Paid ($)')
                    ->numeric()
                    ->sortable()
                    ->default('-'),

                TextColumn::make('secret_key')
                    ->label('Secret Key')
                    ->copyable() // Allow copying the key
                    ->toggleable(),
            ])
            ->filters([
                //
            ])
            ->actions([
                Tables\Actions\EditAction::make(),
                Tables\Actions\DeleteAction::make(),
                   Tables\Actions\Action::make('print')
        ->label('Print')
        ->icon('heroicon-o-printer')
      ->action(fn ($record) => static::printRecord($record)),
            ])
            ->bulkActions([
                Tables\Actions\BulkActionGroup::make([
                    Tables\Actions\DeleteBulkAction::make(),
                ]),
            ]);
    }

    public static function printRecord($record)
{
    $record = ParkingLog::findOrFail($record->id);
        // dd($record->toArray());
    $pdf = Pdf::loadView('parkingticket', compact('record'));
    return response()->streamDownload(
        fn () => print($pdf->output()),
        'parking_ticket_report.pdf'
    );
}

    public static function getPages(): array
    {
        return [
            'index' => Pages\ListParkingLogs::route('/'),
            'create' => Pages\CreateParkingLog::route('/create'),
            'edit' => Pages\EditParkingLog::route('/{record}/edit'),
        ];
    }
}
