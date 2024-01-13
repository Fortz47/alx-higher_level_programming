#!/usr/bin/node

const header = $('header');

$('#toggle_header').on('click', function (event) {
  if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else {
    header.removeClass('green');
    header.addClass('red');
  }
});
