import json
import networkx as nx
import matplotlib.pyplot as plt
data=[]
G=nx.Graph()
names=[]
with open('american-healthcare.json') as tfile:
	for line in tfile:
		try:
			data.append(json.loads(line))
		except:
			continue
# generate user list and add nodes
for d in data:
	try:
		name=d['user']['id']
		if name not in names:
			names.append(name)
			G.add_node(name, size=1)
		else:
			size=G.node[name]['name']
			size+=5
			G.add_node(name,size=size)
	except:
		continue
# add edges between users and mentions
for d in data:
	try:
		name=d['user']['id']
		mentions=d['entities']['user_mentions']
		for m in mentions:
			if m['id'] in names:
				if not G.has_edge(name, m['id']):
					G.add_edge(name,m['id'],weight=5)
				else:
					weight=G[name][m['id']]['weight']
					weight+=5
					G.add_edge(name,m['id'],weight=weight)
	except:
		continue
G_largest = max(nx.connected_component_subgraphs(G), key=len)
nx.write_gexf(G_largest, "march-madness.gexf")
# nx.draw(G_largest)
# plt.show()
