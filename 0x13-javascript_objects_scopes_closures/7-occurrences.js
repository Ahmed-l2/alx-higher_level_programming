#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nb += 1;
    }
  }
  return nb;
};
