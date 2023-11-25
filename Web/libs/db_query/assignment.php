<?php

namespace DBQuery;

class Assignment
{
  private $column;
  private $value;

  public function __construct($column, $value = null)
  {
    $this->column = $column;
    $this->value = $value;
  }

  public function build(): string
  {
    if (is_string($this->value)) {
      return "$this->column = \"$this->value\"";
    } else {
      return "$this->column = $this->value";
    }
  }
}
