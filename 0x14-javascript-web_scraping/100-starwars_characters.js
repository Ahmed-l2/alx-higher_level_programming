#!/usr/bin/node

const request = require('request');
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  const film = JSON.parse(body);
  const filmChars = film.characters;

  for (const character of filmChars) {
    request(character, function (error, response, body) {
      if (error) {
        return console.log(error);
      }

      const chars = JSON.parse(body);
      console.log(chars.name);
    });
  }
});
