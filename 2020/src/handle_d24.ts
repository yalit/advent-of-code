type Tile = [number, number];
type MinMax = { min: number; max: number };
type Corners = {
  x: MinMax;
  y: MinMax;
};

const directions = {
  e: [2, 0],
  se: [1, 1],
  sw: [-1, 1],
  w: [-2, 0],
  nw: [-1, -1],
  ne: [1, -1],
};

const flipTile = (tiles: Set<string>, tile: Tile) => {
  const s = `${tile[0]}_${tile[1]}`;
  if (tiles.has(s)) {
    tiles.delete(s);
  } else {
    tiles.add(s);
  }
};

const gridHasTile = (tiles: Set<string>, tile: Tile): boolean => {
  return tiles.has(`${tile[0]}_${tile[1]}`);
};

const getBlackTiles = (lines: Array<string>): Set<string> => {
  let tiles = new Set<string>();

  let referenceTile: Tile = [0, 0];
  lines.forEach((l) => {
    let i = 0;

    let currentTile: Tile = Object.assign([], referenceTile);
    while (i < l.length) {
      let dx: number, dy: number;
      if (["e", "w"].includes(l[i])) {
        [dx, dy] = directions[l[i]];
        i++;
      } else {
        [dx, dy] = directions[l.slice(i, i + 2)];
        i += 2;
      }
      currentTile = [currentTile[0] + dx, currentTile[1] + dy];
    }

    flipTile(tiles, currentTile);
  });

  return tiles;
};

function handleInput_1(lines: Array<string>) {
  const tiles = getBlackTiles(lines);
  return tiles.size;
}

function handleInput_2(lines: Array<string>) {
  let blackTiles = getBlackTiles(lines);

  const getCorners = (set: Set<string>): Corners => {
    let [minX, minY, maxX, maxY] = [0, 0, 0, 0];

    const getX = (s: string): number => parseInt(s.split("_")[0]);
    const getY = (s: string): number => parseInt(s.split("_")[1]);

    return {
      x: {
        min: Array.from(set).reduce((m, i) => (getX(i) < m ? getX(i) : m), 0),
        max: Array.from(set).reduce((m, i) => (getX(i) > m ? getX(i) : m), 0),
      },
      y: {
        min: Array.from(set).reduce((m, i) => (getY(i) < m ? getY(i) : m), 0),
        max: Array.from(set).reduce((m, i) => (getY(i) > m ? getY(i) : m), 0),
      },
    };
  };

  const getBlackNeighbors = (tiles: Set<string>, tile: Tile): Array<Tile> => {
    return Object.values(directions)
      .map(([dx, dy]): Tile => [tile[0] + dx, tile[1] + dy])
      .filter((t: Tile) => gridHasTile(tiles, t));
  };

  for (let i = 0; i < 100; i++) {
    let newTiles = new Set(blackTiles);
    const corners: Corners = getCorners(newTiles);

    for (let x = corners.x.min - 1; x <= corners.x.max + 1; x++) {
      for (let y = corners.y.min - 1; y <= corners.y.max + 1; y++) {
        if ((y % 2 == 0 && x % 2 == 1) || (y % 2 == 1 && x % 2 == 0)) {
          // coordinates are alawys the same odd or evenness
          continue;
        }

        const currentTile: Tile = [x, y];
        const blackNeighbors = getBlackNeighbors(
          blackTiles,
          currentTile,
        ).length;
        if (
          gridHasTile(blackTiles, currentTile) &&
          (blackNeighbors === 0 || blackNeighbors > 2)
        ) {
          flipTile(newTiles, currentTile);
        } else if (
          !gridHasTile(blackTiles, currentTile) &&
          blackNeighbors === 2
        ) {
          flipTile(newTiles, currentTile);
        }
      }
    }

    blackTiles = newTiles;
  }

  return blackTiles.size;
}

export function handleInput(lines: Array<string>) {
  return [handleInput_1(lines), handleInput_2(lines)];
}

