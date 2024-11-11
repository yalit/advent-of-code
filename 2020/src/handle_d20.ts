/**
 * Tiles need to be ordered
 * Each tile has neighbors
 * the outer edges of the pattern are unique
 */

type Edges = {
  top: string;
  right: string;
  bottom: string;
  left: string;
};

type EdgeSide = keyof Edges;

type Tile = {
  id: string;
  lines: Array<string>;
  edges: Edges;
};

const getTiles = (lines: Array<string>): Array<Tile> => {
  const tiles: Array<Tile> = [];

  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (line.startsWith("Tile")) {
      const id = line.split(" ")[1].slice(0, -1);

      // always 10 lines for a tile
      const tileLines = lines.slice(i + 1, i + 11);
      tiles.push({ id, lines: tileLines, edges: getEdges(tileLines) });
      i += 10;
    }

    i++;
  }

  return tiles;
};

const getEdges = (tileLines: Array<string>): Edges => {
  return {
    top: tileLines[0],
    right: tileLines.map((l) => l[9]).join(""),
    bottom: tileLines[9],
    left: tileLines.map((l) => l[0]).join(""),
  };
};

const getReversedEdges = (edges: Edges): Edges => {
  return {
    top: edges.top.split("").reverse().join(""),
    right: edges.right.split("").reverse().join(""),
    bottom: edges.bottom.split("").reverse().join(""),
    left: edges.left.split("").reverse().join(""),
  };
};

const rotateTile = (tile: Tile): Tile => {
  let newlines = [];

  for (let i = tile.lines.length - 1; i >= 0; i--) {
    newlines.push(tile.lines.map((l) => l[i]).join(""));
  }

  return { id: tile.id, lines: newlines, edges: getEdges(newlines) };
};

const flipTile = (tile: Tile): Tile => {
  const newLines = tile.lines.map((l) => l.split("").reverse().join(""));
  return {
    id: tile.id,
    lines: newLines,
    edges: getEdges(newLines),
  };
};

const isMatchingRight = (from: Tile, to: Tile): boolean => {
  return from.edges.right === to.edges.left;
};

const isMatchingBottom = (from: Tile, to: Tile): boolean => {
  return from.edges.bottom === to.edges.top;
};

function handleInput_1(lines: Array<string>) {
  const tiles = getTiles(lines);

  return tiles
    .filter((tile) => {
      return (
        tiles.filter((otherTile) => {
          if (tile.id === otherTile.id) return false;
          const otherEdges = Object.values(otherTile.edges).concat(
            Object.values(getReversedEdges(otherTile.edges)),
          );

          return (
            Object.values(tile.edges).filter((side: string) => {
              return (
                otherEdges.includes(side) ||
                otherEdges.includes(side.split("").reverse().join(""))
              );
            }).length > 0
          );
        }).length === 2
      );
    })
    .reduce((acc, tile) => acc * parseInt(tile.id), 1);
}

function handleInput_2(lines: Array<string>) {
  const tiles = getTiles(lines);

  const allTiles = [];

  tiles.forEach((tile) => {
    for (let f = 0; f < 2; f++) {
      for (let r = 0; r < 4; r++) {
        allTiles.push(tile);
        tile = rotateTile(tile);
      }
      tile = flipTile(tile);
    }
  });

  const gridSize = Math.sqrt(tiles.length);
  let grid: Array<Array<Tile>> = [];
  for (let a = 0; a < gridSize; a++) {
    grid.push([]);
    for (let b = 0; b < gridSize; b++) {
      grid[a].push(null);
    }
  }

  const searchGrid = (r: number, c: number, visited: Set<string>) => {
    if (r === gridSize) {
      return;
    }

    visited.forEach((v) => console.log(v));
    allTiles.forEach((tile: Tile) => {
      if (visited.has(tile.id)) {
        return;
      }

      if (c > 0 && !isMatchingRight(grid[r][c - 1], tile)) return;
      if (r > 0 && !isMatchingBottom(grid[r - 1][c], tile)) return;

      grid[r][c] = tile;
      const new_visited = new Set(visited);
      new_visited.add(tile.id);
      if (c === gridSize - 1) {
        searchGrid(r + 1, 0, new_visited);
      } else {
        searchGrid(r, c + 1, new_visited);
      }
    });
  };

  searchGrid(0, 0, new Set());

  console.log(grid);

  return 0;
}

export function handleInput(lines: Array<string>) {
  return [handleInput_1(lines), handleInput_2(lines)];
}
