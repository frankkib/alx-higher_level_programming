#!/usr/bin/node

const argCount = process.argv.length - 2;

if (argCount === 0) {
  console.log('No argument');
} else if (argCount === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
