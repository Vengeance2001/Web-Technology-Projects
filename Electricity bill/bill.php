<!DOCTYPE html>
<html>
<head>
    <title>Electricity Bill Calculator</title>
    <link rel="stylesheet" href="bill.css">
</head>
<body>
    <div class="main">

        <div class="container">
            <h1>Electricity Bill </h1>
        <?php echo "Name: " . $_POST["name1"]?>
        <?php
        
        if (isset($_POST['units'])) {
            $units = intval($_POST['units']);
            if ($units <= 50) {
                $billAmount = $units * 3.50;
            } elseif ($units <= 150) {
                $billAmount = 50 * 3.50 + ($units - 50) * 4.00;
            } elseif ($units <= 250) {
                $billAmount = 50 * 3.50 + 100 * 4.00 + ($units - 150) * 5.20;
            } else {
                $billAmount = 50 * 3.50 + 100 * 4.00 + 100 * 5.20 + ($units - 250) * 6.50;
            }


            echo "<p>Your Electricity Bill: Rs. " . number_format($billAmount, 2) . "</p>";
            echo "<p>For first 50 Units -  Rs. 3.50/unit,</p>";
            echo "<p>For next 100 Units -  Rs. 4.00/unit,</p>";
            echo "<p>For Units Above 250 Units -  Rs. 5.20/unit,</p>";
            echo "<p>For 50 Units -  Rs. 6.50/unit,</p>";
        } else {
            echo "<p>No data submitted. Please enter units and click Calculate.</p>";
        }
        ?>
        <a href="index.html" class="btn btn-primary">Back</a>
        
    </div>
</div>
</body>
</html>