import { createUnzip } from "zlib";

type Node = {
  value: number;
  next: Node;
};

const displayCups = (n: { [k: number]: number }, c: number) => {
  let r = `${c}`;
  let next = n[c];

  while (next !== c) {
    r += `${next}`;
    next = n[next];
  }

  console.log(r);
};

const updateCups = (
  next: { [k: number]: number },
  current: number,
  max: number,
) => {
  // pick
  const startpick = next[current];
  const middlepick = next[next[current]];
  const endpick = next[next[next[current]]];

  // find destination
  let destination = current === 1 ? max : current - 1;
  while (
    destination === startpick ||
    destination === middlepick ||
    destination === endpick
  ) {
    destination = destination === 1 ? max : destination - 1;
  }

  // re-arrange
  next[current] = next[endpick];
  next[endpick] = next[destination];
  next[destination] = startpick;
};

function handleInput_1(lines: Array<string>) {
  // test input
  let input = Array.from("389125467").map((n) => parseInt(n));
  // problem input
  // let input = Array.from("368195742").map((n) => parseInt(n));

  const max = Math.max(...input);
  let current: number = input[0];
  let next = {};

  input.forEach((c, i) => {
    if (i < input.length - 1) {
      next[c] = input[i + 1];
    } else {
      next[c] = input[0];
    }
  });

  for (let i = 0; i < 10; i++) {
    updateCups(next, current, max);
    current = next[current];
  }

  displayCups(next, 1);
  return 0;
}
function handleInput_2(lines: Array<string>) {
  // test input
  // let input = Array.from("389125467").map((n) => parseInt(n));
  // problem input
  let input = Array.from("368195742").map((n) => parseInt(n));

  for (let i = 10; i <= 1000000; i++) {
    input.push(i);
  }
  const max = 1000000;

  let current: number = input[0];
  let next = {};

  input.forEach((c, i) => {
    if (i < input.length - 1) {
      next[c] = input[i + 1];
    } else {
      next[c] = input[0];
    }
  });

  for (let i = 0; i < 10000000; i++) {
    updateCups(next, current, max);
    current = next[current];
  }

  console.log(next[1], next[next[1]]);
  return next[1] * next[next[1]];
}

export function handleInput(lines: Array<string>) {
  return [handleInput_1(lines), handleInput_2(lines)];
}

