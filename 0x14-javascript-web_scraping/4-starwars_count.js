#!/usr/bin/node

const url = process.argv[2];

const request = require('request');

const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const bodyObj = JSON.parse(body);
  const results = bodyObj.results;
  let count = 0;
  for (let i = 0; i < results.length; i++) {
    results[i].characters.forEach((item) => {
      if (wedge === item) {
        count += 1;
      }
    });
  }
  console.log(count);
});
