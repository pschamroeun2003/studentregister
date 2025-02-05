<?php

namespace App\Filament\Resources\ParkingLogResource\Pages;

use App\Filament\Resources\ParkingLogResource;
use Filament\Actions;
use Filament\Resources\Pages\ListRecords;

class ListParkingLogs extends ListRecords
{
    protected static string $resource = ParkingLogResource::class;

    protected function getHeaderActions(): array
    {
        return [
            Actions\CreateAction::make(),
        ];
    }
}
