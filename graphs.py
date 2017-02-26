class Graph:

  def __init__(self, edges=[], directed=True, root=None):
    
    self.directed = directed
    self.graph = {}
    
    self.root = root
    if root:
      self.graph[tuple(root)] = set([])
  
    self.add_edges_from(edges)

  def add_edges_from(self, edges):
    for node1, node2 in edges:
      self.add_edge(node1,node2)


  def add_edge(self, node1, node2):

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
