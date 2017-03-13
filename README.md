Description
-----------

This is the solution for Assignment 2 in CS820 - Artificial Intelligence.
The solution proposes an implementation of 5 search algorithms for solving the 8-puzzle problem.
Follows an overview for each implemented algorithm:

1) Depth-first search (DFS) is an algorithm for traversing a graph. It starts at the root and explores as deep as possible along each branch before backtracking.
2) Breadth-first search (BFS) is an algorithm for traversing a graph. It starts at the root and explores the neighbor nodes first, before moving to the next level neighbors.
3) Best-first search with heuristic being number of tiles out of place.
4) Best-first search with heuristic being minimum number of moves to reach the goal state.
5) Best-first search with heuristic being the total distance and sequence score.
  - The "total distance" of the eight tiles in a board position from their "home squares". We use the Manhattan distance to calculate the distance of each tile from its home square.
  - The "sequence score" that measures the degree to which the tiles are already ordered in the current position with respect to the order required in the goal configuration.


There are 5 files in this solution:
  - main.py: utility script with a simple user menu for running an initial state with a chosen search algorithm.
  - searches.py: search algorithm implementations.
  - README: overview and instructions
  - graphs.py: a simple graph structure implementation.
  - utilities.py: shared utility functions.
  - tests.py: helper script for demonstrating functions.

You can also find this solution in the following [GitHub repository](https://github.com/jhonatanoliveira/cs820-strips-8-puzzle).


Requirements
-------------

This solution requires the following softwares:
- Python 3.6 or higher


How it Works
-------------

Functions can be called from the ```searches.py``` file individually or an user can use the ```main.py``` script helper for a simple menu navigation.
Notice that all state input is *comma separated* and with numbers filling the board from *top* to *down* and from *left* to *right* and *number zero* representing the clear block.
For example, an initial state 1,2,3,0,6,4,8,7,5 represents the following board configuration:

|   |   |   |
|---|---|---|
| 1 | 2 | 3 |
|   | 6 | 4 |
| 8 | 7 | 5 |

where the X is the clear block.



Getting Started
---------------

In order to run the solution using the user's menu, the script ```main.py``` can be called from the terminal command as follows:

```
$ python main.py
```

This is an example of a complete user interaction run:

```
$ python main.py
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
```

Users can keep running the menu as long as they want by typing "Y" or "y" at the end of the search algorithm run.


AUTHOR
---------
Jhonatan S. Oliveira,
oliveira@uregina.ca,
Department of Computer Science,
University of Regina,
Canada
