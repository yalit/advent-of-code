import { parse } from "path"

interface ValidNorthPoleCredentials {
    ecl: string,
    pid: string,
    eyr: string, 
    hcl: string,
    byr: string,
    iyr: string,
    hgt: string
}

function isValidNorthPoleCredentials(elem: any): boolean {
    return 'ecl' in elem
        && 'pid' in elem
        && 'eyr' in elem
        && 'hcl' in elem
        && 'byr' in elem
        && 'iyr' in elem
        && 'hgt' in elem
}

function isExtendedValidNorthPoleCredentials(elem: any): boolean {
    if (!isValidNorthPoleCredentials(elem)) {
        return false
    }
    const height = elem.hgt.match(/^(?<value>[0-9]+)(?<unit>cm|in)$/)
    return ['amb', 'blu', 'brn', 'gry','grn', 'hzl', 'oth'].includes(elem.ecl)
        && parseInt(elem.byr) >= 1920 && parseInt(elem.byr) <= 2002
        && parseInt(elem.iyr) >= 2010 && parseInt(elem.iyr) <= 2020
        && parseInt(elem.eyr) >= 2020 && parseInt(elem.eyr) <= 2030
        && height !== null 
        && (height.groups.unit === 'cm' 
            ? parseInt(height.groups.value) >= 150 && parseInt(height.groups.value) <= 193
            : parseInt(height.groups.value) >= 59 && parseInt(height.groups.value) <= 76
            )
        && elem.hcl.match(/^#[0-9a-f]{6}$/) !== null
        && elem.pid.match(/^[0-9]{9}$/) !== null
}

function extractDataFromLine(line: string): Partial<ValidNorthPoleCredentials> {
    let data = {}
    line.trim().split(' ').map(l => {
        return l.split(':')
    }).forEach(([t, d]) =>{
        return data[t] = d
    })
    return data
}

function handleInput_1(lines: Array<string>){
    return lines.filter(line => isValidNorthPoleCredentials(extractDataFromLine(line))).length
}

function handleInput_2(lines: Array<string>){
    return lines.filter(line => isExtendedValidNorthPoleCredentials(extractDataFromLine(line))).length
}

export function handleInput(lines: Array<string>) {
    lines = lines.join(' ').split('  ')
    return [handleInput_1(lines), handleInput_2(lines)]
}