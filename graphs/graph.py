import networkx as nx 

G = nx.Graph()

G.add_node("Michael")
G.add_nodes_from(["Dina","Ben","Mussa","Yuda"])

G.add_edge("Michael","Dina")
G.add_edge("Mussa","Nadia")
print(list(G.nodes))
print(list(G.edges))
