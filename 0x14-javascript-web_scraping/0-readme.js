#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

fs.readFile(argv[2],
  { encoding: 'utf8', flag: 'r' },
  function (err, data) {
    if (err) { console.log(err); } else { console.log(data); }
  });
