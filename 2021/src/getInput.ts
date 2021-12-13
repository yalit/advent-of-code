import { readFile } from 'fs'

export default function getInput(day: string){
    return new Promise((resolve, reject) => {
        readFile("../input/input_d"+day+".txt", "utf-8", (err, data) => {
            if (err) reject(err)
            resolve(data)
        })
    })
}