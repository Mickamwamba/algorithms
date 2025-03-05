import networkx as nx 
import matplotlib.pyplot as plt

vertices = range(1,10)
edges= [(7,2), (2,3), (7,4), (4,5), (7,3), (7,5), (1,6),(1,7),(2,8),(2,9)]

G = nx.Graph()

G.add_nodes_from(vertices)
G.add_edges_from(edges)
pos=nx.spring_layout(G)

# 1. Let's define the NF nodes:

nx.draw_networkx_nodes( G,pos,
nodelist=[1,4,3,8,9],
# with_labels=True,
node_color='g',
node_size=1300)

# 1. Now, let's create the nodes that are known to be involved in fraud:
nx.draw_networkx_nodes(G,pos,
nodelist=[2,5,6,7],
# with_labels=True,
node_color='r',
node_size=1300)

nx.draw_networkx_edges(G,pos,edges,width=3,alpha=0.5,edge_color='b') 
labels={}
labels[1]=r'1 NF'
nx.draw_networkx_labels(G,pos,labels,font_size=16)

plt.show()