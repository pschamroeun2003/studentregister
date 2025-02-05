<?php

namespace App\Filament\Resources;

use App\Filament\Resources\ParkingslotsResource\Pages;
use App\Filament\Resources\ParkingslotsResource\RelationManagers;
use App\Models\Parkingslots;
use App\Models\Slotnumbers;
use App\Models\Vehicle;
use Barryvdh\DomPDF\Facade\Pdf;
use Filament\Forms;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\Toggle;
use Filament\Forms\Form;
use Filament\Resources\Resource;
use Filament\Tables;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\SoftDeletingScope;

class ParkingslotsResource extends Resource
{
    protected static ?string $model = Parkingslots::class;

    protected static ?string $navigationIcon = 'heroicon-o-rectangle-stack';

   public static function form(Form $form): Form
{
        return $form
            ->schema([
                Forms\Components\Group::make([
                 Select::make('vehicle_id')
    ->label('Vehicle')
    ->options(function () {
        return Vehicle::whereNotIn('id', function ($query) {
            $query->select('vehicle_id')->from('parkingslots')->whereNotNull('vehicle_id');
        })->pluck('license_plate', 'id');
    })
    ->searchable()
    ->required()
    ->columnSpan(6),
                    Toggle::make('is_available')
                        ->label('Is Available')
                        ->required()
                        ->inline()
                        ->columnSpan(6),
                ])
                    ->columnSpan(12),

                Select::make('slot_number_id')
                    ->label('Parking Slot')
                    ->options(fn() => Slotnumbers::where('status', 'active')->pluck('slot_number', 'id'))
                    ->searchable()
                    ->required()
                    ->columnSpan(12)
                    ->afterStateUpdated(function ($state) {
        if($state){
            Slotnumbers::where('id', $state)->update(['status' => 'inactive']);

        }
    }),
        ]);
}


    public static function table(Table $table): Table
    {
        return $table
            ->columns([
                Tables\Columns\TextColumn::make('vehicle.license_plate')
                ->label('License Plate')
                ->searchable(),
                Tables\Columns\TextColumn::make('vehicle.vehicle_type')
                ->label('Vehicle Type')
                ->searchable(),
                  Tables\Columns\TextColumn::make('slot.slot_number')
                ->label('Slot Number')
                ->searchable(),
                Tables\Columns\IconColumn::make('is_available')
                    ->boolean(),
                Tables\Columns\TextColumn::make('created_at')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
                Tables\Columns\TextColumn::make('updated_at')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
            ])
            ->filters([
                //
            ])
            ->actions([
                Tables\Actions\EditAction::make(),
                  Tables\Actions\DeleteAction::make(),
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
            'index' => Pages\ListParkingslots::route('/'),
            'create' => Pages\CreateParkingslots::route('/create'),
          //  'edit' => Pages\EditParkingslots::route('/{record}/edit'),
        ];
    }
}
