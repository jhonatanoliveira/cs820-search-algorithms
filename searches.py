# searches.py
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
# We propose a solution for the 8-puzzle problem using 5 search algorithms: depth first search, breath first search, best first search with 3 different heuristics. Follows their description below:
# 1) Depth-first search (DFS) is an algorithm for traversing a graph. It starts at the root and explores as deep as possible along each branch before backtracking.
# 2) Breadth-first search (BFS) is an algorithm for traversing a graph. It starts at the root and explores the neighbor nodes first, before moving to the next level neighbors.
# 3) Best-first search with heuristic being number of tiles out of place.
# 4) Best-first search with heuristic being minimum number of moves to reach the goal state.
# 5) Best-first search with heuristic being the total distance and sequence score.
#   5.1) The "total distance" of the eight tiles in a board position from their "home squares". We use the Manhattan distance to calculate the distance of each tile from its home square.
#   5.2) The "sequence score" that measures the degree to which the tiles are already ordered in the current position with respect to the order required in the goal configuration.
#
#
# IMPLEMENTATION STRUCTURES
# -------------------------
# - Initial state
#   A list with 9 numbers. 
#   The order in the list represents the game board from left to right and from top to bottom. 
#   The number zero represents the empty block.
#   For example,
#     [1,2,3,8,5,6,7,4,0]
#   represents the following board game configuration:
#     1 | 2 | 3
#     ----------
#     8 | 5 | 6
#     ----------
#     7 | 4 |   



# General purposes libraries
from collections import deque
import queue
# Local libraries
from graphs import Graph
from utilities import *



# Constant representing the goal state
GOAL_STATE = [1,2,3,8,0,4,7,6,5]



def depth_first_search(initial_state, goal_state=GOAL_STATE):
  """
  Description
  -----------
  Implements the depth first search algorithm.
  
  Example
  -------
  >>> initial_state = [1,2,3,8,5,6,7,4,0]
  >>> depth_first_search(initial_state)
  [[1, 2, 3, 8, 5, 6, 7, 4, 0], [1, 2, 3, 8, 5, 0, 7, 4, 6], ... ]
  """
  
  graph = Graph(directed = True, root = initial_state)
  # Uses a stack for the depth first search
  stack = [initial_state]
  visited = []
  found_goal = False

  while (len(stack) > 0) and (not found_goal):

    current_state = stack.pop()

    if not current_state in visited:

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



def breath_first_search(initial_state, goal_state=GOAL_STATE):
  """
  Description
  -----------
  Implements the breath first search algorithm.
  
  Example
  -------
  >>> initial_state = [1,2,3,8,5,6,7,4,0]
  >>> breath_first_search(initial_state)
  [[1, 2, 3, 8, 5, 6, 7, 4, 0], [1, 2, 3, 8, 5, 6, 7, 0, 4], [1, 2, 3, 8, 5, 0, 7, 4, 6], [1, 2, 3, 8, 5, 6, 0, 7, 4], ... ]
  """
  
  graph = Graph(directed = True, root = initial_state)
  # Using a queue for the breath first search
  queue = deque([initial_state])
  visited = []
  found_goal = False

  while (len(queue) > 0) and (not found_goal):

    current_state = queue.popleft()

    if not current_state in visited:

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



def best_first_search_1(initial_state, goal_state=GOAL_STATE):
  """
  Description
  -----------
  Best search algorithm using the number of tiles out of place as heuristic.
  
  Example
  -------
  >>> initial_state = [1,2,3,8,5,6,7,4,0]
  >>> best_first_search_1(initial_state)
  [[1, 2, 3, 8, 5, 6, 7, 4, 0], [1, 2, 3, 8, 5, 0, 7, 4, 6], [1, 2, 3, 8, 0, 5, 7, 4, 6], ... ]
  """
  
  graph = Graph(directed = True, root = initial_state)
  # Uses a priority queue for a best search algorithm
  stack = queue.PriorityQueue()
  stack.put((0,initial_state,0))
  visited = []
  found_goal = False

  while (stack.qsize() > 0) and (not found_goal):

    priority, current_state, depth_counter = stack.get(block=False)

    if not current_state in visited:

      visited.append(current_state)

      all_possible_states = find_all_possible_states_from(current_state)

      # Compute priority based on the heuristic
      for poss_state in all_possible_states:
        out_of_place = 0
        for pos,block in enumerate(poss_state):
          if goal_state[pos] != block:
            out_of_place += 1
        priority = depth_counter + out_of_place

        graph.add_edge(current_state, poss_state)
        stack.put((priority, poss_state, depth_counter + 1))
        if poss_state == goal_state:
          visited.append(poss_state)
          found_goal = True
          break

  return visited



