import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_nodes_from([(4, {"color": "red"}), (5, {"color": "blue"})])
nx.draw(g, with_labels=True, node_color="red", node_size=800)
plt.show()