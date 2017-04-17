import json
import networkx as nx

def twitter_graph(twitterJSON, G=nx.Graph()):
	data=[]
	names=[]
	with open(twitterJSON) as tfile:
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
	return G

def make_attr_dict1(twitterJSON, attr_list):
	d={}
	with open(twitterJSON) as tfile:
		for line in tfile: #loop over each entry in json
			try:
				py_obj=json.loads(line)
				name=py_obj["user"]["name"]
			except:
				continue
			for a in attr_list:
				try:
					d[name] = py_obj[a]
				except:
					continue
	return d

def make_attr_dict2(twitterJSON, attr_list):
	d={}
	with open(twitterJSON) as tfile:
		for line in tfile: #loop over each entry in json
			try:
				py_obj=json.loads(line)
				name=py_obj["user"]["name"]
			except:
				continue
			for a in attr_list:
				try:
					d[name] = py_obj[a[0]][a[1]]
				except:
					continue
	return d