#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const data = process.argv[3];

fs.writeFile(filename, data, 'utf-8', function (error) {
  if (error) {
    return console.log(error);
  }
});
