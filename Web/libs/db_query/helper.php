<?php

namespace DBQuery;
trait Helper {
  public static function pushCondition(&$conditions, $condition, $boolean = null) {
    if (empty($conditions) || !isset($boolean)) {
      array_push($conditions, $condition);
    } else {
      array_push($conditions, "$boolean $condition");
    }
  }

  public static function pushAssignment(&$assignments, $assignment)
  {
    array_push($assignments, $assignment);
  }
}