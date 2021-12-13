"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.handleInput = void 0;
function handleInput_1(lines) {
    let gamma;
    let epsilon;
    let mapped = [];
    lines.forEach((line, k) => {
        if (k === 0) {
            mapped = line.split('').map(d => [d]);
            return;
        }
        line.split('').forEach((element, k) => {
            mapped[k].push(element);
        });
    });
    gamma = parseInt(mapped.map(elems => findMostCommonBit(elems)).join(''), 2);
    epsilon = parseInt(mapped.map(elems => findLeastCommonBit(elems)).join(''), 2);
    return gamma * epsilon;
}
function handleInput_2(lines) {
    let oxygen = lines, co2 = lines;
    let n = 0;
    while (oxygen.length > 1 && n < lines[0].length) {
        let bits = getNthBitsFromElements(oxygen, n);
        oxygen = rating(oxygen, n, findMostCommonBit(bits));
        n++;
    }
    let oxygenLevel = parseInt(oxygen[0], 2);
    n = 0;
    while (co2.length > 1 && n < lines[0].length) {
        let bits = getNthBitsFromElements(co2, n);
        co2 = rating(co2, n, findLeastCommonBit(bits));
        n++;
    }
    let co2Level = parseInt(co2[0], 2);
    return oxygenLevel * co2Level;
}
function rating(elements, bitPosition, value) {
    return elements.filter(elem => elem.split('')[bitPosition] === value);
}
function getNthBitsFromElements(elements, n) {
    return elements.map(elem => elem.split('')[n]);
}
function findMostCommonBit(elements) {
    let common = 0;
    elements.forEach(element => {
        if (element === '0')
            common -= 1;
        else if (element === '1')
            common += 1;
    });
    return (common >= 0) ? '1' : '0';
}
function findLeastCommonBit(elements) {
    let common = 0;
    elements.forEach(element => {
        if (element === '0')
            common += 1;
        else if (element === '1')
            common -= 1;
    });
    return (common > 0) ? '1' : '0';
}
function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)];
}
exports.handleInput = handleInput;
