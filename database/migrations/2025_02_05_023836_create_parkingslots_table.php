<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('parkingslots', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('slot_number_id')->nullable();
            $table->boolean('is_available')->default(true);
            $table->unsignedBigInteger('vehicle_id')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('parkingslots');
    }
};
