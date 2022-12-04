export function arraySum(arr: Array<number>): number {
    return arr.reduce((s: number, n: number) => s + n, 0)
}