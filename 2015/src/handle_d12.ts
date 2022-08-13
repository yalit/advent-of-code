import { type } from "os";
import { off } from "process";
import { isInteger } from "./helpers";

function getNumbers(s: string): Array<number> {
    return (s.match(/(-?\d+)/g)??[]).map(n => parseInt(n))
}

function handleInput_1(s: string): number{
    return getNumbers(s).reduce((ts, n) => ts+n,0)
}

function parseRecursive(o: {} | [] | string | number) : number {
    if (typeof(o) === 'number') {
        return o
    }
    
    if (typeof(o) === 'string') {
        return (isInteger(o))?parseInt(o):0
    }

    if (Array.isArray(o)) {
        return o.map(n => parseRecursive(n)).reduce((s,a) => s+a,0)
    }

    if (Object.values(o).indexOf('red') >= 0) {
        return 0
    }

    return Object.values(o).map(n => parseRecursive(n)).reduce((s,a) => s+a,0)
    
}

function handleInput_2(s: string) : number{
    const json = JSON.parse(s);
    
    return parseRecursive(json)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines[0]), handleInput_2(lines[0])]
}