import {createInterface} from 'readline'
import {stdin, stdout} from 'process'
import getInput from './getInput.js'

const readConsole = createInterface({
    input: stdin,
    output: stdout
})

readConsole.question('Which day do you want to test ?', day => {
    let input = ''
    getInput(day)
        .catch(console.log)
        .then(data => {
            input = data
            return import("./handle_d"+String(day)+".js")
        }).then(({handleInput}) => {
            console.log(handleInput(input.trim().split('\n')))
        })
    readConsole.close()
})