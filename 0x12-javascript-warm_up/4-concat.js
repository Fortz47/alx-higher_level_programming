#!/usr/bin/node

const args = process.argv;

if (args.length > 2) {
  if (args[3]) {
    console.log(`${args[2]} is ${args[3]}`);
  } else {
    console.log(`${args[2]} is undefined`);
  }
} else {
  console.log('undefined is undefined');
}
