#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) console.log('Missing size');
else {
  for (let i = 0; i < Number(size); i++) {
    let onerow = '';
    for (let j = 0; j < Number(size); j++) onerow += 'X';
    console.log(onerow);
  }
}
