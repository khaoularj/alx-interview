#!/usr/bin/node

const request = require('request');

const filmNumber = process.argv[2] + '/';
const filmUrl = 'https://swapi-api.hbtn.io/api/films/';

request(filmUrl + filmNumber, async function (Error, response, bd) {
  if (Error) {
    console.error(Error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch film data. Status code: ${response.statusCode}`);
    return;
  }

  let charUrlLs;
  try {
    charUrlLs = JSON.parse(bd).characters;
  } catch (parseError) {
    console.error('Error parsing response body:', parseError);
    return;
  }

  for (const charURL of charUrlLs) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (Error, response, bd) {
        if (Error) {
          console.error(Error);
          return reject(Error);
        }

        if (response.statusCode !== 200) {
          console.error(`Failed to fetch character data. Status code: ${response.statusCode}`);
          return reject(new Error(`Status code: ${response.statusCode}`));
        }

        try {
          const character = JSON.parse(bd);
          console.log(character.name);
        } catch (parseError) {
          console.error('Error parsing character response body:', parseError);
          return reject(parseError);
        }
        resolve();
      });
    });
  }
});
