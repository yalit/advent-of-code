Array.prototype.has = function(arr) {
    if (!arr) return false

    let found = false
    for (let i = 0; i < this.length; i++) {
        if (this[i][0] === arr[0] && this[i][1] === arr[1]) found = true
    }

    return found
}

function handleInput_1(lines){
    let grid = lines.map(line => line.split('').map(n => ({value: Number(n), flashed: false})))
    const height = grid.length
    const width = grid[0].length

    let flashers = 0
    let currentFlashers = []

    const increaseLevel = (y, x) => {
        if (grid[y][x].value < 9) {
            grid[y][x].value++
        }
        else if (!grid[y][x].flashed && !currentFlashers.has([y,x])) {
            currentFlashers.push([y,x])
        }
    }

    const flash = (y, x) => {
        if (grid[y][x].flashed) return

        grid[y][x].flashed = true
        for (let a = -1; a <= 1; a++) {
            for (let b = -1; b <= 1; b++) {
                if ((x+b) >= 0 && (x+b) < width && (y+a) >=0 && (y+a) < height) {
                    increaseLevel(y+a, x+b)
                }
            }
        }
    }

    const shouldStillFlash = () => {
        return Array.from(currentFlashers).length > 0
    }

    let i = 0

    while (i < 100) {
        //increase all by 1
        for (let y = 0; y < grid.length; y++) {
            for (let x = 0; x < grid[y].length; x++) {
                increaseLevel(y, x)
            }
        }

        while (shouldStillFlash()) {
            let n = currentFlashers.pop()
            flash(...n)
            flashers++
        }

        for (let y = 0; y < grid.length; y++) {
            for (let x = 0; x < grid[y].length; x++) {
                if (grid[y][x].flashed) {
                    grid[y][x].flashed = false
                    grid[y][x].value = 0
                }
            }
        }
        i++
    }
    
    return flashers
}

function handleInput_2(lines){
    let grid = lines.map(line => line.split('').map(n => ({value: Number(n), flashed: false})))
    const height = grid.length
    const width = grid[0].length

    let flashers = 0
    let currentFlashers = []

    const increaseLevel = (y, x) => {
        if (grid[y][x].value < 9) {
            grid[y][x].value++
        }
        else if (!grid[y][x].flashed && !currentFlashers.has([y,x])) {
            currentFlashers.push([y,x])
        }
    }

    const flash = (y, x) => {
        if (grid[y][x].flashed) return

        grid[y][x].flashed = true
        for (let a = -1; a <= 1; a++) {
            for (let b = -1; b <= 1; b++) {
                if ((x+b) >= 0 && (x+b) < width && (y+a) >=0 && (y+a) < height) {
                    increaseLevel(y+a, x+b)
                }
            }
        }
    }

    const shouldStillFlash = () => {
        return Array.from(currentFlashers).length > 0
    }

    let i = 0
    let isSynchronized = false
    while (!isSynchronized) {
        let flashInTurn = 0
        //increase all by 1
        for (let y = 0; y < grid.length; y++) {
            for (let x = 0; x < grid[y].length; x++) {
                increaseLevel(y, x)
            }
        }

        while (shouldStillFlash()) {
            let n = currentFlashers.pop()
            flash(...n)
            flashers++
            flashInTurn++
        }

        for (let y = 0; y < grid.length; y++) {
            for (let x = 0; x < grid[y].length; x++) {
                if (grid[y][x].flashed) {
                    grid[y][x].flashed = false
                    grid[y][x].value = 0
                }
            }
        }

        if (flashInTurn === width*height) isSynchronized = true
        i++
    }
    
    return i
}


export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}