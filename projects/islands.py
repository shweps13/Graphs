class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def island_counter(matrix):
    # Create a visited matrix of the same dimensions as the given matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    # Walk through each cel of the matrix
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
          # Count up the connected components
          # If it has not been visited...
          if not visited[row][col]:
              # When I reach a 1...
              if matrix[row][col] == 1:
                  # Do a DFT and mark each 1 as visited
                  visited = dft(col, row, matrix, visited)
                  # Increment the counter by 1
                  island_count += 1
              else:
                  visited[row][col] = True
    return island_count


def dft(col, row, matrix, visited):
    '''
    This will mark each connect component as visited

    Return visited matrix
    '''
    # Create an empty stack
    s = Stack()
    # Push starting node onto the stack
    s.push( (col, row) )
    # While stack is not empty
    while s.size() > 0:
        # Pop vertex from top of the stack
        v = s.pop()
        col = v[0]
        row = v[1]
        # Check if it's visited. If not...
        if not visited[row][col]:
            # Mark it as visited
            visited[row][col] = True
            # Push each neighbor onto the top of the stack
            for neighbor in get_neighbors((col, row), matrix):  # STUB
                s.push(neighbor)
    return visited


def get_neighbors(vertex, graph_matrix):
    col = vertex[0]
    row = vertex[1]
    neighbors = []
    # Check north
    if row > 0 and graph_matrix[row-1][col] == 1:
        neighbors.append((col, row-1))
    # Check south
    if row < len(graph_matrix) - 1 and graph_matrix[row+1][col] == 1:
        neighbors.append((col, row+1))
    # Check east
    if col < len(graph_matrix[0]) - 1 and graph_matrix[row][col+1] == 1:
        neighbors.append((col+1, row))
    # Check west
    if col > 0 and graph_matrix[row][col-1] == 1:
        neighbors.append((col-1, row))
    # Return all directions that contain a 1
    return neighbors



islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]


islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))