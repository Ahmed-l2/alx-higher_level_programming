#!/usr/bin/node

const request = require('request');
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  const film = JSON.parse(body);
  const filmChars = film.characters.map(function (character) {
    return new Promise(function (resolve, reject) {
      request(character, function (error, response, body) {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  });

  Promise.all(filmChars).then(function (names) {
    console.log(names.join('\n'));
  });
});
