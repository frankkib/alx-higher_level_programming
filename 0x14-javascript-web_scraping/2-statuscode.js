#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
if (!url) {
  console.log('Please provide url argument');
  process.exit(1);
}
request.get(url, (error, response) => {
  if (error) {
    console.error('An error occurred when making a request:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
