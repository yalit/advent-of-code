"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.handleInput = void 0;
function handleInput_1(lines) {
    let x = 0, y = 0;
    const actions = {
        forward: (dist) => x += dist,
        down: (dist) => y += dist,
        up: (dist) => y -= dist
    };
    lines.forEach(element => {
        const [action, dist] = element.split(" ");
        actions[action](Number(dist));
    });
    return x * y;
}
function handleInput_2(lines) {
    let x = 0, y = 0, aim = 0;
    const actions = {
        forward: (dist) => {
            x += dist;
            y += (aim * dist);
        },
        down: (dist) => aim += dist,
        up: (dist) => aim -= dist
    };
    lines.forEach(element => {
        const [action, dist] = element.split(" ");
        actions[action](Number(dist));
    });
    return x * y;
}
function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)];
}
exports.handleInput = handleInput;
