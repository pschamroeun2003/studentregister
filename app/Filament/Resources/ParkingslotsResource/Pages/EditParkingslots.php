<?php

namespace App\Filament\Resources\ParkingslotsResource\Pages;

use App\Filament\Resources\ParkingslotsResource;
use Filament\Actions;
use Filament\Resources\Pages\EditRecord;

class EditParkingslots extends EditRecord
{
    protected static string $resource = ParkingslotsResource::class;

    protected function getHeaderActions(): array
    {
        return [
            Actions\DeleteAction::make(),
        ];
    }
}
