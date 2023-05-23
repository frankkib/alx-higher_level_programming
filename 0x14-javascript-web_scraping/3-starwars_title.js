#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide the movie ID as an argument.');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('An error occurred while making the request:', error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } else if (response.statusCode === 404) {
      console.log('Movie not found.');
    } else {
      console.error('Request failed with status code:', response.statusCode);
    }
  }
});
