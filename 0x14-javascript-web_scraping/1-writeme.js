#!/usr/bin/node
const fs = require('fs');

const [, , filePath, fileContent] = process.argv;

if (!filePath || !fileContent) {
  process.exit(1);
}
fs.writeFile(filePath, fileContent, 'utf-8', (err) => {
  if (err) {
    console.log('An error occurred while writing to the file:');
    console.log(err);
  }
});
