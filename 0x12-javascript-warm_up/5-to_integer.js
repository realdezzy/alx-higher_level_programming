#!/usr/bin/node
isNaN(process.argv[2])
  ? console.log('Not a number')
  : console.log(`My number: ${Math.floor(Number(process.argv[2]))}`);
