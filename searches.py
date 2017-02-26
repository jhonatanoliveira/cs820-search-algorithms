from graphs import Graph
from utilities import *

def depth_first_search(initial_state, goal_state=[1,2,3,8,0,4,7,6,5], max_depth=1000):
  
  graph = Graph(directed = True, root = initial_state)
  stack = [initial_state]
  visited = []
  depth_count = 0
  found_goal = False

  while (len(stack) > 0) and (not found_goal):

    current_state = stack.pop()
    visited.append(current_state)

    all_possible_states = find_all_possible_states_from(current_state)

    for state in all_possible_states:
      graph.add_edge(current_state, state)
      stack.append(state)
      if state == goal_state:
        visited.append(state)
        found_goal = True
      break

  return visited

