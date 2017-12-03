import networkx as nx
import community

borders = nx.Graph()
not_borders1 = nx.DiGraph()
# not_borders2 = nx.MultiDiGraph()

# clustering() 函数不能作用在有向图上
# nx.clustering(not_borders1) //wrong
nx.clustering(nx.Graph(not_borders1))


borders.add_node("Zimbabwe")
borders.add_nodes_from(["Lugandon", "Zambia", "Portugal", "Kuwait", "Colombia"])

borders.remove_node("Lugandon")
borders.add_edge("Zambia", "Zimbabwe")
borders.add_edges_from([("Uganda", "Rwanda"), ("Uganda", "Kenya"), ("Uganda", "South Sudan"),
                        ("Uganda", "Tanzania"), ("Uganda", "Democratic Republic of the Congo")])
# print(nx.clustering(borders))

# print(nx.clustering(borders, "Uganda"))

# print(list(nx.connected_components(borders)))

# 边属性
# borders["Germany"]["Poland"]["weight"] = 456.0

# 节点属性
# borders.node["Germany"]["area"] = 357168
# borders.add_node("Penguinia", area=14000000)

borders.nodes(data = True)

borders.edges(data = True)

# nx.find_cliques(not_borders1) //不能直接用于有向图
nx.find_cliques(nx.Graph(not_borders1)) # 转换为无向图才能正常运行
list(nx.find_cliques(borders))

nx.isolates(borders)

partition = community.best_partition(borders)
# print(partition)

community.modularity(partition, borders)