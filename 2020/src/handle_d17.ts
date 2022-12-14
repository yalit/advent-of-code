import { getEnvironmentData } from "worker_threads";

const coord = (x, y, z) => {
    return `${x},${y},${z}`;
}
    

const neighbors = (x, y, z) => {
    let n = [];
    [-1,0,1].forEach(dx => {
        [-1,0,1].forEach(dy => {
            [-1,0,1].forEach(dz => {
                if (dx === 0 && dy === 0 && dz === 0) {
                    return
                }
                n.push(coord(x+dx, y+dy, z+dz))
            })
        })  
    })

    return n 
}

function handleInput_1(lines: Array<string>){
    let grid = {
        x: {min: 0, max: lines[0].length - 1},
        y: {min: 0, max: lines.length - 1},
        z: {min: 0, max: 0},
    }
    let activeCubes = new Set()
    
    lines.forEach((line, y) => {
        line.split('').forEach((e, x) => {
            if (e === '#'){
                activeCubes.add(coord(x, y, 0))
            }
        })
    })
    console.log(grid);
    
    for (let i = 0; i < 6; i++) {
        let newGrid = {...grid}
        let newActiveCubes = new Set(activeCubes)
        for (let x = grid.x.min - 1; x <= grid.x.max + 1; x++) {    
            for (let y = grid.y.min - 1; y <= grid.y.max + 1; y++) {    
                for (let z = grid.z.min - 1; z <= grid.z.max + 1; z++) {    
                    const nbNeighbors = neighbors(x, y, z).filter(c => {
                        return activeCubes.has(c)
                    }).length
                    if (activeCubes.has(coord(x,y,z)) && !(nbNeighbors === 2 || nbNeighbors === 3)) {
                        newActiveCubes.delete(coord(x,y,z))
                    }
                    if (!activeCubes.has(coord(x,y,z)) && nbNeighbors === 3) {
                        newActiveCubes.add(coord(x,y,z))
                        if (x < grid.x.min) {
                            newGrid.x.min = grid.x.min - 1
                        }
                        if (x > grid.x.max) {
                            newGrid.x.max = grid.x.max + 1
                        }
                        if (y < grid.y.min) {
                            newGrid.x.min = grid.y.min - 1
                        }
                        if (y > grid.y.max) {
                            newGrid.y.max = grid.y.max + 1
                        }
                        if (z < grid.z.min) {
                            newGrid.z.min = grid.z.min - 1
                        }
                        if (z > grid.z.max) {
                            newGrid.z.max = grid.z.max + 1
                        }
                    }
                }
            }   
        }
        grid = {...newGrid}
        activeCubes = new Set(newActiveCubes)
        console.log(`Cycle ${i + 1} : active Cubes = ${activeCubes.size}`);
        
    }
    
    return activeCubes.size
}

function handleInput_2(lines: Array<string>){      
    return 0
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}