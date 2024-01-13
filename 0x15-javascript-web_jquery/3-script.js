#!/usr/bin/node

const list = $('UL.my_list');

$('#add_item').on('click', function (event) {
  list
    .add('<li>Item</li>')
    .appendTo(list);
});
