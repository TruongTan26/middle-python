<?php

namespace DBQuery;

defined("DB_HOST") or defined("DB_NAME") or defined("DB_USER") or defined("DB_PASS") or exit("No configuration for connect database");

trait Connection
{
  /**
   * Database host name
   */
  private static $host = DB_HOST;

  /**
   * Database name
   */
  private static $dbname = DB_NAME;

  /**
   * The user to using database
   */
  private static $user = DB_USER;

  /**
   * The password of the user using database
   */
  private static $pass = DB_PASS;

  /**
   * Connect to database
   * @return PDO Return PDO connection
   */
  public static function connect():\PDO
  {
    $conn = new \PDO("mysql:host=" . self::$host . ";dbname=" . self::$dbname, self::$user, self::$pass);
    $conn->setAttribute(\PDO::ATTR_ERRMODE, \PDO::ERRMODE_EXCEPTION);
    return $conn;
  }
}
