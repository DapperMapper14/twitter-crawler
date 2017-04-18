import networkx as nx
import pandas as pd
import datetime as dt
import graph_stats as gs
import build_nw as bn
import matplotlib.pyplot as plt

jsonFile = "twitter-data/march-madness.json"
G = bn.twitter_graph(jsonFile)
date = bn.make_attr_dict1(jsonFile, "created_at")
for d in date.items():
	date[d[0]] = dt.datetime.strptime(d[1], "%a %b %d %H:%M:%S +0000 %Y")
nx.set_node_attributes(G, "date", date)

def active_time_series(G):
	# Set an "active" value to attribute dictionary
	active = {}
	for n in G.nodes():
		active[n] = False
	nx.set_node_attributes(G, "active", active)

	# Extract date values and create range over time series
	date = nx.get_node_attributes(G, "date")
	min_date = min(date.itervalues())
	max_date = max(date.itervalues())
	diff = abs((max_date-min_date).days)*24
	date_list = [max_date - dt.timedelta(hours=x) for x in range(0, diff)][::-1]

	# Loop over dates and the graph to count "active" nodes
	nodes = float(nx.number_of_nodes(G))
	count_nodes=[]
	for date in date_list:
		active_nodes=[]
		for (n, data) in G.nodes(data=True):
			try:
				if date > data["date"]:
					G.node[n]["active"]=True
					active_nodes.append(n)
				else:
					continue
			except:
				continue
		perc = float(len(active_nodes))/nodes
		count_nodes.append(perc)
	time_series = pd.DataFrame({"date": date_list,"count": count_nodes})
	return time_series

ts = active_time_series(G)

# MATPLOTLIB
ts.plot()
plt.title("#Samsung Activation Timeseries")
plt.xlabel("Days After Initial Tweet")
plt.ylabel("Fraction of Activated Users")
plt.grid(True)
plt.show()

# Create multiple dictionaries for setting node attributes
#nx.set_node_attributes(G, "date", date)
#rt = bn.make_attr_dict1(jsonFile, "retweet_count")
#followers = bn.make_attr_dict2(jsonFile, ["user", "follower_count"])
#location = bn.make_attr_dict2(jsonFile, ["user", "location"])
#friends = bn.make_attr_dict2(jsonFile, ["user", "friends_count"])
#favorites = bn.make_attr_dict2(jsonFile, ["user", "favourites_count"])

# Calculate several topology characteristics to add as attributs
#deg = G.degree()
#bc = nx.betweenness_centrality(G)
#dc = nx.degree_centrality(G)
#cc = nx.closeness_centrality(G)

#attr_list = [("date", date), ("retweet", rt), ("followers", followers), ("location", location),
#			("friends", friends), ("favorites", favorites), ("degree", deg), ("betweenness", bc), 
#			("degcent", dc), ("closeness", cc)]
#for a in attr_list:
#	nx.set_node_attributes(G, a[0], a[1])

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