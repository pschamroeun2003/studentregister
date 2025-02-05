<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Str;
use Carbon\Carbon;

class ParkingLog extends Model
{
    protected $fillable = ['vehicle_id', 'entry_time', 'exit_time', 'fee_paid', 'secret_key'];
    protected $table = 'parkinglogs';

    protected static function boot()
    {
        parent::boot();

        static::creating(function ($parkingLog) {
            if (empty($parkingLog->entry_time)) {
                $parkingLog->entry_time = Carbon::now();
            }
            if (empty($parkingLog->secret_key)) {
                $parkingLog->secret_key = Str::random(12);
            }
        });
    }

    public function vehicle(){
        return $this->belongsTo(Vehicle::class, 'vehicle_id', 'id');
    }
    public function slot()
{
    return $this->belongsTo(Slotnumbers::class, 'vehicle_id');
}

}