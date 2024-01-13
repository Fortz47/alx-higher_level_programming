#!/usr/bin/node

const list = $('UL#list_movies');
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  for (const x of data.results) {
    const value = `<li>${x.title}</li>`;
    list
      .add(value)
      .appendTo(list);
  }
});
