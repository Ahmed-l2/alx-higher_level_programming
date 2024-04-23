#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    return console.log(error);
  }
  return console.log(`code: ${response.statusCode}`);
});
