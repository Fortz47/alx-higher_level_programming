#!/usr/bin/node

$(document).ready(() => {
  const addItem = $('DIV#add_item');
  const removeItem = $('DIV#remove_item');
  const clearList = $('DIV#clear_list');
  const list = $('UL.my_list');

  addItem.on('click', function () {
    list.append('<li>Item</li>');
  });

  removeItem.on('click', function () {
    $('UL.my_list li:last-child').remove();
  });

  clearList.on('click', function () {
    list.empty();
  });
});
