#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const apiUrl = process.argv[2];
const filename = process.argv[3];

request(apiUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  fs.writeFile(filename, body, 'utf-8', function (error) {
    if (error) {
      return console.log(error);
    }
  });
});
