/**
 * Tiles need to be ordered
 * Each tile has neighbors
 * the outer edges of the pattern are unique
 */
import { flipStringArray, rotateStringArray } from "./libraries/array";

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
  const newLines = rotateStringArray(tile.lines);
  return {
    id: tile.id,
    lines: newLines,
    edges: getEdges(newLines),
  };
};

const nextRotatedEdge = (e: EdgeSide): EdgeSide => {
  const n: { [k in EdgeSide]: EdgeSide } = {
    top: "left",
    right: "top",
    bottom: "right",
    left: "bottom",
  };
  return n[e];
};

const flipTile = (tile: Tile): Tile => {
  const newLines = flipStringArray(tile.lines);
  return {
    id: tile.id,
    lines: newLines,
    edges: getEdges(newLines),
  };
};

const allPossibleTransformations = (tile: Tile): Array<Tile> => {
  const flipped = flipTile(tile);
  return [
    tile,
    rotateTile(tile),
    rotateTile(rotateTile(tile)),
    rotateTile(rotateTile(rotateTile(tile))),
    flipped,
    rotateTile(flipped),
    rotateTile(rotateTile(flipped)),
    rotateTile(rotateTile(rotateTile(flipped))),
  ];
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

const findMatchingEdges = (tiles: Array<Tile>, tile: Tile): Set<EdgeSide> => {
  let matching: Set<EdgeSide> = new Set();

  for (let j in tiles) {
    const otherTile = tiles[j];

    if (tile.id === otherTile.id) {
      continue;
    }
    Object.entries(tile.edges).forEach(([e, edge]: [EdgeSide, string]) => {
      if (Object.values(otherTile.edges).includes(edge)) {
        matching.add(e);
      }
      if (Object.values(getReversedEdges(otherTile.edges)).includes(edge)) {
        matching.add(e);
      }
    });
  }

  return matching;
};

const getTopLeft = (tiles: Array<Tile>): Tile => {
  for (let i in tiles) {
    let tile = tiles[i];

    const matching = findMatchingEdges(tiles, tile);

    if (matching.size === 2) {
      let m: [EdgeSide, EdgeSide] = Array.from(matching).sort() as [
        EdgeSide,
        EdgeSide,
      ];

      while (!(m[0] === "bottom" && m[1] === "right")) {
        tile = rotateTile(tile);
        m = [nextRotatedEdge(m[0]), nextRotatedEdge(m[1])].sort() as [
          EdgeSide,
          EdgeSide,
        ];
      }
      return tile;
    }
  }
};

// inspired by Anthonywritescode : https://github.com/anthonywritescode/aoc2020/blob/master/day20/part2.py
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

  let connections = { 2: [], 3: [], 4: [] };

  tiles.forEach((tile) => {
    connections[findMatchingEdges(tiles, tile).size].push(tile);
  });

  const gridSize = Math.sqrt(tiles.length);
  let grid: Array<Array<Tile>> = [];

  const topLeft = getTopLeft(tiles);
  const placed = new Set();
  for (let i = 0; i < gridSize; i++) {
    let row: Array<Tile> = [];

    // get first piece of line
    let targetConnections = i === 0 || i === gridSize - 1 ? 2 : 3;
    if (i === 0) {
      row.push(topLeft);
      placed.add(topLeft.id);
    } else {
      const targetEdge = grid[i - 1][0].edges.bottom;
      for (let t in connections[targetConnections]) {
        const borderTile = connections[targetConnections][t];

        if (placed.has(borderTile.id)) {
          continue;
        }

        if (
          Object.values(borderTile.edges).includes(targetEdge) ||
          Object.values(getReversedEdges(borderTile.edges)).includes(targetEdge)
        ) {
          const possibilites = allPossibleTransformations(borderTile);
          for (let p in possibilites) {
            const transformedBorderTile = possibilites[p];
            if (targetEdge === transformedBorderTile.edges.top) {
              row.push(transformedBorderTile);
              placed.add(transformedBorderTile.id);
              break;
            }
          }
        }
      }
    }

    // find row
    for (let j = 1; j < gridSize; j++) {
      targetConnections =
        i === 0 || i === gridSize - 1
          ? j === gridSize - 1
            ? 2
            : 3
          : j == gridSize - 1
            ? 3
            : 4;

      const targetEdge = row[j - 1].edges.right;
      for (let t in connections[targetConnections]) {
        const nextTile = connections[targetConnections][t];

        if (placed.has(nextTile.id)) {
          continue;
        }

        if (
          Object.values(nextTile.edges).includes(targetEdge) ||
          Object.values(getReversedEdges(nextTile.edges)).includes(targetEdge)
        ) {
          const possibilites = allPossibleTransformations(nextTile);
          for (let p in possibilites) {
            const transformedBorderTile = possibilites[p];
            if (targetEdge === transformedBorderTile.edges.left) {
              row.push(transformedBorderTile);
              placed.add(transformedBorderTile.id);
              break;
            }
          }
        }
      }
    }

    grid.push(row);
  }

  let innerGrid = [];
  let totalCountElements = 0;
  const seaMonster = [
    [1, -18],
    [1, -13],
    [1, -12],
    [1, -7],
    [1, -6],
    [1, -1],
    [1, 0],
    [1, 1],
    [2, -17],
    [2, -14],
    [2, -11],
    [2, -8],
    [2, -5],
    [2, -2],
  ];

  const tileSize = grid[0][0].lines.length;
  grid.forEach((row) => {
    for (let i = 1; i < tileSize - 1; i++) {
      let innerRow = "";
      row.forEach((t) => {
        const content = t.lines[i].slice(1, tileSize - 1);
        innerRow += content;
        totalCountElements += Array.from(content).filter(
          (c) => c === "#",
        ).length;
      });
      innerGrid.push(innerRow);
    }
  });

  const findNbMonsters = (g: Array<string>): number => {
    let nb = 0;
    for (let r = 0; r < g.length - 3; r++) {
      for (let c = 18; c < g[0].length - 2; c++) {
        if (g[r][c] !== "#") {
          continue;
        }
        const isAMonster =
          seaMonster.filter(([dr, dc]) => g[r + dr][c + dc] === "#").length ===
          seaMonster.length;

        nb += isAMonster ? 1 : 0;
      }
    }
    return nb;
  };

  const flippedInnerGrid = flipStringArray(innerGrid);
  const allPossibleInnerGrids = [
    innerGrid,
    rotateStringArray(innerGrid),
    rotateStringArray(rotateStringArray(innerGrid)),
    rotateStringArray(rotateStringArray(rotateStringArray(innerGrid))),
    flippedInnerGrid,
    rotateStringArray(flippedInnerGrid),
    rotateStringArray(rotateStringArray(flippedInnerGrid)),
    rotateStringArray(rotateStringArray(rotateStringArray(flippedInnerGrid))),
  ];

  for (let i in allPossibleInnerGrids) {
    const g = allPossibleInnerGrids[i];

    const nbMonsters = findNbMonsters(g);

    if (nbMonsters > 0) {
      return totalCountElements - nbMonsters * (seaMonster.length + 1);
    }
  }

  return "Not found";
}

export function handleInput(lines: Array<string>) {
  return [handleInput_1(lines), handleInput_2(lines)];
}
