<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menu</title>
</head>
<body>
    <?php include('./libs/header.php')?>
    <?php  $query = mysqli_query($db, "SELECT * FROM tbl_menu");    ?>

    <table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Name</th>
      <th scope="col">Price</th>
      <th scope="col">Group</th>
    </tr>
  </thead>
  <tbody>
    <?php while($row = mysqli_fetch_array($query)){ ?>
    <tr>
      <th><?= $row['menu_id'] ?></th>
      <td><?= $row['menu_name'] ?></td>
      <td><?= $row['menu_price'] ?></td>
      <td><?= $row['menu_group'] ?></td>
    </tr>
  <?php } ?>
  </tbody>
</table>

</body>
</html>