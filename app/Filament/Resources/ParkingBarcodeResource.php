<?php

namespace App\Filament\Resources;

use App\Filament\Resources\ParkingBarcodeResource\Pages;
use App\Filament\Resources\ParkingBarcodeResource\RelationManagers;
use App\Models\ParkingBarcode;
use App\Models\ParkingLog;
use Carbon\Carbon;
use DesignTheBox\BarcodeField\Forms\Components\BarcodeInput;
use Filament\Forms;
use Filament\Forms\Form;
use Filament\Resources\Resource;
use Filament\Tables;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\SoftDeletingScope;

class ParkingBarcodeResource extends Resource
{
    protected static ?string $model = ParkingBarcode::class;

    protected static ?string $navigationIcon = 'heroicon-o-rectangle-stack';

   public static function form(Form $form): Form
{
    return $form
        ->schema([
            BarcodeInput::make('barcode')
                ->required()
                ->label('Barcode')
                ->unique('parkinglogs', 'secret_key')
                ->afterStateUpdated(function ($state, $set) {
                    $parkingLog = ParkingLog::where('secret_key', $state)->first();
                    if ($parkingLog) {
                        $parkingLog->update([
                            'exit_time' => Carbon::now(),
                            'status' => 'out',
                        ]);
                        $set('fee_paid', $parkingLog->fee_paid);
                    } else {
                        $set('barcode', null);
                        $set('fee_paid', null);
                    }
                }),
        ]);
}


    public static function table(Table $table): Table
    {
        return $table
            ->columns([
                TextColumn::make('barcode')
                    ->label('Barcode')
                    ->sortable()
                    ->searchable(),
            ])
            ->filters([
                //
            ])
            ->actions([
                Tables\Actions\EditAction::make(),
            ])
            ->bulkActions([
                Tables\Actions\BulkActionGroup::make([
                    Tables\Actions\DeleteBulkAction::make(),
                ]),
            ]);
    }

    public static function getRelations(): array
    {
        return [
            //
        ];
    }

    public static function getPages(): array
    {
        return [
            'index' => Pages\ListParkingBarcodes::route('/'),
            'create' => Pages\CreateParkingBarcode::route('/create'),
            'edit' => Pages\EditParkingBarcode::route('/{record}/edit'),
        ];
    }
}