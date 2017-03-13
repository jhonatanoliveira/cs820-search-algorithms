from searches import *


def main():

  keep_running = True

  while keep_running:

    print(">>> Initial state (comma separated):")
    initial_state_str = input("--> ")
    initial_state = [int(n.strip()) for n in initial_state_str.split(",")]

    print(">>> Choose the Search algorithm")
    print(">>> 1) Depth First")
    print(">>> 2) Breath First")
    print(">>> 3) Best First - tiles out of place")
    print(">>> 4) Best First - min moves")
    print(">>> 5) Best First - heuristic H")

    option = input("--> ")

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
    

    if result:
      print(">>> Result:")
      print(result)
    else:
      print(">>> Not a valid choice.")


    print(">>> Want to try again? (Y/N)")
    again = input("--> ")

    if again != "y" and again != "Y":
      keep_running = False



if __name__ == "__main__":
  main()
