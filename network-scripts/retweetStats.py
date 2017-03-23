# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:29:02 2017

@author: jonsull
"""

import networkx as nx
from operator import itemgetter

g = nx.read_pajek("repealReplace_031417.net")

for node in g.nodes():
    print node," ",nx.degree(g,node)

print "diameter: ",nx.diameter(g)
print "density: ",nx.density(g)

list(nx.find_cliques(g))

dc = nx.degree_centrality(g)


def topfive(centrality_rank):
    rank_sorted = sorted(centrality_rank.iteritems(),key=itemgetter(1),reverse=True) 
    for key,value in rank_sorted[0:5]:
        print "highest: ",key,value

print "top 5 by degree"
topfive(nx.degree_centrality(g))

print "\n"

print "top 5 by betweenness"
topfive(nx.betweenness_centrality(g))

print "\n"

print "top 5 by closeness"
topfive(nx.closeness_centrality(g))