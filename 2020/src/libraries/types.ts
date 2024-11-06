export function isText(value: any): value is string {
    return typeof value === 'string' && isNaN(parseInt(value))
}