#!/usr/bin/node

const request = require('request');

const movieId = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(movieId, async function (error, response, body) {
  if (!error) {
    const resJson = JSON.parse(body);
    const people = resJson.characters;
    for (const i of people) {
      const requestTime = await new Promise((resolve, reject) => {
        request(i, function (error, response, body) {
          if (!error) {
            resolve({ body });
          } else {
            reject(error);
          }
        });
      });
      console.log(JSON.parse(requestTime.body).name);
    }
  }
});
