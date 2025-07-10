#!/usr/bin/node

// Prints the second biggest integer from a list of arguments
const args = process.argv.slice(2).map(n => parseInt(n, 10));

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
