const transform = (value: number, subjectNumber: number): number => {
  return (value * subjectNumber) % 20201227;
};
const getLoopSize = (key: number, subjectNumber: number = 7): number => {
  let value = 1;

  let n = 0;
  while (value !== key) {
    value = transform(value, subjectNumber);
    n += 1;
  }

  return n;
};

const getEncryptionKey = (subjectNumber: number, loopSize: number): number => {
  let value = 1;
  for (let i = 0; i < loopSize; i++) {
    value = transform(value, subjectNumber);
  }
  return value;
};

function handleInput_1(lines: Array<string>) {
  const cardKey = parseInt(lines[0]);
  const doorKey = parseInt(lines[1]);

  const cardLoopSize = getLoopSize(cardKey);
  const doorLoopSize = getLoopSize(doorKey);

  const encryptionKey = getEncryptionKey(cardKey, doorLoopSize);

  return encryptionKey;
}

function handleInput_2(lines: Array<string>) {
  return 0;
}

export function handleInput(lines: Array<string>) {
  return [handleInput_1(lines), handleInput_2(lines)];
}

