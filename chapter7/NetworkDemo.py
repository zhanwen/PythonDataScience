import networkx as nx
import pandas as pd


#使用 networkx
borders = nx.Graph()
# # not_borders1 = nx.DiGraph()
# not_borders2 = nx.MultiDiGraph()

borders.add_node("Zimbabwe")
borders.add_nodes_from(["Lugandon", "Zambia", "Portugal", "Kuwait", "Colombia"])

borders.remove_node("Lugandon")
borders.add_edge("Zambia", "Zimbabwe")
borders.add_edges_from([("Uganda", "Rwanda"), ("Uganda", "Kenya"), ("Uganda", "South Sudan"),
                        ("Uganda", "Tanzania"), ("Uganda", "Democratic Republic of the Congo")])

# print(len(borders))

print(borders.nodes)
print(borders.node)
print(borders.edges)
print(borders.neighbors("Uganda"))
print(borders.degree("Uganda"))
print(borders.degree())

degrees = pd.DataFrame(list(borders.degree().items()), columns=("country", "degree")).set_index("country")
print(degrees.sort("degree").tail(5))

