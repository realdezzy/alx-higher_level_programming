#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const Url = argv[2];
request(Url, (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    let counter = 0;
    for (const movie of results) {
      if (movie.characters.find(value => value.endsWith('18/'))) {
        counter++;
      }
    }
    console.log(counter);
  }
});
