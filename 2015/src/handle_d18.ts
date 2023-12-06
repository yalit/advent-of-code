import {displayMatrix, inMatrix, neighbors} from "../../ts/utils";

function handleInput_1(lines: Array<string>){
    let m = lines.map(l => l.replace('\r','').split(""))
    const h = m.length
    const w = m[0].length

    let i = 0
    while(i < 100) {
        let n = m.map(row => [...row])
        m.forEach((row, r) => {
            row.forEach((v, c) => {

                const nbLitNeighbors = neighbors.reduce((nb, [dr,dc]) => {
                    if (!inMatrix(r+dr,c+dc,w,h)) {
                        return nb
                    }

                    return m[r+dr][c+dc] == '#' ? nb + 1 : nb
                }, 0)
                if (m[r][c] === "#") {
                    n[r][c] = nbLitNeighbors === 2 || nbLitNeighbors === 3 ? '#' : '.'
                } else {
                    n[r][c] = nbLitNeighbors === 3 ? "#" : ":"
                }
            })
        })
        m = n.map(row => [...row])
        i += 1
    }

    return m.reduce((s, row) => row.filter((v) => v === "#").length + s, 0)
}

function handleInput_2(lines: Array<string>){
    let m = lines.map(l => l.replace('\r','').split(""))
    const h = m.length
    const w = m[0].length

    m[0][0] = '#'
    m[0][w-1] = '#'
    m[h-1][0] = '#'
    m[h-1][w-1] = '#'
    let i = 0
    while(i < 100) {

        let n = m.map(row => [...row])
        m.forEach((row, r) => {
            row.forEach((v, c) => {

                const nbLitNeighbors = neighbors.reduce((nb, [dr,dc]) => {
                    if (!inMatrix(r+dr,c+dc,w,h)) {
                        return nb
                    }

                    return m[r+dr][c+dc] === '#' ? nb + 1 : nb
                }, 0)
                if (m[r][c] === "#") {
                    if(nbLitNeighbors <2 || nbLitNeighbors >3) {
                        n[r][c] = "."
                    } else {
                        n[r][c] = "#"
                    }
                } else {
                    n[r][c] = nbLitNeighbors === 3 ? '#' : '.'
                }

            })
        })
        m = n.map(row => [...row])
        m[0][0] = '#'
        m[0][w-1] = '#'
        m[h-1][0] = '#'
        m[h-1][w-1] = '#'
        i += 1
    }


    return m.reduce((s, row) => row.filter((v) => v === "#").length + s, 0)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}