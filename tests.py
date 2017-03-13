# test.py
#
# AUTHOR
# ---------
# Jhonatan S. Oliveira
# oliveira@uregina.ca
# Department of Computer Science
# University of Regina
# Canada
#
#
# DESCRIPTION
# -----------
# This runs all the main functions for the search algorithm implementations.
# The tests are not formal and are not checked.
# This is only a simple way of visualizing outputs and trying different settings for running the implementations.


from graphs import Graph
from searches import *

def main():

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
  original = [1,2,3,8,5,6,7,4,0]
  r = depth_first_search(original)
  print(r)
  print("---> End Test <---")

  # Breath First
  print()
  print("---> Begin Test <---")
  print("*** Breath First Search ***")
  original = [1,2,3,8,5,6,7,4,0]
  r = breath_first_search(original)
  print(r)
  print("---> End Test <---")

  # Best first search 1
  print()
  print("---> Begin Test <---")
  print("*** Best First Search 1 ***")
  original = [1,2,3,8,5,6,7,4,0]
  r = best_first_search_1(original)
  print(r)
  print("---> End Test <---")

  # Best first search 2
  print()
  print("---> Begin Test <---")
  print("*** Best First Search 2 ***")
  original = [1,2,3,8,5,6,7,4,0]
  r = best_first_search_2(original)
  print(r)
  print("---> End Test <---")

  # Best first search 3
  print()
  print("---> Begin Test <---")
  print("*** Best First Search 3 ***")
  original = [1,2,3,8,5,6,7,4,0]
  r = best_first_search_3(original)
  print(r)
  print("---> End Test <---")



# Run main
if __name__ == "__main__":
  main()
