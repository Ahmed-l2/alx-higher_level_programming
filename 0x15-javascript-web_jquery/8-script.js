$(document).ready(function () {
  const films = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.getJSON(films, function (response) {
    for (const film of response.results) {
      $('ul#list_movies').append(`<li>${film.title}</li>`);
    }
  });
});
