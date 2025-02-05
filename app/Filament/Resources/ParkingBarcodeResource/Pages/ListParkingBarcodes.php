<?php

namespace App\Filament\Resources\ParkingBarcodeResource\Pages;

use App\Filament\Resources\ParkingBarcodeResource;
use Filament\Actions;
use Filament\Resources\Pages\ListRecords;

class ListParkingBarcodes extends ListRecords
{
    protected static string $resource = ParkingBarcodeResource::class;

    protected function getHeaderActions(): array
    {
        return [
            Actions\CreateAction::make(),
        ];
    }
}
