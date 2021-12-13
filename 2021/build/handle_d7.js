"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.handleInput = void 0;
const lodash_1 = require("lodash");
function handleInput_1(lines) {
    const numbers = lines[0].split(',').map(a => Number(a)).sort((a, b) => a - b);
    const ground = getMedian(numbers);
    return getSimpleCostNumbers(numbers, ground);
}
function handleInput_2(lines) {
    const numbers = lines[0].split(',').map(a => Number(a)).sort((a, b) => a - b);
    //use of mass center
    const ground = getCenterOfMass(numbers);
    return getAccumulativeCostNnumber(numbers, ground);
}
function getPointsMasses(numbers) {
    const masses = {};
    numbers.forEach((d) => {
        masses[d] = masses[d] ? masses[d] + 1 : 1;
    });
    return masses; //number of points at a position x
}
function getMedian(numbers) {
    return numbers[Math.round(numbers.length / 2)];
}
function getCenterOfMass(numbers) {
    const masses = getPointsMasses(numbers);
    const ponderedMass = Object.keys(masses).reduce((a, x) => a + (Number(x) * masses[x]), 0);
    return Math.floor(ponderedMass / numbers.length);
}
function getSimpleCostNumbers(numbers, ground) {
    numbers = numbers.map(n => Math.abs(ground - n));
    return lodash_1._.sum(numbers);
}
function getAccumulativeCostNnumber(numbers, ground) {
    numbers = numbers.map(n => getNSum(Math.abs(ground - n)));
    return lodash_1._.sum(numbers);
}
function getNSum(n) {
    return lodash_1._.sum(lodash_1._.range(1, n + 1));
}
function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)];
}
exports.handleInput = handleInput;
