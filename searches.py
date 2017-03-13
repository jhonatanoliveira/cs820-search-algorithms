from collections import deque
import queue

from graphs import Graph
from utilities import *


GOAL_STATE = [1,2,3,8,0,4,7,6,5]


def depth_first_search(initial_state, goal_state=GOAL_STATE):
  
  graph = Graph(directed = True, root = initial_state)
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
  
  graph = Graph(directed = True, root = initial_state)
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


# Tiles out of place
def best_first_search_1(initial_state, goal_state=GOAL_STATE):
  
  graph = Graph(directed = True, root = initial_state)
  stack = queue.PriorityQueue()
  stack.put((0,initial_state))
  visited = []
  found_goal = False

  depth_counter = 0

  while (stack.qsize() > 0) and (not found_goal):

    priority, current_state = stack.get(block=False)

    if not current_state in visited:

      visited.append(current_state)
      depth_counter += 1

      all_possible_states = find_all_possible_states_from(current_state)

      # Compute priority
      for poss_state in all_possible_states:
        out_of_place = 0
        for pos,block in enumerate(poss_state):
          if goal_state[pos] != block:
            out_of_place += 1
        priority = depth_counter + out_of_place

        graph.add_edge(current_state, poss_state)
        stack.put((priority, poss_state))
        if poss_state == goal_state:
          visited.append(poss_state)
          found_goal = True
          break

  return visited




# Min number of moves
def best_first_search_2(initial_state, goal_state=GOAL_STATE):
  
  graph = Graph(directed = True, root = initial_state)
  stack = queue.PriorityQueue()
  stack.put((0,initial_state))
  visited = []
  found_goal = False

  depth_counter = 0

  while (stack.qsize() > 0) and (not found_goal):

    priority, current_state = stack.get(block=False)

    if not current_state in visited:

      visited.append(current_state)
      depth_counter += 1

      all_possible_states = find_all_possible_states_from(current_state)

      # Compute priority
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
        stack.put((priority, poss_state))
        if poss_state == goal_state:
          visited.append(poss_state)
          found_goal = True
          break

  return visited




# Heuristic H
def best_first_search_3(initial_state, goal_state=GOAL_STATE):
  
  graph = Graph(directed = True, root = initial_state)
  stack = queue.PriorityQueue()
  stack.put((0,initial_state))
  visited = []
  found_goal = False

  depth_counter = 0

  while (stack.qsize() > 0) and (not found_goal):

    priority, current_state = stack.get(block=False)

    if not current_state in visited:

      visited.append(current_state)
      depth_counter += 1

      all_possible_states = find_all_possible_states_from(current_state)

      # Compute priority
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
        stack.put((priority, poss_state))
        if poss_state == goal_state:
          visited.append(poss_state)
          found_goal = True
          break

  return visited

