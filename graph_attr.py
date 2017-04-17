import networkx as nx
import graph_stats as gs
import build_nw as bn
import matplotlib.pyplot as plt

jsonFile = "twitter-data/samsung.json"
G = bn.twitter_graph(jsonFile)

# Create multiple dictionaries for setting node attributes
date = bn.make_attr_dict1(jsonFile, "created_at")
rt = bn.make_attr_dict1(jsonFile, "retweet_count")
followers = bn.make_attr_dict2(jsonFile, ["user", "follower_count"])
location = bn.make_attr_dict2(jsonFile, ["user", "location"])
friends = bn.make_attr_dict2(jsonFile, ["user", "friends_count"])
favorites = bn.make_attr_dict2(jsonFile, ["user", "favourites_count"])

# Calculate several topology characteristics to add as attributs
deg = G.degree()
bc = nx.betweenness_centrality(G)
dc = nx.degree_centrality(G)
cc = nx.closeness_centrality(G)

attr_list = [("date", date), ("retweet", rt), ("followers", followers), ("location", location),
			("friends", friends), ("favorites", favorites), ("degree", deg), ("betweenness", bc), 
			("degree_centrality", dc), ("closeness", cc)]
for a in attr_list:
	nx.set_node_attributes(G, a[0], a[1])

# Select largest subcomponent within graph
#Gc = max(nx.connected_component_subgraphs(G), key=len)

# Trim down graph to most important nodes based on centrality
#Gt = gs.most_important(Gc, "betweenness", 3)

# Create the layout
#pos = nx.spring_layout(Gc)
# draw the nodes and the edges (all)
#nx.draw_networkx_nodes(Gc,pos,node_color='b',alpha=0.2,node_size=8)
#nx.draw_networkx_edges(Gc,pos,alpha=0.1)

# draw the most important nprint json.loads(line)["created_at"]odes with a different style
#nx.draw_networkx_nodes(Gt,pos,node_color='r',alpha=0.4,node_size=254)
# also the labels this time
#nx.draw_networkx_labels(Gt,pos,font_size=12,font_color='b')
#plt.show()