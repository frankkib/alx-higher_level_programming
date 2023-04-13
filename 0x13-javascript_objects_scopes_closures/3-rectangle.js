#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
	    return Object.create(null);
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (!this.width || !this.height) {
      return;
    }

    let rect = '';
    for (let i = 0; i < this.height; i++) {
	console.log('X'.repeat(this.width));
      }
    }
  };
