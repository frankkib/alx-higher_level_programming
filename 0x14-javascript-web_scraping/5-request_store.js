#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.log('Please provide the URL and file path as arguments.');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error('An error occurred while making the request:', error);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf8', (error) => {
        if (error) {
          console.error('An error occurred while writing the file:', error);
        } else {
          console.log('File saved successfully.');
        }
      });
    } else {
      console.error('Request failed with status code:', response.statusCode);
    }
  }
});
