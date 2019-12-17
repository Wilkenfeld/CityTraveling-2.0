import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph as Graph

graph_obj = Graph("C:/Users\Roberto\Desktop\progetto scientifico FLL\samples\cities/test.json")

        
nx.draw_networkx(graph, with_labels=True, pos=position_dict)

plt.draw()
plt.show()
# print("Nodes >> {0}\nEdges >> {1}".format(graph.number_of_nodes(), graph.number_of_edges()))