def best_first_search_2(initial_state, goal_state=GOAL_STATE):
  """
  Description
  -----------
  Best search algorithm using the minimum number moves to reach the goal state as heuristic.
  
  Example
  -------
  >>> initial_state = [1,2,3,8,5,6,7,4,0]
  >>> best_first_search_2(initial_state)
  [[1, 2, 3, 8, 5, 6, 7, 4, 0], [1, 2, 3, 8, 5, 6, 7, 0, 4], [1, 2, 3, 8, 5, 6, 0, 7, 4], ... ]
  """
  
  graph = Graph(directed = True, root = initial_state)
  # Uses a priority queue for a best search algorithm
  stack = queue.PriorityQueue()
  stack.put((0,initial_state,0))
  visited = []
  found_goal = False

  while (stack.qsize() > 0) and (not found_goal):

    priority, current_state, depth_counter = stack.get(block=False)

    if not current_state in visited:

      visited.append(current_state)

      all_possible_states = find_all_possible_states_from(current_state)

      # Compute priority based on the heuristic
      total_distance = 0
      for poss_state in all_possible_states:
        for pos,block in enumerate(poss_state):
          if goal_state[pos] != block:
            # Count vertical distance
            desired_pos = goal_state.index(block)
            def _get_row_level(p):
              level = 0
              if p >=0 and p < 3:
                level = 1
              elif p > 2 and p < 6:
                level = 2
              else:
                level = 9
              return level
            pos_row_lvl = _get_row_level(pos)
            des_pos_row_lvl = _get_row_level(desired_pos)
            vertical_distance = abs(des_pos_row_lvl-pos_row_lvl)
            # Count horizontal distance
            horizontal_distance = abs((pos % 3) - (desired_pos % 3))
            # Add to total distance
            total_distance += vertical_distance + horizontal_distance
        priority = depth_counter + total_distance

        graph.add_edge(current_state, poss_state)
        stack.put((priority, poss_state, depth_counter + 1))
        if poss_state == goal_state:
          visited.append(poss_state)
          found_goal = True
          break

  return visited




# Heuristic H
def best_first_search_3(initial_state, goal_state=GOAL_STATE):
  """
  Description
  -----------
  Best search algorithm using the total distance and sequence score as heuristic.
  The "total distance" of the eight tiles in a board position from their "home squares". We use the Manhattan distance to calculate the distance of each tile from its home square.
  The "sequence score" that measures the degree to which the tiles are already ordered in the current position with respect to the order required in the goal configuration.
  
  Example
  -------
  >>> initial_state = [1,2,3,8,5,6,7,4,0]
  >>> best_first_search_3(initial_state)
  [[1, 2, 3, 8, 5, 6, 7, 4, 0], [1, 2, 3, 8, 5, 6, 7, 0, 4], [1, 2, 3, 8, 5, 6, 0, 7, 4], ... ]
  """
  
  graph = Graph(directed = True, root = initial_state)
  # Uses a priority queue for a best search algorithm
  stack = queue.PriorityQueue()
  stack.put((0,initial_state,0))
  visited = []
  found_goal = False

  while (stack.qsize() > 0) and (not found_goal):

    priority, current_state, depth_counter = stack.get(block=False)

    if not current_state in visited:

      visited.append(current_state)

      all_possible_states = find_all_possible_states_from(current_state)

      # Compute priority based on the heuristic
      total_distance = 0
      seq = 0
      H = 0
      for poss_state in all_possible_states:
        for pos,block in enumerate(poss_state):
          if goal_state[pos] != block:
            # Compute the Total Distance for H
            # Count vertical distance
            desired_pos = goal_state.index(block)
            def _get_row_level(p):
              level = 0
              if p >=0 and p < 3:
                level = 1
              elif p > 2 and p < 6:
                level = 2
              else:
                level = 9
              return level
            pos_row_lvl = _get_row_level(pos)
            des_pos_row_lvl = _get_row_level(desired_pos)
            vertical_distance = abs(des_pos_row_lvl-pos_row_lvl)
            # Count horizontal distance
            horizontal_distance = abs((pos % 3) - (desired_pos % 3))
            # Add to total distance
            total_distance += vertical_distance + horizontal_distance
            # Compute the Sequence Score
            if pos == 4: # if it's the center block, then scores 1 to seq
              seq += 1
            else: # otherwise, scores 2 to seq
              seq += 2
        H = total_distance + 3 * seq
        priority = depth_counter + H

        graph.add_edge(current_state, poss_state)
        stack.put((priority, poss_state, depth_counter + 1))
        if poss_state == goal_state:
          visited.append(poss_state)
          found_goal = True
          break

  return visited

