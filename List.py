def add_vertex(v):
  global graph
  global vertices_no
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    vertices_no = vertices_no + 1
    graph[v] = []

def add_edge(v1, v2, e):
  global graph
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    temp = [v2, e]
    graph[v1].append(temp)

def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

graph = {}
vertices_no = 0
add_vertex('a')
add_vertex('b')
add_vertex('c')
add_vertex('d')
add_vertex('e')
add_vertex('f')
add_vertex('g')

add_edge('a', 'b', 5)
add_edge('a', 'c', 3)
add_edge('b', 'a', 5)
add_edge('b', 'c', 4)
add_edge('b', 'd', 6)
add_edge('b', 'e', 2)
add_edge('c', 'a', 3)
add_edge('c', 'a', 3)
add_edge('c', 'b', 4)
add_edge('c', 'd', 5)
add_edge('c', 'f', 6)
add_edge('d', 'b', 6)
add_edge('d', 'c', 5)
add_edge('d', 'e', 6)
add_edge('d', 'f', 6)
add_edge('e', 'b', 2)
add_edge('e', 'd', 6)
add_edge('e', 'f', 3)
add_edge('e', 'g', 5)
add_edge('f', 'c', 6)
add_edge('f', 'd', 6)
add_edge('f', 'e', 3)
add_edge('f', 'g', 4)
add_edge('g', 'e', 5)
add_edge('g', 'f', 4)
print_graph()
print ("Internal representation: ", graph)