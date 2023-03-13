#!/usr/bin/node
const { argv } = require('node:process');
isNaN(argv[2])
  ? console.log('Not a number')
  : console.log(`My number: ${Number(argv[2])}`);
