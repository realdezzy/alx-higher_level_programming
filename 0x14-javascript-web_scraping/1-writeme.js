#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

try {
  fs.writeFileSync(argv[2], argv[3], { flag: 'w+', encoding: 'utf-8' });
} catch (err) {
  console.error(err);
}
