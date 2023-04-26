#!/usr/bin/node
const { argv } = require('process');
const requests = require('request');

const link = argv[2];
const temp = {};
requests(link, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const output = JSON.parse(body);

    for (let i = 1; i < output.length; i++) {
      if (output[i].completed === true) {
        if (!temp[`${output[i].userId}`]) {
          temp[`${output[i].userId}`] = 1;
        } else {
          temp[`${output[i].userId}`] = temp[`${output[i].userId}`] + 1;
        }
      }
    }
    console.log(temp);
  }
});
