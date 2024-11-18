const weapons = { 8: [4, 0], 10: [5, 0], 25: [6, 0], 40: [7, 0], 74: [8, 0] };

const armor = {
  0: [0, 0],
  13: [0, -1],
  31: [0, -2],
  53: [0, -3],
  75: [0, -4],
  102: [0, -5],
};

const rings = {
  0: [0, 0],
  25: [1, 0],
  50: [2, 0],
  100: [3, 0],
  20: [0, -1],
  40: [0, -2],
  80: [0, -3],
};

type Stats = [number, number];

type Player = {
  health: number;
  stats: Stats;
};

type StatsSetup = [number, Stats, Array<string>];

const mergeStats = (...stats: Array<Stats>): Stats => {
  let stat: Stats = [0, 0];
  stats.forEach((s) => {
    stat = [stat[0] + s[0], stat[1] + s[1]];
  });
  return stat;
};

const nbTurnToDeath = (attacker: Player, defender: Player): number => {
  const actualDamage = Math.max(attacker.stats[0] + defender.stats[1], 1);

  return Math.ceil(defender.health / actualDamage);
};

const wins = (player1: Player, player2: Player): boolean => {
  const player1TurnsToDeath = nbTurnToDeath(player2, player1);
  const player2TurnsToDeath = nbTurnToDeath(player1, player2);
  return player1TurnsToDeath >= player2TurnsToDeath;
};

const allCombinations = (a: Array<any>): Array<Array<any>> => {
  var combi = [];
  var temp = [];
  var slent = Math.pow(2, a.length);

  for (var i = 0; i < slent; i++) {
    temp = [];
    for (var j = 0; j < a.length; j++) {
      if (i & Math.pow(2, j)) {
        temp.push(a[j]);
      }
    }
    if (temp.length > 0) {
      combi.push(temp);
    }
  }

  combi.sort((a, b) => a.length - b.length);
  return combi;
};

const getPossibleSetups = (): Array<StatsSetup> => {
  const possibleWeaponsSetup: Array<StatsSetup> = Object.keys(weapons).map(
    (k): StatsSetup => {
      return [parseInt(k), weapons[k], ["Weapons : " + k]];
    },
  );

  const possibleArmorSetup: Array<StatsSetup> = Object.keys(armor).map(
    (k: string): StatsSetup => {
      return [parseInt(k), armor[k], [`Armor : ${k}`]];
    },
  );

  const possibleRingsSetups: Array<StatsSetup> = allCombinations(
    Object.keys(rings),
  )
    .filter((c) => c.length <= 2)
    .map((combination: Array<string>): StatsSetup => {
      const g = combination.reduce((s, c) => s + parseInt(c), 0);
      const stats: Stats = combination.reduce(
        (st: Stats, s: string): Stats => mergeStats(st, rings[s]),
        [0, 0],
      );
      return [g, stats, [`Rings : ${combination.join("/")}`]];
    })
    .sort((a, b) => a[0] - b[0]);

  // by default must have one weapon
  const possibleSetups = [];
  possibleWeaponsSetup.forEach((weaponSetup) => {
    possibleArmorSetup.forEach((armorSetup) => {
      possibleRingsSetups.forEach((ringSetup) => {
        possibleSetups.push([
          weaponSetup[0] + armorSetup[0] + ringSetup[0],
          mergeStats(weaponSetup[1], armorSetup[1], ringSetup[1]),
          weaponSetup[2].concat(armorSetup[2], ringSetup[2]),
        ]);
      });
    });
  });

  return possibleSetups;
};
function handleInput_1(lines: Array<string>) {
  const boss: Player = { health: 103, stats: [9, -2] };

  let you: Player = { health: 100, stats: [1, 0] };
  let possibleSetups = getPossibleSetups();

  possibleSetups.sort((a, b) => a[0] - b[0]);

  for (let i in possibleSetups) {
    const p = possibleSetups[i];
    you.stats = p[1];
    if (wins(you, boss)) {
      console.log(p, you, boss);
      return p[0];
    }
  }

  throw new Error("no Wins found");
}

function handleInput_2(lines: Array<string>) {
  const boss: Player = { health: 103, stats: [9, -2] };

  let you: Player = { health: 100, stats: [1, 0] };
  let possibleSetups = getPossibleSetups();

  possibleSetups.sort((a, b) => b[0] - a[0]);

  for (let i in possibleSetups) {
    const p = possibleSetups[i];
    you.stats = p[1];
    if (!wins(you, boss)) {
      return p[0];
    }
  }
  throw new Error("no Loss found");
}

export function handleInput(lines: Array<string>) {
  return [handleInput_1(lines), handleInput_2(lines)];
}
