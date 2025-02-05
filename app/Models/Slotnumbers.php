<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Slotnumbers extends Model
{
    use HasFactory;

    protected $table = 'slotnumbers'; // Specify the table name

    protected $fillable = [
        'id',
        'slot_number',
        'status',
    ];

    /**
     * Scope to get only available slots.
     */
    public function scopeActive($query)
    {
        return $query->where('status', 'active');
    }
}
