function handleInput_1(lines, nbSteps){
    let grid = new Grid(lines)
    let flashers = 0
    console.log(grid.values());
    grid.assignNeighbors()
    
    let i = 0
    while (i < nbSteps) {
        grid.increaseLevel(() => {
            flashers++
        })
        grid.resetLevelsAfterFlash()   
        i++
    }
    console.log(grid.values());

    return flashers
}

function handleInput_2(lines){
    return 0
}

function Octopus(level) {
    this.level = level
    this.neighbors = []
    this.currentAugmentation = 0
    this.flashed = false

    this.increaseLevel = (addFlasher) => {
        if (this.level === 9 && !this.flashed) {
            addFlasher(this)
            this.flashed = true
        } else if (this.level !== 9) {
            this.level++
            this.currentAugmentation++
        }
    }

    this.flashes = (addFlasher) => {
        this.neighbors.forEach(neighbor => neighbor.increaseLevel(addFlasher))
    }

    this.reset = () => {
        if (this.level - this.currentAugmentation === 9) this.level = 0
        this.currentAugmentation = 0
        this.flashed = false
    }
}

function Grid (data) {
    this.width = data[0].length
    this.octopuses = []
    this.currentFlashers = []

    //init octopuses
    data.forEach(row => {
        this.octopuses = this.octopuses.concat(row.split('').map((v) => new Octopus(Number(v))))
    })

    this.totalLength = this.octopuses.length
    
    this.addFlasher = (octopus) => {
        console.log("Adding Flasher");
        console.log(octopus);
        this.currentFlashers.push(octopus)
        console.log(this.currentFlashers);
    }

    this.assignNeighbors = () => {
        this.octopuses.forEach((octopus, index) => {
            octopus.neighbors = this.getNeighbors(index)
        })
    }

    this.increaseLevel = (increaseFlashers) => {
        this.octopuses.forEach((octopus) => {
            octopus.increaseLevel(this.addFlasher)
        })
        this.flashesAll(increaseFlashers)
    }

    this.flashesAll = (increaseFlashers) => {
        console.log("start flash all");
        while (this.currentFlashers.length > 0){
            let octopus = this.currentFlashers.pop()
            octopus.flashes(this.addFlasher)
            increaseFlashers()
        }
    }

    this.resetLevelsAfterFlash = () => {
        this.octopuses.forEach((octopus) => {
            octopus.reset()
        })
    }

    this.values = () => {
        let display = []
        for (let i = 0; i <= this.totalLength - this.width; i += this.width) {
            display.push(this.octopuses.slice(i, i + this.width).map(octopus => octopus.level))
        }

        return display
    }

    this.getNeighbors = (index) => {
        let neighbors = []
        //left
        if ((index % this.width) - 1 >= 0) neighbors.push(this.octopuses[index - 1])
        //right
        if ((index % this.width) + 1 < this.width) neighbors.push(this.octopuses[index + 1])
        //above
        if (index >= this.width) neighbors.push(this.octopuses[index - this.width])
        //down
        if (index + this.width < this.totalLength) neighbors.push(this.octopuses[index + this.width])

        //diagonals
        // above left
        if ((index % this.width) - 1 >= 0 && index >= this.width) neighbors.push(this.octopuses[index - 1 - this.width])
        //above right
        if ((index % this.width) + 1 < this.width && index >= this.width) neighbors.push(this.octopuses[index + 1 - this.width])
        //below left
        if ((index % this.width) - 1 >= 0 && index + this.width < this.totalLength) neighbors.push(this.octopuses[index - 1 + this.width])
        //below right
        if ((index % this.width) + 1 < this.width && index + this.width < this.totalLength) neighbors.push(this.octopuses[index + 1 + this.width])

        return neighbors
    }
}

export function handleInput(lines) {
    return [handleInput_1(lines, 1), handleInput_2(lines)]
}