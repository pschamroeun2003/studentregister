<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Parking Ticket</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            text-align: center;
            max-width: 300px;
            margin: 20px auto;
            border: 2px solid black;
            padding: 20px;
        }

        .logo {
            font-size: 50px;
        }

        .header {
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .line {
            border-top: 2px solid black;
            margin: 10px 0;
        }

        .title {
            font-size: 16px;
            font-weight: bold;
        }

        .time {
            font-size: 28px;
            font-weight: bold;
        }

        .details {
            font-size: 14px;
            margin-top: 5px;
        }

        .paid {
            font-size: 20px;
            font-weight: bold;
            margin-top: 10px;
        }

        .barcode {
            margin-top: 15px;
        }

        .barcode img {
            width: 100%;
            height: auto;
        }

        .footer {
            font-size: 12px;
            margin-top: 10px;
        }
    </style>
</head>

<body>

    <div class="logo">🚗</div>

    <div class="header">
        Beltei Parking <br>
        Toul Sleang, Street : 360 <br>
        888-888-8888
    </div>

    <div class="line"></div>

    <div class="title">PARKING RECEIPT</div>

    <!-- Replace dynamic content with Blade syntax in Laravel -->
    <div class="time">{{ $record['created_at']->format('m/d/Y h:i A') }}</div>

    <div class="details">
        {{ now()->format('m/d/Y') }} <br>
        Space: {{ $record->slot->slot_number }}
    </div>

    <div class="paid">Paid: {{ $record->fee_paid }}Riel</div>

    <div class="line"></div>

    <div class="footer">THANK YOU AND DRIVE SAFELY!</div>

    <div class="barcode">
        {!! DNS1D::getBarcodeHTML($record->secret_key, 'C128') !!}
    </div>


</body>

</html>
