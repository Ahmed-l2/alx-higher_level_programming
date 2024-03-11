#!/usr/bin/node

if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  let temp = Number(process.argv[2]);
  for (let i = 3; i < process.argv.length; i++) {
    if (temp < Number(process.argv[i])) {
      temp = Number(process.argv[i]);
    }
  }
  console.log(temp);
}
