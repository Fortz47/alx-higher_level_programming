#!/usr/bin/node

const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, (err) => {
  if (err) {
    console.log(err);
  }
}).pipe(fs.createWriteStream(filePath, 'utf-8'));
