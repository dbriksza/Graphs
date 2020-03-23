from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

room_map = {}

visited = set()


while len(visited) < 500:
    next_move = None
    visited.add(player.current_room.id)

    previous_room = player.current_room.id

    possible_moves = list(player.current_room.get_exits())

    for move in possible_moves:
        if previous_room not in room_map.keys():
            room_map[previous_room] = {}
        try:
            room_map[previous_room][move] != '?'
        except KeyError:
            room_map[previous_room][move] = '?'
        
    for move in possible_moves:
        if room_map[previous_room][move] == '?':
            next_move = move

    if next_move != None:

        # next_move = random.choice(possible_moves)
        traversal_path.append(next_move)
        player.travel(next_move)
        current_room = player.current_room.id
        print(f"previous room: {previous_room}, direction: {next_move}, current room: {current_room}")
        if next_move == 'n':
            room_map[previous_room]['n'] = current_room
            if current_room not in room_map.keys():
                room_map[current_room] = {}
            room_map[current_room]['s'] = previous_room
        if next_move == 's':
            room_map[previous_room]['s'] = current_room
            if current_room not in room_map.keys():
                room_map[current_room] = {}
            room_map[current_room]['n'] = previous_room
        if next_move == 'e':
            room_map[previous_room]['e'] = current_room
            if current_room not in room_map.keys():
                room_map[current_room] = {}
            room_map[current_room]['w'] = previous_room
        if next_move == 'w':
            room_map[previous_room]['w'] = current_room
            if current_room not in room_map.keys():
                room_map[current_room] = {}
            room_map[current_room]['e'] = previous_room
        print(f"previous room: {room_map[previous_room]} current room: {room_map[current_room]} visited: {len(visited)}")
    else:
        visited_just_now = set()
        q = Queue()
        p = Queue()
        q.enqueue([player.current_room.id])
        p.enqueue([player.current_room.id])
        
        while q.size() > 0:

            rooms = q.dequeue()
            path = p.dequeue()
            print(path)
            print(rooms)
            current_node = rooms[-1]
            print(f"current node {current_node}")
            if '?' in list(room_map[current_node].values()):
                # path.append(list(room_map[current_node].keys())[list(room_map[current_node].values()).index('?')])
                print(path)
                path.pop(0)
                for move in path:
                    player.travel(move)
                    traversal_path.append(move)
                    prev = move
                    print(f"direction: {move} current room: {player.current_room.id}")
                break
            else:
                if current_node not in visited_just_now:
                    visited_just_now.add(current_node)
                    edges = room_map[current_node].values()
                for edge in edges:
                    print(edge)
                    new_rooms = list(rooms)
                    new_path = list(path)
                    new_rooms.append(edge)
                    try:
                        new_path.append(list(room_map[current_node].keys())[list(room_map[current_node].values()).index(edge)])
                        p.enqueue(new_path)
                    except ValueError:
                        continue
                    q.enqueue(new_rooms)
                    




# def findroute():
#     player = Player(world.starting_room)
#     travel_path = []
#     last_move = None
#     next_move = None
#     visited = set()
#     while len(visited) < 500:
#         visited.add(player.current_room.id)
#         possible_moves = player.current_room.get_exits()
        
#         if len(possible_moves) > 1:
#             if last_move == 'n':
#                 possible_moves.remove('s')
#                 next_move = random.choice(possible_moves)
#             if last_move == 's':
#                 possible_moves.remove('n')
#                 next_move = random.choice(possible_moves)
#             if last_move == 'e':
#                 possible_moves.remove('w')
#                 next_move = random.choice(possible_moves)
#             if last_move == 'w':
#                 possible_moves.remove('e')
#                 next_move = random.choice(possible_moves)
#             else:
#                 next_move = random.choice(possible_moves)
#         else:
#             if last_move == 'n':
#                 next_move = 's'
#             if last_move == 's':
#                 next_move = 'n'
#             if last_move == 'e':
#                 next_move = 'w'
#             if last_move == 'w':
#                 next_move = 'e'
#         print(f"next Move: {last_move} rooms visited: {len(visited)} current room {player.current_room.id} moves {len(travel_path)}")
#         travel_path.append(next_move)
#         player.travel(next_move)
#         last_move = next_move
#         if len(travel_path) > 2000:
#             findroute()
#             break
#     return travel_path

# traversal_path = findroute()

# last_move = None
# next_move = None
# visited = set()
# rooms = {}
# moves_made = {}
# while len(visited) < 500:
#     visited.add(player.current_room.id)
    
#     rooms[player.current_room.id] = player.current_room.get_exits()

#     possible_moves = player.current_room.get_exits()
#     if player.current_room.id in moves_made.keys():
#         for move in moves_made[player.current_room.id]:
#             possible_moves.remove(move)
#     next_move = random.choice(possible_moves)

#     if player.current_room.id in moves_made.keys():
#         moves_made[player.current_room.id].append(next_move)
#     else:
#         moves_made[player.current_room.id] = [next_move]

#     possible_moves = rooms[player.current_room.id]

#     print(f"next Move: {last_move} rooms visited: {len(visited)} current room {player.current_room.id} moves {len(traversal_path)}")
#     traversal_path.append(next_move)
#     player.travel(next_move)
#     last_move = next_move

# last_move = None
# next_move = None
# visited = set()
# room_map = {}
# last_room = None
# while len(visited) < 500:
#     visited.add(player.current_room.id)
#     possible_moves = player.current_room.get_exits()
    
#     if len(possible_moves) > 1:
#         if last_move == 'n': 
#             possible_moves.remove('s')
#             next_move = random.choice(possible_moves)
#         if last_move == 's':
#             possible_moves.remove('n')
#             next_move = random.choice(possible_moves)
#         if last_move == 'e':
#             possible_moves.remove('w')
#             next_move = random.choice(possible_moves)
#         if last_move == 'w':
#             possible_moves.remove('e')
#             next_move = random.choice(possible_moves)
#         else:
#             next_move = random.choice(possible_moves)
#     else:
#         if last_move == 'n':
#             next_move = 's'
#         if last_move == 's':
#             next_move = 'n'
#         if last_move == 'e':
#             next_move = 'w'
#         if last_move == 'w':
#             next_move = 'e'
#     if last_room not in room_map:
#         room_map[last_room] = {}
#     room_map[last_room][player.current_room.id] = last_move
#     last_room = player.current_room.id
#     player.travel(next_move)
#     last_move = next_move

# player.current_room = world.starting_room

# next_move = None
# visited = set()
# last_move = None
# while len(visited) < 500:
#     visited.add(player.current_room.id)
#     possible_moves = player.current_room.get_exits()
#     if len(possible_moves) > 1:
#         remove = []
#         possible_moves = list(room_map[player.current_room.id].keys())
#         possible_moves = [x for x in possible_moves if x not in visited]
#         print(possible_moves)
#         if possible_moves:
#             next_move = room_map[player.current_room.id][max(possible_moves)]
#         else:
#             next_move = room_map[player.current_room.id][min(room_map[player.current_room.id].keys())]
#     else:
#         next_move = str(possible_moves[0])
#     print(f"next Move: {next_move} rooms visited: {len(visited)} current room {player.current_room.id} length {len(traversal_path)}")
#     last_move = next_move
#     traversal_path.append(next_move)
#     player.travel(next_move)

# print(visited)



# while len(traversal_path) > 2000:
#     traversal_path = findroute()

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
