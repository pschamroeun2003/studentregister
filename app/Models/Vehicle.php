<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Vehicle extends Model
{
    use HasFactory;

    protected $fillable = ['license_plate', 'vehicle_type'];

    public function parkingRecords()
    {
        return $this->hasMany(ParkingRecord::class);
    }

    public function parkingSlot()
    {
        return $this->hasOneThrough(Parkingslots::class, ParkingRecord::class, 'vehicle_id', 'id', 'id', 'parking_slot_id');
    }
}