#!/usr/bin/node

const args = process.argv.slice(2).map(Number); // Convert arguments to numbers

// If no arguments or only one argument, print 0
if (args.length <= 1) {
  console.log(0);
} else {
  // Find the second biggest integer
  const sortedArgs = args.sort((a, b) => b - a);
  const secondBiggest = sortedArgs[1];

  console.log(secondBiggest);
}
