"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const readline_1 = require("readline");
const process_1 = require("process");
const getInput_js_1 = require("./getInput.js");
const readConsole = (0, readline_1.createInterface)({
    input: process_1.stdin,
    output: process_1.stdout
});
readConsole.question('Which day do you want to test ?', (day) => {
    let input = '';
    (0, getInput_js_1.default)(day)
        .then((data) => {
        input = data;
        return Promise.resolve().then(() => require("./handle_d" + String(day) + ".js"));
    }).then(({ handleInput }) => {
        console.log(handleInput(input.trim().split('\n')));
    })
        .catch(err => {
        console.error(err);
    });
    readConsole.close();
});
