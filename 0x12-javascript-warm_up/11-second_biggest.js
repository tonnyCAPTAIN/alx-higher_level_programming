#!/usr/bin/node

function sortNumber (a, b) {
  return a - b;
}
let argsLen = process.argv.length;
if (argsLen === 2 || argsLen === 3) {
  console.log('0');
} else {
  const arr = [];
  for (let i = 2; i < argsLen; i++) {
    arr.push(process.argv[i]);
  }
  arr.sort(sortNumber);
  console.log(arr[arr.length - 2]);
}
