#!/usr/bin/node

const argFirst = process.argv[2];
if (argFirst) {
  console.log(argFirst);
} else {
  console.log('No argument');
}
