#!/usr/bin/node
// Start Wars Movie Characters Script
// The movie ID is passed as the first position argument.

const request = require('request');

const movieId = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];

request.get(url, (err, response, body) => {
    if (err) {
      console.log(err)
    } else if (response.statusCode === 200) {
      const film = JSON.parse(body);
      const characterPromises = film.characters.map(characterURL =>
        new Promise((resolve, reject) => {
          request.get(characterURL, (err, response, body) => {
            if (err) {
              reject(err);
             } else if (response.statusCode === 200) {
               const character = JSON.parse(body);
               resolve(character.name);
             } else {
               reject(new Error('request failed with status code ${response.statusCode}'));
             }
        });
      })
    );

// Wait for all promises to resolve, then print the character names

       Promise.all(characterPromises)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(error => {
        console.log(error);
      });
  } else {
    console.log(`Request failed with status code ${response.statusCode}`);
  }
});
