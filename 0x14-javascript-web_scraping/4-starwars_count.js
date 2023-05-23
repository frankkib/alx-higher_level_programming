#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.log('Please provide the API URL as an argument.');
  process.exit(1);
}

const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred while making the request:', error);
  } else {
    if (response.statusCode === 200) {
      const filmsData = JSON.parse(body).results;
      const moviesWithWedgeAntilles = filmsData.filter((film) => {
        const characters = film.characters.map((characterUrl) => {
          const characterIdMatch = characterUrl.match(/\/(\d+)\/$/);
          return characterIdMatch ? parseInt(characterIdMatch[1]) : null;
        });
        return characters.includes(characterId);
      });
      console.log(moviesWithWedgeAntilles.length);
    } else {
      console.error('Request failed with status code:', response.statusCode);
    }
  }
});
