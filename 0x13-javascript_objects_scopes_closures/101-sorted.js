#!/usr/bin/node

const dict1 = require('./101-data').dict;

let dict2 = {};

for (let key in dict1) {
  let value = dict1[key];
  if (dict2.hasOwnProperty(value)) {
    dict2[value].push(key);
  } else {
    dict2[value] = [key];
  }
}
console.log(dict2);
