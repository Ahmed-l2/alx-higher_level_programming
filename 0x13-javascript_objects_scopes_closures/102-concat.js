#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function(err, dataA) {
  fs.readFile(process.argv[3], 'utf8', function(err, dataB) {
    fs.writeFile(process.argv[4], dataA + dataB, function(err) {
      if (err) throw err;
    });
  });
});
