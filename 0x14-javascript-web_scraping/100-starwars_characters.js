#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const link = 'https://swapi-api.alx-tools.com/api/films';
const movieId = argv[2];
request(link, (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    const characters = results[movieId - 1].characters;
    for (const character of characters) {
      request(character, (err, resp, bdy) => {
        if (!err) {
          const person = JSON.parse(bdy);
          console.log(person.name);
        }
      });
    }
  }
});
