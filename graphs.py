# graph.py
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
# A simple graph structure for representing the search algorithms.
# Here, we use a dictionary for representing the graph.

class Graph:
  """
  This class implements a simple graph structure.
  """

  def __init__(self, edges=[], directed=True, root=None):
    """
    Description
    -----------
    Constructor for Graph class.
    A graph can be initialized with a list of edges, a flag for being directed or not and a root node.
    Edges are given as tuples.
    
    Example
    -------
    >>> Graph(directed=True, root=initial_state)
    """
    
    self.directed = directed
    self.graph = {}
    
    self.root = root
    if root:
      self.graph[tuple(root)] = set([])
  
    self.add_edges_from(edges)



  def add_edges_from(self, edges):
    """
    Description
    -----------
    Add edges from a list of edges.
    Edges are given as a tuple (containing two nodes).
    
    Example
    -------
    >>> G = Graph(directed=True, root=initial_state)
    >>> G.add_edges_from([(1,2), (2,3)])
    """
    for node1, node2 in edges:
      self.add_edge(node1,node2)


  def add_edge(self, node1, node2):
    """
    Description
    -----------
    Add a single edge to the graph.
    Edges are given as a tuple (containing two nodes).
    
    Example
    -------
    >>> G = Graph(directed=True, root=initial_state)
    >>> G.add_edge(1,2)
    """

    def _add(n1, n2):
      n1 = tuple(n1)
      n2 = tuple(n2)
      if n1 in self.graph.keys():
        self.graph[n1].add(n2)
      else:
        self.graph[n1] = set([n2])

    _add(node1, node2)

    if not self.directed:
      _add(node2, node1)
