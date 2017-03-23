# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:05:15 2017

@author: jonsull
"""

import networkx as nx
import os
import pickle
import matplotlib.pyplot as plt
from operator import itemgetter

# Function to load text file data into dictionary
def load_cached(file_name):
	f = open(file_name, 'rb')
	try:
		tweets_data = pickle.load(f)
	except:
		tweets_data = {}
	f.close()
	return tweets_data

# Function to turn retweet data in to a network graph
def networkIt(retweetDict):
    g = nx.Graph()
    userNames = retweetDict.keys()

    for u in userNames:
        retweeters = retweetData.get(u)["retweeters"]    
        g.add_node(u, retweets=len(retweeters), time=retweetData.get(u)["time"], 
                   tweet = retweetData.get(u)["text"])
    
        if retweeters:
            #print "Retweeted {0} times".format(len(retweeters))
            for r in retweeters:
                try:
                    if g.has_edge(u,r):  # Add additional weight to edge if edge exists
                        #print "Adding additional tweet to edge"
                        g[u][r]["weight"]+=1
                        
                    else: #create edge if it doesn't arleady exist
                        g.add_node(r)
                        g.add_edge(u,r, weight=1)
                except:
                    #print "Oops, not a valid retweet..."
                    pass
                
        else:
            #print "No retweeters"
            pass
        
    return g

# Apply the functions on your retweet data
retweetData = load_cached("C:\Users\jonsull\Box Sync\UM SNRE Classes\Network Analysis (SI 608)\Project\Scripts\Data\jonCached_031417.txt")
retweetGraph = networkIt(retweetData)
print "Your retweet graph has {0} nodes & {1} edges".format(len(retweetGraph.nodes()),
                                                            len(retweetGraph.edges()))
#os.chdir("Data")
#nx.write_pajek(retweetGraph, "repealReplace.net")

#size= nx.get_node_attributes(retweetGraph, "retweets")
#nx.draw_networkx(retweetGraph, nodelist=size.keys(), 
#                 node_size=[(v+1)*10 for v in size.values()])
#plt.show()

nd=sorted(retweetGraph.degree_iter(),key=itemgetter(1),reverse=True)[0:25]
print nd
#print "diameter: ",nx.diameter(retweetGraph)
print "density: ",nx.density(retweetGraph)

print "Number of cliques", len(list(nx.find_cliques(retweetGraph)))

dc = nx.degree_centrality(retweetGraph)


def topfive(centrality_rank):
    rank_sorted = sorted(centrality_rank.iteritems(),key=itemgetter(1),reverse=True) 
    for key,value in rank_sorted[0:5]:
        print "highest: ",key,value

print "top 5 by degree"
topfive(nx.degree_centrality(retweetGraph))

print "\n"

print "top 5 by betweenness"
topfive(nx.betweenness_centrality(retweetGraph))

print "\n"

print "top 5 by closeness"
topfive(nx.closeness_centrality(retweetGraph))

    