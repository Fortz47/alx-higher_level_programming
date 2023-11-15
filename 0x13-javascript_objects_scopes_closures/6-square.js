#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    this.print(c);
  }
}

module.exports = Square;
