#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (ch = 'X') {
    if (this.height && this.width) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += ch;
        }
        console.log(row);
      }
    }
  }

  rotate () {
    if (this.height && this.width) {
      const width = this.width;
      this.width = this.height;
      this.height = width;
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
