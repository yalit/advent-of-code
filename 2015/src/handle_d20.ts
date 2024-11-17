type Factors = { [k: number]: number };

const range = (n: number, step: number = 1): Array<number> => {
  let r = [];

  for (let i = 1; i <= n; i += step) r.push(i);

  return r;
};

const primeFactors = (n: number): Factors => {
  let factors: Factors = {};

  const addToFactors = (x: number) => {
    if (!(x in factors)) {
      factors[x] = 0;
    }
    factors[x]++;
  };
  while (n % 2 === 0) {
    addToFactors(2);
    n /= 2;
  }

  for (let i = 3; i <= Math.sqrt(n); i = i + 2) {
    while (n % i === 0) {
      addToFactors(i);
      n /= i;
    }
  }

  if (n > 2) addToFactors(n);

  return factors;
};

const sumDividers = (n: number): number => {
  const factors = primeFactors(n);

  return Object.keys(factors).reduce((s, x) => {
    const k = parseInt(x);
    return (s * (k ** (factors[k] + 1) - 1)) / (k - 1);
  }, 1);
};

const limitedDividers = (n: number): Array<number> => {
  return range(n).filter((x) => n % x === 0 && Math.floor(n / x) < 51);
};

const sumDividersLimited = (n: number): number => {
  const ds = limitedDividers(n);

  return ds.reduce((s, n) => s + n);
};

function handleInput_1(lines: Array<string>) {
  const target = 34000000 / 10;

  let i = 1;
  let t = sumDividers(i);
  while (t < target) {
    i++;
    t = sumDividers(i);
  }
  return i;
}

function handleInput_2(lines: Array<string>) {
  const target = 34000000 / 11;

  let i = handleInput_1(lines);
  let t = sumDividersLimited(i);
  while (t < target) {
    i++;
    t = sumDividersLimited(i);
  }
  return i;
}

export function handleInput(lines: Array<string>) {
  return [handleInput_1(lines), handleInput_2(lines)];
}
