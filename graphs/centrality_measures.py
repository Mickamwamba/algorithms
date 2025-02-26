import networkx as nx 
import matplotlib.pyplot as plt 
import os

parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
graph_folder = os.path.join(parent_dir, "graphs")

vertices = range(1,10)
edges = [(7,2), (2,3), (7,4), (4,5), (7,3), (7,5), (1,6),(1,7),(2,8),(2,9)]

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)

nx.draw(G,with_labels=True, node_color='y',node_size=800)
file_path = os.path.join(graph_folder, "graph1.png")
print(file_path)
plt.savefig(file_path)

# plt.show()
print(f"Centrality: {nx.degree_centrality(G)}")
print(f"Betweeness: {nx.betweenness_centrality(G)}")
print(f"Closeness: {nx.closeness_centrality(G)}")

centrality = nx.eigenvector_centrality(G)
print(f"Eigenvector: {nx.closeness_centrality(G)}")


