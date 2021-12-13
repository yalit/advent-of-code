"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.handleInput = void 0;
function handleInput_1(lines) {
    let increase = 0;
    lines.forEach((element, k) => {
        increase += Number(k !== 0 && element > lines[k - 1]);
    });
    return increase;
}
function handleInput_2(lines) {
    let measurements = [];
    measurements = lines.reduce((acc, elem, k) => {
        if (k > lines.length - 3)
            return acc;
        acc.push(sumMeasures(lines.slice(k, k + 3).map(c => Number(c))));
        return acc;
    }, []);
    return handleInput_1(measurements);
}
function sumMeasures(measures) {
    return measures.reduce((acc, measure) => acc + measure, 0);
}
function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)];
}
exports.handleInput = handleInput;
