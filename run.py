import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_nodes_from([1, 2, 3, 4])  # 4 — изолированная вершина
g.add_edges_from([(1, 2), (2, 3), (1, 3)])

# раскладка только для связной компоненты
connected_nodes = [1, 2, 3]
subgraph = g.subgraph(connected_nodes)
pos = nx.spring_layout(subgraph, seed=42, k=0.1)

# копируем позиции в общий словарь
full_pos = {}
full_pos.update(pos)

# вручную задаём координаты для изолированных вершин
full_pos[4] = (1.5, 0)  # ставим справа от графа
node_colors = ["red" if node == 4 else "lightblue" for node in g.nodes()]

nx.draw(
    g, full_pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=14
)

plt.show()
