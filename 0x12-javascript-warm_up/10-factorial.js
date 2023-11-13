#!/usr/bin/node

function recursiveHelper (n) {
  if (n === 0) {
    return (1);
  }
  return (n * recursiveHelper(n - 1));
}

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  const num = recursiveHelper(n);
  return (num);
}

const value = process.argv[2];
console.log(factorial(value));
