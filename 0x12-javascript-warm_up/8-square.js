#!/usr/bin/node

const num = Number(process.argv[2]);

if (num) {
  for (let i = 0; i < num; i++) {
    let r = '';
    for (let j = 0; j < num; j++) {
      r += 'X';
    }
    console.log(r);
  }
} else {
  console.log('Missing size');
}
