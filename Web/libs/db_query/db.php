<?php
require "import.php";

use DBQuery\Builder;

class DB
{
  public static function table($table, $as = null)
  {
    return new Builder($table, $as);
  }
}
