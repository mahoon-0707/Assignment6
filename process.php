<?php

// Retrieve and validate inputs from URL query parameters
$inputs = [];
for ($i = 1; $i <= 5; $i++) {
    if (isset($_GET["num$i"]) && ctype_digit($_GET["num$i"])) {
        $inputs[] = (int)$_GET["num$i"];
    } else {
        echo "Error: All inputs (num1, num2, ...) must be integers.\n";
        exit;
    }
}

// Bitwise operations
$andResult = $inputs[0];
$orResult = $inputs[0];
$xorResult = $inputs[0];

for ($i = 1; $i < count($inputs); $i++) {
    $andResult &= $inputs[$i];
    $orResult |= $inputs[$i];
    $xorResult ^= $inputs[$i];
}

// Output bitwise results
echo "Bitwise AND result: $andResult\n";
echo "Bitwise OR result: $orResult\n";
echo "Bitwise XOR result: $xorResult\n";

// Threshold filtering
if (isset($_GET['threshold']) && ctype_digit($_GET['threshold'])) {
    $threshold = (int)$_GET['threshold'];
    $filteredNumbers = array_filter($inputs, function($num) use ($threshold) {
        return $num > $threshold;
    });
    echo "Numbers greater than $threshold: " . implode(", ", $filteredNumbers) . "\n";
} else {
    echo "Error: Threshold must be an integer.\n";
}

?>
