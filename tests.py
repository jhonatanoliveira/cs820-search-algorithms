from graphs import Graph
from searches import *


# Graphs
print()
print("---> Begin Test <---")
print("*** Graphs ***")
initial_state = [1,2,3,8,7,4,0,6,5]
G = Graph(directed=True, root=initial_state)
print(G.graph)
print(G.root)
print("---> End Test <---")

# Swap state
print()
print("---> Begin Test <---")
print("*** Swap States ***")
original = [1,2,3,8,7,4,0,6,5]
ss = swap_state(original, 6,7)
print(original)
print(ss)
print("---> End Test <---")

# Find All possible
print()
print("---> Begin Test <---")
print("*** Find all possible states ***")
original = [1,2,3,4,0,8,5,7,6]
r = find_all_possible_states_from(original)
print(r)
original = [1,2,0,4,3,8,5,7,6]
r = find_all_possible_states_from(original)
print(r)
print("---> End Test <---")

# Depth First
print()
print("---> Begin Test <---")
print("*** Depth First Search ***")
original = [1,2,3,8,4,0,7,6,5]
r = depth_first_search(original)
print(r)
print("---> End Test <---")

# Breath First
print()
print("---> Begin Test <---")
print("*** Breath First Search ***")
original = [1,2,3,8,4,5,7,6,0]
r = breath_first_search(original)
print(r)
print("---> End Test <---")