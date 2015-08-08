"""
  Unidrected Graph data structure implemented:
  --------------------------------------------
  The Undirected_Graph class represents an undirected graph of vertices
  which can be any hashable value.
  
  It supports the following two primary operations: 
  add_edge: add an edge to the graph O(1)
  adj: return list of all of the vertices adjacent to a vertex O(1)
  vertices: return list of all vertices in the graph O(N)

  It also supports the followign secondary operations:
  vertex_count: return the number of vertices O(1)
  edge_count: return the number of edges O(1)
  degree: return degree of the vertex O(1)
  
  Parallel edges and self-loops are permitted.

  Adapted from: http://algs4.cs.princeton.edu/41undirected/Graph.java.html
 """

class Undirected_Graph :
  def __init__(self):
    self.__adj = {}
    self.__v_count = 0
    self.__e_count = 0

  def vertex_count(self):
    """
    Returns the number of vertices in the graph.
    """

    return self.__v_count
  
  def edge_count(self):
    """
    Returns the number of edges in the graph.
    """

    return self.__e_count

  def add_edge(self, src, dest):
    """
    Adds an undirected edge 'src'-'dest' to the graph.
    """
    if src in self.__adj:
      self.__adj[src].append(dest)
    else:
      self.__adj[src] = [dest]
      self.__v_count += 1


    if dest in self.__adj:
      self.__adj[dest].append(src)
    else:
      self.__adj[dest] = [src]
      self.__v_count += 1

    self.__e_count += 1

  def adj(self, src):
    """
    Returns the vertices adjacent to vertex 'src'.
    """
    return self.__adj[src]

  def degree(self, src):
    """
    Returns the degree of the vertex 'src'
    """
    if src in self.__adj:
      return len(self.__adj[src])
    else:
      raise LookupError("This vertex is not in the graph.")

  def vertices(self):
    """
    Returns an iterable of all the vertices in the graph.
    """
    return self.__adj.keys()

  def __str__(self):
    s = []
    s.append("{0} vertices and {1} edges \n".format(self.__vertex_count, 
                                                    self.__edge_count))
    for key in self.vertices():
      s.append("{0}: ".format(key))
      for val in self.adj(key):
        s.append("{0} ".format(val))
      s.append("\n")

    return "".join(s)