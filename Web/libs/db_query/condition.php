<?php

namespace DBQuery;

class Condition
{
  private $column;
  private $operator;
  private $value;

  public function __construct($column, $operator = null, $value = null)
  {
    $this->column = $column;
    $this->operator = $operator;
    $this->value = $value;
  }

  public function build(): string
  {
    if (!isset($this->operator) && !isset($this->value)) {
      return $this->column;
    } else if (!isset($this->value)) {
      return "$this->column = \"$this->operator\"";
    } else {
      return "$this->column $this->operator \"$this->value\"";
    }
  }
}
