<?php

namespace DBQuery;

trait Execution {
  public function execSelect() {
    $this->buildSelect();
    $conn = Connection::connect();
    $stmt = $conn->query($this->sql);
    return $stmt->fetchAll(\PDO::FETCH_ASSOC);
  }

  public function execSelectSingle() {
    $this->buildSelect();
    $conn = Connection::connect();
    $stmt = $conn->query($this->sql);
    return $stmt->fetch(\PDO::FETCH_ASSOC);
  }

  public function execInsert() {
    $this->buildInsert();
    $conn = Connection::connect();
    $stmt = $conn->query($this->sql);
    return $stmt->fetch(\PDO::FETCH_ASSOC);
  }

  public function execUpdate() {
    $this->buildUpdate();
    $conn = Connection::connect();
    return $conn->query($this->sql);
  }

  public function execDelete() {
    $this->buildDelete();
    $conn = Connection::connect();
    return $conn->query($this->sql);
  }

}