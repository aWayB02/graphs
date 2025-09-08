import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

g = nx.MultiGraph()
g.add_nodes_from([1, 2, 3, 4, 5, 6])
g.add_edges_from([(1, 2), (1, 2), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5), (5, 6)])

pos = nx.spring_layout(g, k=0.3, iterations=50)

# Рисуем узлы и подписи
nx.draw_networkx_nodes(g, pos, node_color="skyblue", node_size=1200)
nx.draw_networkx_labels(g, pos, font_size=14, font_weight="bold")

# Считаем кратные рёбра
edge_counts = defaultdict(int)
for u, v, key in g.edges(keys=True):
    edge_counts[(u, v)] += 1

# Рисуем рёбра с параллельным смещением и выделением кратных
offset = 0.15
edge_drawn = defaultdict(int)

for u, v, key in g.edges(keys=True):
    count = edge_counts[(u, v)]
    n = edge_drawn[(u, v)]
    rad = -offset + (2 * offset) * n / max(1, count - 1) if count > 1 else 0
    color = "red" if count > 1 else "gray"  # красим кратные рёбра
    nx.draw_networkx_edges(
        g,
        pos,
        edgelist=[(u, v)],
        width=2,
        edge_color=color,
        connectionstyle=f"arc3,rad={rad}",
    )
    edge_drawn[(u, v)] += 1

plt.axis("off")
plt.show()
