#!/usr/bin/node

exports.converter = function (base) {
  return (num) => {
    return Number(num).toString(base);
  };
};
