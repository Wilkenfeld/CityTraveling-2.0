import networkx as nx
import matplotlib.pyplot as plt
from samples.classes.graph import Graph as Graph

graph_obj = Graph("./samples//cities/city1.json")
        
graph = nx.Graph()

graph_dict = dict()

# Adds the nodes to the graph
for node in graph_obj.nodes:
    graph.add_node(node.id)
    # Adds the edges
    for link in node.closeTo:
        graph.add_edge(node.id, link[0], weight=link[1])

    graph_dict[node.id] = node.position
    print(node.position)

nx.draw_networkx(graph, with_labels=True, pos=graph_dict)

plt.draw()
# plt.show()
# print("Nodes >> {0}\nEdges >> {1}".format(graph.number_of_nodes(), graph.number_of_edges()))
for x in graph.nodes:
    print(x)