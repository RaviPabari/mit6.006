"""
Breadth First Search
--------------------
An implementation of BFS on the
binary search tree implemented in
lecture 5

An implementation of the BFS demonstrated
in the lecture

"""


def bst_bfs(tree, value):
  """
  Breadth first search on a binary search tree
  with conditionals that reduce unnecessary
  traversal

  Complexity: Worst case this is O(log(n))
  """
  queue = [tree]
  i = 0
  while i < len(queue):
    curr = queue[i]
    if curr.value == value:
      return True
    i += 1
    if value < curr.value and curr.left:
      queue.append(curr.left)
    if value > curr.value and curr.right:
      queue.append(curr.right)
  return False


def add_graph_node(adjacency_list, val):
  """
  Add a node to a graph, adjacency_list
  is a dictionary of lists

  """
  adjacency_list[val] = []
  return adjacency_list


def add_directed_edge(adjacency_list, v1, v2):
  """
  Add directed graph edge to the
  adjacency list from v1 to v2

  """
  try:
    adjacency_list[v1]
    adjacency_list[v2]
  except:
    return
  adjacency_list[v1].append(v2)


def add_undirected_edge(adjacency_list, v1, v2):
  """
  Add an undirected graph edge to the
  adjacency list

  """
  try:
    adjacency_list[v1]
    adjacency_list[v2]
  except:
    return
  adjacency_list[v1].append(v2)
  adjacency_list[v2].append(v1)



def graph_bfs(s, adjacency_list):
  """
  Graph breadth first search will visit
  every node and return 2 dictionaries

  levels maps each node's value to its
  distance from s

  parents creates a list of pointers
  which can be used to create a tree
  whose root is s

  Complexity: O(v + e) where v is the number of nodes
    and e is the number of edges

  """
  levels = { s: 0 }
  parents = { s: None }
  i = 1
  frontier = [s]
  while frontier:
    next_frontier = []
    for u in frontier:
      for v in adjacency_list[u]:
        if v not in levels:
          levels[v] = i
          parents[v] = u
          next_frontier.append(v)
    frontier = next_frontier
    i += 1
  return (levels, parents)
