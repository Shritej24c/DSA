import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("a", "b", weight=0.31)
G.add_edge("q", "b", weight=0.50)

print(G.get_edge_data("a", "b"))

nx.complete_graph(3)
print(nx.adjacency_data(G))

nx.draw(G, with_labels=True, with_weights=True)


plt.show()
