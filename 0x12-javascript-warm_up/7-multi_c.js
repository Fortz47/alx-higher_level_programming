#!/usr/bin/node

const arg = process.argv[2];
let num = parseInt(arg);
if (isNaN(num) || !arg) {
  console.log('Missing number of occurrences');
} else {
  while (num) {
    console.log('C is fun');
    num--;
  }
}
