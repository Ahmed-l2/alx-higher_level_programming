#!/usr/bin/node

const array1 = require('./100-data.js').list;
const map1 = array1.map((x, i) => x * i);

console.log(array1);
console.log(map1);
