#!/usr/bin/node

const id = process.argv[2];

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const bodyObj = JSON.parse(body);
  console.log(bodyObj.title);
});
