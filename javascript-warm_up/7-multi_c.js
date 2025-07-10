#!/usr/bin/node

// Ensure this file is executable: chmod +x 7-multi_c.js
const count = parseInt(process.argv[2], 10);

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
