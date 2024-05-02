$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
    $.get(url, function (response) {
      $('div#hello').text(response.hello);
    });
  });
});
