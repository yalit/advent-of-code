export function arraySum(arr: Array<number>): number {
    return arr.reduce((s: number, n: number) => s + n, 0)
}

export const transpose = (matrix) => {
    let [row] = matrix
    return row.map((_, column) => matrix.map(row => row[column]))
}

export function intersection<T> (arrA: Array<T>, arrB: Array<T>): Array<T> {
    return arrA.filter((t: T) => arrB.includes(t))
}

export function removeElement<T>(arr: Array<T>, elem: T): Array<T> {
    return arr.filter(t => t !== elem)
}