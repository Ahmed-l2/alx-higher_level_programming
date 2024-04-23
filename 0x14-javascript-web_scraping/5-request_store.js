#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const apiUrl = process.argv[2];
const filename = process.argv[3];

request(apiUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  const films = JSON.parse(body).results;

  let count = 0;
  for (const film of films) {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  fs.writeRead()
});
