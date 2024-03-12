#!/usr/bin/node

const OSquare = require('./5-square');

class Square extends OSquare {
  charPrint (c) {
    let cp = c;
    if (!cp) {
      cp = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let r = '';
      for (let j = 0; j < this.width; j++) {
        r += cp;
      }
      console.log(r);
    }
  }
}

module.exports = Square;
