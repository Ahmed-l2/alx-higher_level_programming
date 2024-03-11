#!/usr/bin/node

const num = Number(process.argv[2]);

function fact (x) {
  if (!x) {
    return (1);
  } else {
    return (x * fact(x - 1));
  }
}

console.log(fact(num));
