<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Vehicle;
use Illuminate\Support\Facades\DB;

class VehicleSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        DB::table('vehicles')->insert([
            [
                'license_plate' => '2A-1234',
                'vehicle_type' => 'Car',
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'license_plate' => '1B-5678',
                'vehicle_type' => 'Motorbike',
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'license_plate' => '3C-9876',
                'vehicle_type' => 'Car',
                'created_at' => now(),
                'updated_at' => now(),
            ],
        ]);
    }
}
