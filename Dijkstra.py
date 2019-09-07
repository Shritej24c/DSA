import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()


G.add_edge("BWI", "JFK", weight=184)
G.add_edge("BWI", "MIA", weight=946)
G.add_edge("BWI", "ORD", weight=621)
G.add_edge("JFK", "PVD", weight=144)
G.add_edge("JFK", "BOS", weight=187)
G.add_edge("JFK", "ORD", weight=740)
G.add_edge("JFK", "DFW", weight=1391)
G.add_edge('JFK', 'MIA', weight=1090)
G.add_edge('PVD', 'ORD', weight=849)
G.add_edge('BOS', 'ORD', weight=867)
G.add_edge('BOS', 'MIA', weight=1258)
G.add_edge('BOS', 'SFO', weight=2704)
G.add_edge('ORD', 'DFW', weight=802)
G.add_edge('ORD', 'SFO', weight=1846)
G.add_edge('MIA', 'DFW', weight=1121)
G.add_edge('MIA', 'LAX', weight=2342)
G.add_edge('DFW', 'LAX', weight=1235)
G.add_edge('DFW', 'SFO', weight=1464)
G.add_edge('SFO', 'LAX', weight=337)















nx.draw(G, with_labels=True, with_weights=True)

plt.show()


