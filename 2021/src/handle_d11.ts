function arrayHas(arr: Array<Array<number>>, needle: Array<number>): boolean {
    if (!needle) return false

    let found = false
    for (let i = 0; i < arr.length; i++) {
        if (arr[i][0] === needle[0] && arr[i][1] === needle[1]) found = true
    }

    return found
}

interface GridPoint {
    value: number, 
    flashed: boolean
}

function handleInput_1(lines: Array<string>){
    let grid: Array<Array<GridPoint>> = lines.map(line => line.split('').map(n => ({value: Number(n), flashed: false})))
    const height: number = grid.length
    const width: number = grid[0].length

    let flashers: number = 0
    let currentFlashers: Array<Array<number>> = []

    const increaseLevel = (y: number, x: number): void => {
        if (grid[y][x].value < 9) {
            grid[y][x].value++
        }
        else if (!grid[y][x].flashed && !arrayHas(currentFlashers, [y,x])) {
            currentFlashers.push([y,x])
        }
    }

    const flash = (y: number, x: number): void => {
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
            let n: Array<number> = currentFlashers.pop()
            flash(n[0], n[1])
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

function handleInput_2(lines: Array<string>){
    let grid = lines.map(line => line.split('').map(n => ({value: Number(n), flashed: false})))
    const height = grid.length
    const width = grid[0].length

    let flashers = 0
    let currentFlashers = []

    const increaseLevel = (y, x) => {
        if (grid[y][x].value < 9) {
            grid[y][x].value++
        }
        else if (!grid[y][x].flashed && !arrayHas(currentFlashers, [y,x])) {
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
            flash(n[0], n[1])
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


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}