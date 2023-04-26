#!/usr/bin/node
const { argv } = require('process');
const requests = require('request');
const fs = require('fs');

const link = argv[2];
const path = argv[3];

requests(link, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFileSync(path, body, { flag: 'w+', encoding: 'utf-8' });
  }
});
