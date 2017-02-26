from graphs import Graph


### Utilities


def swap_state(current_state, pos1, pos2):
  copy_state = current_state.copy()
  copy_state[pos1] = current_state[pos2]
  copy_state[pos2] = current_state[pos1]
  return copy_state


def find_all_possible_states_from(state):

  all_possible_states = []

  adjacent_positions = [ set([0,1]), set([0,3]), set([1,2]), set([1,4]), set([2,5]), set([3,4]), set([3,6]), set([4,5]), set([4,7]), set([5,8]), set([6,7]), set([7,8]) ]

  empty_pos = state.index(0)

  # Try left
  left_pos = empty_pos - 1
  if left_pos > 0 and (set([empty_pos,left_pos]) in adjacent_positions):
    all_possible_states.append( swap_state(state, empty_pos, left_pos) )

  # Try right
  right_pos = empty_pos + 1
  if right_pos < 9 and (set([empty_pos,right_pos]) in adjacent_positions):
    all_possible_states.append( swap_state(state, empty_pos, right_pos) )

  # Try top
  top_pos = empty_pos - 3
  if top_pos > 0 and (set([empty_pos,top_pos]) in adjacent_positions):
    all_possible_states.append( swap_state(state, empty_pos, top_pos) )

  # Try bottom
  bottom_pos = empty_pos + 3
  if bottom_pos < 9 and (set([empty_pos,bottom_pos]) in adjacent_positions):
    all_possible_states.append( swap_state(state, empty_pos, bottom_pos) )

  return all_possible_states



### Searxh

def depth_first_search(initial_state, goal_state=[1,2,3,8,0,4,7,6,5], max_depth=1000):
  
  graph = Graph(directed = True, root = initial_state)
  stack = [initial_state]
  visited = []
  depth_count = 0
  found_goal = False

  while (len(stack) > 0) and (not found_goal):

    current_state = stack.pop()
    if not current_state in visited:
      visited.append(current_state)

      # if depth_count < max_depth:
      #   depth_count += 1

      all_possible_states = find_all_possible_states_from(current_state)

      ### DEBUG
      if len(all_possible_states) == 0:
        print(">>>> OPS!!!")
        print(current_state)
      ### --- DEBUG

      for state in all_possible_states:
        graph.add_edge(current_state, state)
        stack.append(state)
        if state == goal_state:
          ### DEBUG
          print(">>>> FOUND!!!")
          print(state)
          ### --- DEBUG
          visited.append(state)
          found_goal = True
        break

    ### DEBUG
    if len(stack) < 1:
      print(">>>EMPTYYY")
    ### --- DEBUG

  return visited

