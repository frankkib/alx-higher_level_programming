#!/usr/bin/node

const argv = process.argv;
const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (arg1 === argv[2] && arg2 === argv[3]) {
  console.log(arg1 + ' is ' + arg2);
}
