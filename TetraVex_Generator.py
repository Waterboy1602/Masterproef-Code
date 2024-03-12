#!/usr/bin/env python3

import random
import numpy as np

# Generate pieces
def generatePieces(sizeGrid):
    grid = []
    for i in range(0, sizeGrid):
        row = []
        for j in range(0, sizeGrid):
            piece = []
            piece.extend(random.randint(0, 9) for _ in range(4))
            if (j > 0):
                piece[3] = row[j - 1][1]
            if (i > 0): 
                piece[0] = grid[i - 1][j][2]
            row.append(piece)  
        grid.append(row)
    return grid

def shufflePieces(grid, sizeGrid):
    grid1D = []
    for i in range(0, sizeGrid):
        for j in range(0, sizeGrid):
            grid1D.append(grid[i][j])
    random.shuffle(grid1D) 
    return grid1D

# Write the board to txt-file
def writeBoardToFile(grid, sizeGrid, dim):
    if(dim == 1):
        textFileName = "TetraVex_" + str(sizeGrid) + "x" + str(sizeGrid) + ".txt"
        textFile = open("./dataFiles/" + textFileName, "w")
        for i in range(0, sizeGrid * sizeGrid):
            textFile.write(str(grid[i][0]) + " " + str(grid[i][1]) + " " + str(grid[i][2]) + " " + str(grid[i][3]))
            textFile.write("\n")
    elif(dim == 2):
        textFileName = "TetraVex_" + str(sizeGrid) + "x" + str(sizeGrid) + "_Solution.txt"
        textFile = open("./dataFiles/" + textFileName, "w")
        for i in range(0, sizeGrid):
            for j in range(0, sizeGrid):
                textFile.write(str(grid[i][j][0]) + " " + str(grid[i][j][1]) + " " + str(grid[i][j][2]) + " " + str(grid[i][j][3]))
                textFile.write("\n")
    textFile.close()


def generateSolvableBoard(sizeGrid):
    grid = generatePieces(sizeGrid)
    writeBoardToFile(grid, sizeGrid, 2)
    grid1D = shufflePieces(grid, sizeGrid)
    writeBoardToFile(grid1D, sizeGrid, 1)
    print("Generated a board of size " + str(sizeGrid) + "x" + str(sizeGrid) + " and wrote it to a file.")
    
if __name__ == '__main__':
    sizeGrid = 2
    generateSolvableBoard(sizeGrid)
