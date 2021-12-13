"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = require("fs");
function getInput(day) {
    return new Promise((resolve, reject) => {
        (0, fs_1.readFile)("../input/input_d" + day + ".txt", "utf-8", (err, data) => {
            if (err)
                reject(err);
            resolve(data);
        });
    });
}
exports.default = getInput;
