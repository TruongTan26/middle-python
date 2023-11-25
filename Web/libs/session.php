<?php

class Session
{

  static function init()
  {
    if (session_status() == PHP_SESSION_NONE) {
      session_start();
    }
  }

  static function set($key, $value)
  {
    self::init();
    $_SESSION[$key] = $value;
  }

  static function get($key)
  {
    self::init();
    if (isset($_SESSION[$key])) {
      return $_SESSION[$key];
    }
    return null;
  }

  static function unset($key)
  {
    self::init();
    unset($_SESSION[$key]);
  }


  static function destroy()
  {
    self::init();
    session_destroy();
  }

  public static function checkSession()
  {
    self::init();
    if (self::get("adminUser") == false) {
      self::destroy();
      header("Location:login.php");
    }
  }
  public static function checkSessions()
  {
    self::init();
    if (self::get("userUser") == false) {
      self::destroy();
      header("Location:login.php");
    }
  }

  public static function checkSessionStaff()
  {
    self::init();
    if (self::get("staffUser") == false) {
      self::destroy();
      header("Location:login.php");
    }
  }

  public static function checkLogin()
  {
    self::init();
    if (self::get("login") == true) {
      header("Location:index.php");
    }
  }

  public static function logout()
  {
    self::destroy();
    header("Location:login.php");
  }
}
