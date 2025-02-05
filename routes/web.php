<?php

use App\Http\Controllers\ReportController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});
Route::get('/report/pdf/{id}', [ReportController::class, 'show'])->name('report.pdf');