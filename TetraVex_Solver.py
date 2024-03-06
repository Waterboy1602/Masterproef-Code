#!/usr/bin/env python3

def getPieces():
    # Get the pieces from the TetraVex game
    file = open("./dataFiles/TetraVex_3x3.txt", "r")
    north = []
    east = []
    south = []
    west = []
    pieces = []
    for line in file:
        sides = line.split(" ")
        pieces.append([int(sides[0]), int(sides[1]), int(sides[2]), int(sides[3])])
        # east.append([int(sides[1])])
        # south.append([int(sides[2])])
        # west.append([int(sides[3])])
    return pieces

# Check if the generated Tetravex is solvable
def isSolvable(solution, sizeBoard):
    solvable = True
    for i in range(0, sizeBoard):
        for j in range(0, sizeBoard):
            if (i < sizeBoard - 1 and solution[i][j][2] != solution[i + 1][j][0]) or \
                (j < sizeBoard - 1 and solution[i][j][3] != solution[i][j + 1][1]):
                solvable = False
                break 
    return solvable

def writeBoardToFile(grid, sizeGrid, dim):
    if(dim == 1):
        textFileName = "TetraVex_" + str(sizeGrid) + "x" + str(sizeGrid) + ".txt"
        textFile = open("./dataFiles/" + textFileName, "w")
        for i in range(0, sizeGrid * sizeGrid):
            textFile.write(str(grid[i][0]) + " " + str(grid[i][1]) + " " + str(grid[i][2]) + " " + str(grid[i][3]))
            textFile.write("\n")
    elif(dim == 2):
        textFileName = "TetraVex_" + str(sizeGrid) + "x" + str(sizeGrid) + "_FoundSolution.txt"
        textFile = open("./dataFiles/" + textFileName, "w")
        for i in range(0, sizeGrid):
            for j in range(0, sizeGrid):
                textFile.write(str(grid[i][j][0]) + " " + str(grid[i][j][1]) + " " + str(grid[i][j][2]) + " " + str(grid[i][j][3]))
                textFile.write("\n")
    textFile.close()


    




board = [
  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]],
  [[3, 4, 5, 6], [7, 8, 9, 0], [1, 2, 3, 4]],
  [[5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]],
]



##################################################################################
#########################         CHATGPT        #################################
##################################################################################


def build_graph(puzzle):
	size = len(puzzle)
	graph = [[0] * size for _ in range(size)]
	print(graph)
	# for i in range(size):
	# 	for j in range(size):
	# 		if i < size - 1 and puzzle[i][j].bottom == puzzle[i + 1][j].top:
	# 			graph[i * size + j][((i + 1) * size) + j] = 1
	# 			graph[((i + 1) * size) + j][i * size + j] = 1
	# 		if j < size - 1 and puzzle[i][j].right == puzzle[i][j + 1].left:
	# 			graph[i * size + j][i * size + (j + 1)] = 1
	# 			graph[i * size + (j + 1)][i * size + j] = 1
	print(graph)
	return graph


def is_safe(v, pos, path, graph):
    for i in range(pos):
        if graph[path[i]][v] == 1:
            return False
    return True

def max_clique_util(path, pos, max_size, size):
    if pos == size * size:
        return pos

    max_size = max(max_size, pos)

    for v in range(pos, size * size):
        if is_safe(v, pos, path):
            path[pos] = v
            max_size = max(max_size, max_clique_util(path, pos + 1, max_size))
            path[pos] = -1

    return max_size

def solve(puzzle):
    size = len(puzzle)
    path = [-1] * (size * size)
    max_clique_size = max_clique_util(path, 0, 0)
    return max_clique_size

if __name__ == '__main__':
    print("Start solving the Tetravex puzzle...")
    startBoard = getPieces()
    print(startBoard)
    graph = build_graph(startBoard)
    # solution = solver(startBoard, sizeBoard)
    # writeBoardToFile(solution, sizeBoard, 2)
    # "Found a solution"
    
##################################################################################
#########################       GOOGLE BARD      #################################
##################################################################################

# def convert_tetravex_to_graph(board):
#   """
#   Converts a Tetravex board to a graph representation.

#   Args:
#     board: A list of lists representing the Tetravex board, where each inner list
#            represents a row and each element is a list/tuple containing the four
#            values (one on each side) of the tile at that position.

#   Returns:
#     A dictionary representing the graph, where keys are tile positions (tuples) and
#     values are lists of adjacent positions.
#   """
#   graph = {}
#   rows, cols = len(board), len(board[0])
#   for row in range(rows):
#     for col in range(cols):
#       position = (row, col)
#       value = board[row][col]  # assuming board elements are lists/tuples now
#       adj_positions = []
#       # Check valid adjacent positions (up, down, left, right)
#       if row > 0:
#         adj_positions.append((row - 1, col))
#       if row < rows - 1:
#         adj_positions.append((row + 1, col))
#       if col > 0:
#         adj_positions.append((row, col - 1))
#       if col < cols - 1:
#         adj_positions.append((row, col + 1))
#       # Add edges to graph for tiles with matching values on adjacent sides
#       for adj_pos in adj_positions:
#         adj_value = board[adj_pos[0]][adj_pos[1]]
#         # Check if any of the four values on the current tile match
#         # any of the four values on the adjacent tile
#         if any(val in adj_value for val in value):
#           graph.setdefault(position, []).append(adj_pos)
#   return graph


# def is_clique(graph, vertices):
#   """
#   Checks if a given set of vertices forms a clique in the graph.

#   Args:
#     graph: A dictionary representing the graph, where keys are tile positions (tuples) and
#            values are lists of adjacent positions.
#     vertices: A set of vertices (tile positions) to check.

#   Returns:
#     True if the vertices form a clique, False otherwise.
#   """
#   for vertex in vertices:
#     for neighbor in graph[vertex]:
#       if neighbor not in vertices:
#         continue  # Skip non-adjacent neighbors
#       if not any(val in graph[neighbor] for val in graph[vertex]):
#         return False
#   return True

# def backtrack(graph, vertices, current_clique, max_clique):
#   """
#   Performs recursive backtracking to find the maximum clique.

#   Args:
#     graph: A dictionary representing the graph.
#     vertices: A set of remaining vertices to explore.
#     current_clique: The current clique found so far.
#     max_clique: The largest clique found yet.

#   Returns:
#     None. Modifies max_clique in-place.
#   """
#   if len(current_clique) > len(max_clique):
#     max_clique.clear()
#     max_clique.update(current_clique)

#   for vertex in vertices.copy():
#     vertices.remove(vertex)
#     current_clique.add(vertex)
#     if is_clique(graph, current_clique):
#       backtrack(graph.copy(), vertices.copy(), current_clique.copy(), max_clique)
#     current_clique.remove(vertex)
#     vertices.add(vertex)

# def find_max_clique(graph):
#   """
#   Finds the maximum clique in the given graph.

#   Args:
#     graph: A dictionary representing the graph.

#   Returns:
#     A set of vertices (tile positions) representing the maximum clique.
#   """
#   vertices = set(graph.keys())
#   current_clique = set()
#   max_clique = set()
#   backtrack(graph, vertices, current_clique, max_clique)
#   return max_clique

# max_clique = find_max_clique(graph)
# print(f"Maximum Clique: {max_clique}")
