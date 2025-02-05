<?php

namespace App\Filament\Resources\ParkingslotsResource\Pages;

use App\Filament\Resources\ParkingslotsResource;
use Filament\Actions;
use Filament\Resources\Pages\ListRecords;

class ListParkingslots extends ListRecords
{
    protected static string $resource = ParkingslotsResource::class;

    protected function getHeaderActions(): array
    {
        return [
            Actions\CreateAction::make(),
        ];
    }
}
