export function isInteger(value: string) {
  return !isNaN(parseInt(value, 10));
}

export function uint16 (n: number) {
  return n & 0xFFFF;
}