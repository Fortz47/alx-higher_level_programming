#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const dict = {};
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const bodyObj = JSON.parse(body);
  bodyObj.forEach((item) => {
    if (item.completed === true) {
      const id = item.userId;
      if (id in dict) {
        dict[id] += 1;
      } else {
        dict[id] = 1;
      }
    }
  });
  console.log(dict);
});
