def add_vertex(v):
  global graph
  global vertices_no
  global vertices
  if v in vertices:
    print("Vertex ", v, " already exists")
  else:
    vertices_no = vertices_no + 1
    vertices.append(v)
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
    temp = []
    for i in range(vertices_no):
        temp.append(0)
    graph.append(temp)

def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices

    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")

    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")

    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

def print_graph():
  global graph
  global vertices_no
  for i in range(vertices_no):
    for j in range(vertices_no):
      if graph[i][j] != 0:
        print(vertices[i], " -> ", vertices[j], \
        " edge weight: ", graph[i][j])


vertices = []

vertices_no = 0
graph = []

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
print("Internal representation: ", graph)