$(document).ready(function() {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(response) {
        $('div#hello').html(response.hello);
    });
});
