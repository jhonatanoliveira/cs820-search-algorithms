from collections import deque

from graphs import Graph
from utilities import *

GOAL_STATE = [1,2,3,8,0,4,7,6,5]


def depth_first_search(initial_state, goal_state=GOAL_STATE, max_depth=1000):
  
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



def breath_first_search(initial_state, goal_state=GOAL_STATE, max_depth=1000):
  
  graph = Graph(directed = True, root = initial_state)
  queue = deque([initial_state])
  visited = []
  depth_count = 0
  found_goal = False

  while (len(queue) > 0) and (not found_goal):

    current_state = queue.popleft()
    visited.append(current_state)

    all_possible_states = find_all_possible_states_from(current_state)

    for state in all_possible_states:
      graph.add_edge(current_state, state)
      queue.append(state)
      if state == goal_state:
        visited.append(state)
        found_goal = True
      break

  return visited

