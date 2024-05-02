$(document).ready(function () {
  $('INPUT#language_code').on('keypress', function(event) {
    if (event.keyCode === 13) {
      $('INPUT#btn_translate').click();
    }
  });

  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
    $.get(url, function (response) {
      $('div#hello').text(response.hello);
    });
  });
});

