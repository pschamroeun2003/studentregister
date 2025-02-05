<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        // Creating a default admin user
        User::create([
            'name' => 'Admin User',
            'email' => 'admin@example.com',
            'password' => Hash::make('password123'), // Ensure to hash the password
        ]);
        User::create([
            'name' => 'Regular User',
            'email' => 'user@example.com',
            'password' => Hash::make('password123'),
        ]);
        User::create([
            'name' => 'AdminKhemasoft',
            'email' => 'admin@khemasoft.com',
            'password' => Hash::make('88889999'),
        ]);

        // Add more users if needed
    }
}
