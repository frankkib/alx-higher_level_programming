#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide the Movie ID as an argument.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred while making the request:', error);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      const characters = movie.characters;

      if (characters.length === 0) {
        console.log('No characters found for the specified movie.');
      } else {
        characters.forEach((characterUrl) => {
          request.get(characterUrl, (characterError, characterResponse, characterBody) => {
            if (characterError) {
              console.error('An error occurred while fetching character data:', characterError);
            } else {
              if (characterResponse.statusCode === 200) {
                const character = JSON.parse(characterBody);
                console.log(character.name);
              } else {
                console.error('Request failed with status code:', characterResponse.statusCode);
              }
            }
          });
        });
      }
    } else {
      console.error('Request failed with status code:', response.statusCode);
    }
  }
});
