
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
    pass