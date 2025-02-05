<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ParkingBarcode extends Model
{
    use HasFactory;
    protected $table = 'parking_barcodes';
    protected $fillable = [
        'barcode',
    ];
    public $timestamps = true;
}