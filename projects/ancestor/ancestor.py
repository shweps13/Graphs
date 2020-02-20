
from graph import Graph
from util import  Stack, Queue

"""

 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9

[(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

=> earliest_ancestor(ancestors, starting_node)
=>      child => separate input
=>      returns their earliest known ancestor – the one at the farthest distance 
=>      if there more there one ancestor => return lowest numeric ID
=>      if child without ancestor => return -1

Example input
  6

  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10


=> input is note None
=> no cycles in the input
=> ID >= 0
=> no repeat ancestor
=> one to many => parent to childrens

[child => strating_vertex]
[ancestor => destination_vertex]

"""

def earliest_ancestor(ancestors, starting_node):
    ancestorTree = Graph()

    #creating vertices first
    #if vertex already exist - nothing to do
    for ancestor in ancestors:
        for vert in ancestor:
            ancestorTree.add_vertex(vert)
    
    #adding edges to the tree
    for ancestor in ancestors:
        ancestorTree.add_edge(ancestor[1], ancestor[0])

    vertices = ancestorTree.vertices
    print(vertices)

    #result initial for last vertex in list
    result = None
    #lenght of path list
    biggest_path = 1

    #going thru each vertex in tree
    for vertex in vertices:
        #looking for path from starting vertex to iteratable vertex
        path = ancestorTree.dfs(starting_node, vertex)
        print(path)

        #as we looking for closer that's mean we need to check path
        if path is not None and len(path) > biggest_path:
                biggest_path = len(path)
                print("biggest_path", biggest_path)
                # last node is = to last node/vertice of the biggest_path
                result = vertex
                print("result", result)
        elif path is None and biggest_path == 1:
            result =(-1)


    return result

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(ancestors, 6))