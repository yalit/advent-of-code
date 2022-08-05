import { getMatrixBorders, Matrix, matrixMap } from "./matrix";

type Image = Matrix

let algorithm: Array<string>;
let image: Image


function handleInput_1(lines: Array<string>){
    return runAlgorithm(2, lines)
}

function handleInput_2(lines: Array<string>){
    return runAlgorithm(50, lines)
}

function runAlgorithm(times: number, lines: Array<string>): number {
    setAlgorithmAndImage(lines)
    addInfinityAroundImage('0')

    for (let n = 0; n < times; n++) {
        image = matrixMap(image, (value, x, y, matrix) => {
            let pixels = getCombinedPixels(x, y)
            return algorithm[getPositionValue(pixels)]
        })
    }

    return image.reduce((total: number, line: Array<string>) => {
        return total + line.reduce((s:number, pixel:string) => {
            return s + parseInt(pixel)
        }, 0)
    }, 0)
}

function getCombinedPixels(x: number, y: number): string {
    let pixels = ''

    for (let a = -1; a <= 1; a++) {
        if (y + a < 0 || y + a >= image.length) {
            pixels += getSurroundingPixelsFromRow(Array(image[0].length).fill(image[0][0]), x, image[0][0]).join('')    
        } else {
            pixels += getSurroundingPixelsFromRow(image[y + a], x, image[0][0]).join('')
        }
    }

    return pixels
}

function getSurroundingPixelsFromRow(row: Array<string>, position: number, defaultValue: string): Array<string> {
    if (position === 0 ) {
        return [defaultValue].concat(row.slice(position, position+2))
    } else if (position === row.length - 1) {
        return row.slice(position-1, position+1).concat([defaultValue])
    } else {
        return row.slice(position-1, position+2)
    }   
}

function getPositionValue(s: string): number {
    return parseInt(s, 2)
}

function setAlgorithmAndImage(lines: Array<string>): void {
    algorithm = lines[0].replace(/#/g, '1').replace(/\./g,'0').split('')
    image = lines.slice(2,lines.length).map(line => line.replace(/#/g, '1').replace(/\./g,'0').split(''))
}

function addInfinityAroundImage(defaultValue: string): void {
    const borderValues = getMatrixBorders(image)

    //add infinite void around image
    const nbToAdd = 100
    const valueToAdd = (defaultValue === undefined) ? image[0][0] : defaultValue
    const additionalLines = Array(nbToAdd).fill(Array(image[0].length + (nbToAdd * 2)).fill(valueToAdd))
    const additionalBorder = Array(nbToAdd).fill(valueToAdd)

    image = image.map(imageLine => additionalBorder.concat(imageLine).concat(additionalBorder))
    image = additionalLines.concat(image).concat(additionalLines)
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}