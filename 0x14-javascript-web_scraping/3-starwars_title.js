#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

const link = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(link, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const output = JSON.parse(body);
    console.log(output.title);
  }
});
