<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class SlotNumbersSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        foreach (range(1, 50) as $index) {
        DB::table('slotnumbers')->insert([
            'slot_number' => 'A' . $index,
            'status' => 'active',
            'created_at' => now(),
            'updated_at' => now(),
        ]);
    }
    }
}