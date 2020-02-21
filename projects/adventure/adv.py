from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
import copy
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print("\nStarting room is: ", world.starting_room)
print("-------------------\n")

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_dict = {}
local_graph = {}

"""
From start room [0]:
{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}

to south point [5]:
{
  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': '?', 'e': '?'}
}
"""

def bfs(starting_room):
    # Create an empty queue
    q = Queue()
    # Add A PATH TO the starting vertex_id to the queue
    q.enqueue([starting_room])
    # Create an empty set to store visited nodes
    visited = set()
    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue, the first PATH
        path = q.dequeue()
        # print(path)
        # GRAB THE LAST VERTEX FROM THE PATH
        current_room = path[-1]
        # print("current_room", current_room) 
        visited.add(current_room)
        # If it has not been visited...
        # if path[-1] not in visited:
        #     # Mark it as visited
        #     visited[current_room] = path
            # print(visited)
            # Then add A PATH TO all neighbors to the back of the queue
                # (Make a copy of the path before adding)
        for direction in local_graph[current_room]:
            print("local path", local_graph[current_room])
            if local_graph[current_room][direction] == "?":
                # return available paths
                return path
            elif local_graph[current_room][direction] not in visited:
                # create new path to append direction
                new_path = list(path)
                new_path.append(local_graph[current_room][direction])
                q.enqueue(new_path)
                print("append direction: ", new_path)


# Player doing [dft]:
    # search for directions
    # evaluate for and "?"
    # if there are exits with "?"
    # keep track of them
    # randomly pick
    # move there
    # log to traversal


def search(starting_room):
    print("===Beginning of search===\n")
    visited_room = set()

    # Where player now
    current_room = player.current_room
    
    # Id of current room
    room_id = current_room.id

    # Define opposite directions
    global_directions = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

    # Define dictionary with room directions
    room_dict = {}

    while len(local_graph) != len(room_graph):
        # print("current room:", room_id)

        if room_id not in local_graph:
            # Find possible exits

            for i in current_room.get_exits():
                room_dict[i] = '?'
                # print("room dictionary", room_dict) 

            if traversal_path:
                previos_room = global_directions[traversal_path[-1]]
                room_dict[previos_room] = previos_room

            # add unexplored room to the room id
            local_graph[room_id] = room_dict
            print("Local graph: ", local_graph[room_id])

        else:
            break
        
        # need to see if a room connected
        possible_exits = []
        print("room dictionary", room_dict)

        # iteration thru room dictionary
        for direction in room_dict:
            # print("direction in room", room_dict[direction])

            if room_dict[direction] == "?":
                possible_exits.append(direction)
                # print("possible exit :", room_dict[direction])
        
        # can we move to room?
        # if there undiscovered room:
        if len(possible_exits) != 0:
            
            random.shuffle(possible_exits)
            print("next possible direction to go ===>", possible_exits[0])

            direction = possible_exits[0]
            # move player to direction
            
            # log the direction
            traversal_path.append(direction)
            # print('traversal path', traversal_path)

            # player movement
            # player.travel(direction)
            # print("we moved to ", direction)
            # print("current room", room_id)

            for movement in traversal_path:
                player.travel(movement)
                print("movement ['", movement, "']")
                movement = player.current_room
                print("current room:", movement.id)
                print("possible to go:", player.current_room.get_exits())
                exits = player.current_room.get_exits()
                print("exit to", exits[0])

                # log to traversal path
                traversal_path.append(exits[0])
        else:
            next_room = bfs(room_id)

            

        


print("\nSearch Function: ", search(room_graph))
print("-------------------")
print("Local graph: ", local_graph)
print("-------------------")
print("Traversal path: ", traversal_path)
print("-------------------")

# =====================================
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")