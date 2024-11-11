const getHands = (lines: Array<string>): [Array<number>, Array<number>] => {
  let i = 1;
  let hand1 = [];
  while (lines[i] !== "") {
    hand1.push(parseInt(lines[i]));
    i++;
  }

  let hand2 = [];
  i += 2;
  while (i < lines.length && lines[i] !== "") {
    hand2.push(parseInt(lines[i]));
    i++;
  }

  return [hand1, hand2];
};
function handleInput_1(lines: Array<string>) {
  let [hand1, hand2] = getHands(lines);

  while (hand1.length !== 0 && hand2.length !== 0) {
    const one = hand1.shift();
    const two = hand2.shift();

    if (one > two) {
      hand1 = hand1.concat([one, two]);
    } else if (two > one) {
      hand2 = hand2.concat([two, one]);
    }
  }

  return hand1.length === 0 ? getScore(hand2) : getScore(hand1);
}

const getScore = (hand: Array<number>): number => {
  return hand.reverse().reduce((s, n, i) => s + n * (i + 1));
};

const recursiveCombat = (
  h1: Array<number>,
  h2: Array<number>,
): [1 | 2, Array<number>] => {
  let drawnHands = new Set();
  const drawnHandsString = (
    hand1: Array<number>,
    hand2: Array<number>,
  ): string => {
    return hand1.join(",") + "-" + hand2.join(",");
  };

  while (h1.length !== 0 && h2.length !== 0) {
    if (drawnHands.has(drawnHandsString(h1, h2))) {
      return [1, []];
    }

    drawnHands.add(drawnHandsString(h1, h2));

    const [one, two] = [h1.shift(), h2.shift()];

    let winner = null;
    if (h1.length >= one && h2.length >= two) {
      // recursiveCombat
      winner = recursiveCombat(h1.slice(0, one), h2.slice(0, two))[0];
    } else {
      winner = one > two ? 1 : 2;
    }

    if (winner === 1) {
      h1 = h1.concat([one, two]);
    } else {
      h2 = h2.concat([two, one]);
    }
  }

  return h1.length === 0 ? [2, h2] : [1, h1];
};

function handleInput_2(lines: Array<string>) {
  /**
   * 0. if exactly same round => Player 1 wins
   * 1. if both players have at least the amount of card the drew => recursive combat winner is the winner of the round
   *    => a recursive combat is a game with the cards being the next n cards for each player where n is the value they drew
   * 2. normal challenge
   *
   * => winner of the round takes the 2 card and put its card first
   **/
  const [h1, h2] = getHands(lines);
  const [_, hand] = recursiveCombat(h1, h2);

  return getScore(hand);
}

export function handleInput(lines: Array<string>) {
  return [handleInput_1(lines), handleInput_2(lines)];
}

