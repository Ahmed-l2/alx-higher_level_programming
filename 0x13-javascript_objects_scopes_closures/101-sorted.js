#!/usr/bin/node

const dict1 = require('./101-data').dict;

const dict2 = {};

for (const key in dict1) {
  const value = dict1[key];
  if (Object.prototype.hasOwnProperty.call(dict2, value)) {
    dict2[value].push(key);
  } else {
    dict2[value] = [key];
  }
}
console.log(dict2);
