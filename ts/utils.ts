/** @type {[number, number][]} */
export const directNeighbors = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
];
/** @type {[number, number][]} */
export const diagNeighbors = [
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1],
];
export const neighbors = [...diagNeighbors, ...directNeighbors];

/** @type {[number, number, number][]} */
export const neighbors3d = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, -1],
    [0, -1, 0],
    [-1, 0, 0],
];

export const digits = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
};

export function inMatrix(r: number,c: number,width: number,height: number): boolean {
    return r >= 0 && r < height && c >= 0 && c < width
}

export function displayMatrix(m: (number|string)[][]): void {
    m.forEach(row => console.log(row.join('')))
}