#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length;
  const temp = [];
  while (len) {
    temp.push(list[len - 1]);
    len--;
  }
  return temp;
};
