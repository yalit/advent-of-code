export function arraySum(arr: Array<number>): number {
  return arr.reduce((s: number, n: number) => s + n, 0);
}

export const transpose = (matrix) => {
  let [row] = matrix;
  return row.map((_, column) => matrix.map((row) => row[column]));
};

export function intersection<T>(arrA: Array<T>, arrB: Array<T>): Array<T> {
  return arrA.filter((t: T) => arrB.includes(t));
}

export function removeElement<T>(arr: Array<T>, elem: T): Array<T> {
  return arr.filter((t) => t !== elem);
}

export function rotateStringArray(a: Array<string>): Array<string> {
  let newArray = [];

  for (let i = a[0].length - 1; i >= 0; i--) {
    newArray.push(a.map((r) => r[i]).join(""));
  }

  return newArray;
}

export function flipStringArray(a: Array<string>): Array<string> {
  return a.map((r) => r.split("").reverse().join(""));
}
