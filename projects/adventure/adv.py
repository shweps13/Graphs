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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
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
local_graph = {}

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


def search(starting_room):
    print("===Beginning of search===\n")
    # Counter of rooms where player was
    visited_room = 0

    # Define opposite directions
    global_directions = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

    while len(local_graph) != len(room_graph):
        # print("current room:", room_id)
        
        # Where player now
        current_room = player.current_room

        # # Id of current room
        room_id = current_room.id
        
        # Define dictionary with room directions
        room_dict = {}

        if room_id not in local_graph:
            # Find possible exits

            for i in current_room.get_exits():
                # add "?" to the room dictionary
                room_dict[i] = '?'
                # print("room dictionary", room_dict) 

            if traversal_path:
                # previous room == opposide direction of last traversal path
                previos_room = global_directions[traversal_path[-1]]

                # add previous_room to the room dictionaty
                room_dict[previos_room] = visited_room

            # add unexplored room to the room id
            local_graph[room_id] = room_dict
            # print("Local graph: ", local_graph[room_id])

        else:
            # Add the room id from local_graph to the inner room dictionary
            room_dict = local_graph[room_id]
        
        # need to see if a room connected
        possible_exits = []
        # print("room dictionary", room_dict)

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
            print("next possible direction to go ===> ['", possible_exits[0], "']")

            direction = possible_exits[0]
            
            # log the direction to traversal
            traversal_path.append(direction)
            # print('traversal path', traversal_path)

            # move player to direction
            player.travel(direction)

            # replace "?" in local_graph with discovered rooms
            movement = player.current_room
            # print("room", local_graph[current_room.id][direction])
            local_graph[current_room.id][direction] = movement.id
            # print("movement", movement.id)
            visited_room = current_room.id
            # print('visited room id: ', visited_room)

        else:
            # BFS to search for next exits/possible rooms using room_id
            next_room = bfs(room_id)
            # print("Next room", next_room) 
            # print("length of next_room", len(next_room))

            # if path of next_room has results from bfs
            if next_room is not None and len(next_room) > 0:
                # print("===Testtestestest===")
                
                # iterate length of the room to give access to room id
                for i in range(len(next_room) -1):
                    # print("map check at: ", local_graph[next_room[i]])

                    # iterate the local_graph dictionary next room at this index to get directions
                    for direction in local_graph[next_room[i]]:
                        # print("direction", direction)
                        # print("conditional", local_graph[next_room[i]][direction])
                        # print("checking next plus one", next_room[i + 1])

                        # if local_graph next_room[i] and [direction] matches that of following room[i] found thru bfs
                        if local_graph[next_room[i]][direction]  == next_room[i + 1]:
                            # print("traversal_path", traversal_path.append(direction))
                            
                            # append the direction to travel_path
                            traversal_path.append(direction)
                            # print("player travel", traversal_path.append(direction))
                            # move player to that room
                            player.travel(direction)
                            # print("player travel", current_room.id)
            else:
                break

            
        


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