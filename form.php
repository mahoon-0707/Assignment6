<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment #6</title>
  </head>
  <body>
    <h2>Assignment #6</h2>

    <form action="process.php" method="POST">
      <label for="integers">Enter a list of integers separated by comma</label>
      <input type="text" id="integers" name="integers" required><br><br>
      <label for="threshold">Threshold</label>
      <input type="text" id="threshold" name="threshold" required><br><br>

      <button type="submit">Submit</button>
    </form>
  </body>
</html>