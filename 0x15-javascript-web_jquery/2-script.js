#!/usr/bin/node

const header = $('header');
$('#red_header').on('click', function (event) {
  header.css('color', '#FF0000');
});
