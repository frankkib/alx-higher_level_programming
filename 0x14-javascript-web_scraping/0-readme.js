#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
if (!filePath) {
  console.log('Please provide the file path as an argument.');
  process.exit(1);
}
try {
  const fileContent = fs.readFileSync(filePath, 'utf-8');
  console.log(fileContent);
} catch (err) {
  console.log('An error occurred while reading the file:');
  console.log(err);
}
