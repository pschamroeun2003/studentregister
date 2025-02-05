<?php

namespace App\Filament\Resources\ParkingBarcodeResource\Pages;

use App\Filament\Resources\ParkingBarcodeResource;
use Filament\Actions;
use Filament\Resources\Pages\EditRecord;

class EditParkingBarcode extends EditRecord
{
    protected static string $resource = ParkingBarcodeResource::class;

    protected function getHeaderActions(): array
    {
        return [
            Actions\DeleteAction::make(),
        ];
    }
}
