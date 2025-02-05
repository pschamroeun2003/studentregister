<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Parkingslots extends Model
{
    use HasFactory;

    protected $fillable = ['slot_number_id', 'is_available','slot_number' ,'vehicle_id'];

    public function parkingRecords()
    {
        return $this->hasMany(ParkingRecord::class);
    }

   public function vehicle()
    {
        return $this->belongsTo(Vehicle::class);
    }
    public function slot()
{
    return $this->belongsTo(Slotnumbers::class, 'slot_number_id', 'id');
}



}