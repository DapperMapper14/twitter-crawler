import collections
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

def topfive(centrality_rank):
    rank_sorted = sorted(centrality_rank.iteritems(),key=itemgetter(1),reverse=True) 
    for key,value in rank_sorted[0:5]:
        print "highest: ",key,value

def most_important(G, centralityMeasure="betweenness", cutoff=3):
	if centralityMeasure == "betweenness":
		ranking = nx.betweenness_centrality(G).items()
	elif centralityMeasure == "closeness":
		ranking = nx.closeness_centrality(G).items()
	elif centralityMeasure == "degree":
		ranking = nx.degree_centrality(G).items()
	else:
		raise "Invalid centrality measure. str type of 'betweenness', 'closeness', or 'degree'"
	r = [x[1] for x in ranking]
	m = sum(r)/len(r) # mean centrality
	t = m*cutoff # threshold, we keep only the nodes with 3 times the mean
	Gt = G.copy()
	for k, v in ranking:
		if v < t:
			Gt.remove_node(k)
	return Gt

def plot_degree_distribution (g, plotTitle, oName):
	degs = {}
	for n in g.nodes():
		deg = g.degree(n)
		if deg not in degs:
			degs[deg] = 0
		degs[deg] += 1
	
	items = sorted (degs.items())
	items = sorted (degs.items())
	fig = plt.figure()
	ax = fig.add_subplot (111)
	ax.plot ([ k for (k , v) in items] , [v for (k ,v) in items])
	ax.set_xscale ('log')
	ax.set_yscale ('log')
	plt.title (plotTitle)
	fig.savefig (oName)