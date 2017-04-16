import json
import networkx as nx
import matplotlib.pyplot as plt
data=[]
G=nx.Graph()
names=[]
with open("twitter-data/march-madness-final.json") as tfile:
	for line in tfile:
		try:
			data.append(json.loads(line))
		except:
			continue
# generate user list and add nodes
for d in data:
	try:
		name=d["user"]["name"]
		if name not in names:
			names.append(name)
			G.add_node(name, size=1)
		else:
			size=G.node[name]["size"]
			size+=5
			G.add_node(name,size=size)
	except KeyError:
		continue
# add edges between users and mentions
for d in data:
	try:
		name=d["user"]["name"]
		mentions=d["entities"]["user_mentions"]
		for m in mentions:
			if m["name"] in names:
				if not G.has_edge(name, m["name"]):
					G.add_edge(name,m["name"],weight=5)
				else:
					weight=G[name][m["name"]]["weight"]
					weight+=5
					G.add_edge(name,m["name"],weight=weight)
	except KeyError:
		continue
nx.draw(G)
plt.show()
