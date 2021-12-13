"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.handleInput = void 0;
const lodash_1 = require("lodash");
const newBornDays = 8;
const resetDays = 6;
function handleInput_1(line, nbDays = 80) {
    let population = setUpPopulation(line[0].split(','));
    let nbRemainingDays = nbDays;
    while (nbRemainingDays > 0) {
        population = getNewPopulationAfterANight(population);
        nbRemainingDays--;
    }
    return getPopulationSize(population);
}
function getZeroedPopulation() {
    let elems = {};
    lodash_1._.range(0, newBornDays + 1).forEach((n) => elems[n] = 0);
    return elems;
}
function setUpPopulation(elements) {
    let elems = getZeroedPopulation();
    elements.forEach((e) => elems[Number(e)] += 1);
    return elems;
}
function getPopulationSize(population) {
    return Object.values(population).reduce((s, n) => s + n, 0);
}
function getNewPopulationAfterANight(population) {
    const newPopulation = getZeroedPopulation();
    Object.keys(population).forEach(d => {
        const n = Number(d);
        if (n === 0) {
            newPopulation[resetDays] = population[0];
            newPopulation[newBornDays] = population[0];
        }
        else {
            newPopulation[n - 1] += population[n];
        }
    });
    return newPopulation;
}
function handleInput(line) {
    return [handleInput_1(line), handleInput_1(line, 256)];
}
exports.handleInput = handleInput;
