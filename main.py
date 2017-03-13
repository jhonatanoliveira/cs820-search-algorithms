# main.py
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
# This script is a utility for running all implemented search algorithms.
# After calling the script in a prompt command, the user can input an initial state for the 8-puzzle problem and pick a search algorithm.
# For more details, please, see documentation in the README file.

from searches import *


def main():
  """
  Description
  -----------
  Shows a menu to the user.
  User can input an initial state by typing numbers in sequence and comma separated.
  User can pick a search algorithm for solving the problem from the initial state.
  See README file for more details.
  
  Example
  -------
  >>> main()
  >>> Initial state (comma separated):
  --> 1,2,3,8,5,6,7,4,0
  >>> Choose the Search algorithm
  >>> 1) Depth First
  >>> 2) Breath First
  >>> 3) Best First - tiles out of place
  >>> 4) Best First - min moves
  >>> 5) Best First - heuristic H
  --> 3
  >>> Result:
  [[1, 2, 3, 8, 5, 6, 7, 4, 0], [1, 2, 3, 8, 5, 0, 7, 4, 6], [1, 2, 3, 8, 0, 5, 7, 4, 6], [1, 2, 3, 8, 5, 6, 7, 0, 4], [1, 2, 0, 8, 5, 3, 7, 4, 6], [1, 2, 3, 8, 0, 6, 7, 5, 4], [1, 2, 3, 8, 4, 5, 7, 0, 6], [1, 0, 3, 8, 2, 5, 7, 4, 6], [1, 2, 3, 0, 8, 5, 7, 4, 6], [1, 2, 3, 8, 5, 6, 0, 7, 4], [1, 2, 3, 8, 4, 5, 7, 6, 0], [1, 2, 3, 8, 6, 0, 7, 5, 4], [1, 0, 2, 8, 5, 3, 7, 4, 6], [1, 0, 3, 8, 2, 6, 7, 5, 4], [1, 2, 3, 0, 8, 6, 7, 5, 4], [1, 2, 3, 8, 4, 5, 0, 7, 6], [1, 2, 3, 8, 4, 0, 7, 6, 5], [1, 2, 3, 8, 0, 4, 7, 6, 5]]
  >>> Want to try again? (Y/N)
  -->
  """

  keep_running = True

  while keep_running:

    # Input initial state
    print(">>> Initial state (comma separated):")
    initial_state_str = input("--> ")
    initial_state = [int(n.strip()) for n in initial_state_str.split(",")]

    # Shows options
    print(">>> Choose the Search algorithm")
    print(">>> 1) Depth First")
    print(">>> 2) Breath First")
    print(">>> 3) Best First - tiles out of place")
    print(">>> 4) Best First - min moves")
    print(">>> 5) Best First - heuristic H")

    # Input search algorithm option
    option = input("--> ")

    # Run search algorithm
    result = None
    if option == "1":
      result = depth_first_search(initial_state)
    elif option == "2":
      result = breath_first_search(initial_state)
    elif option == "3":
      result = best_first_search_1(initial_state)
    elif option == "4":
      result = best_first_search_2(initial_state)
    elif option == "5":
      result = best_first_search_3(initial_state)
    
    # Shows result from search algorithm
    if result:
      print(">>> Result:")
      print(result)
      print(">>> Number of generated nodes:")
      print(len(result))
    else:
      print(">>> Not a valid choice.")

    # Loop again if users wants to 
    print(">>> Want to try again? (Y/N)")
    again = input("--> ")

    if again != "y" and again != "Y":
      keep_running = False



# Run main
if __name__ == "__main__":
  main()
