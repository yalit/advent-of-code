import {createInterface} from 'readline'
import {stdin, stdout} from 'process'
import getInput from './getInput.js'

const readConsole = createInterface({
    input: stdin,
    output: stdout
})

readConsole.question('Which day do you want to test ?', (day: string) => {
    let input:string  = ''
    getInput(day)
        .then((data: string) => {
            input = data
            return import("./handle_d"+String(day)+".js")
        }).then(({handleInput}) => {
            console.log(handleInput(input.trim().split('\n').map(line => line.replace(/\r/g, ''))))
        })
        .catch(err => {
            console.error(err)
        })
    readConsole.close()
})