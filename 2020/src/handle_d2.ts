interface TobogganPolicyVerif {
    first: number,
    second: number,
    pattern: string,
    password: string
}

function mapToTobogganPolicyVerif(line: string): TobogganPolicyVerif {
    const lineElements = line.match(new RegExp(/(?<first>[0-9]+)-(?<second>[0-9]+).(?<pattern>[a-z]+):.(?<password>[a-z]+)/))
    
    return {
        first: parseInt(lineElements.groups.first),
        second: parseInt(lineElements.groups.second),
        pattern: lineElements.groups.pattern,
        password: lineElements.groups.password
    }
}


function handleInput_1(lines: Array<TobogganPolicyVerif>): number {
    return lines.filter((l: TobogganPolicyVerif) => {
        const foundPatterns = l.password.match(new RegExp(l.pattern,'g')) || []
        return foundPatterns.length >= l.first && foundPatterns.length <= l.second
    }).length
}

function handleInput_2(lines: Array<TobogganPolicyVerif>): number{
    return lines.filter((l: TobogganPolicyVerif) => {
        return !(l.password.slice(l.first-1, l.first) === l.pattern) != !(l.password.slice(l.second-1, l.second) == l.pattern) //XOR implementation
    }).length

}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines.map(mapToTobogganPolicyVerif)), handleInput_2(lines.map(mapToTobogganPolicyVerif))]
}