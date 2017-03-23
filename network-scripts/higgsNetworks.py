# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:41:30 2017

@author: jonsull
"""

import networkx as nx

# Change these paths on your local computer
rtEdgeList = r"F:\Twitter Networks\higgs-retweet_network.edgelist\higgs-retweet_network.edgelist"
mtEdgeList = r"F:\Twitter Networks\higgs-mention_network.edgelist\higgs-mention_network.edgelist"
reEdgeList = r"F:\Twitter Networks\higgs-reply_network.edgelist\higgs-reply_network.edgelist"
snEdgeList = r"F:\Twitter Networks\higgs-social_network.edgelist\higgs-social_network.edgelist"

rwGraph = nx.read_edgelist(rtEdgeList, create_using= nx.DiGraph(), 
                           nodetype = int, data=(('weight',float),))
reGraph = nx.read_edgelist(reEdgeList, create_using= nx.DiGraph(), 
                           nodetype = int, data=(('weight',float),))
mtGraph = nx.read_edgelist(mtEdgeList, create_using= nx.DiGraph(), 
                           nodetype = int, data=(('weight',float),))
snGraph = nx.read_edgelist(snEdgeList, create_using=nx.DiGraph(), 
                           nodetype=int)


print nx.number_of_nodes(snGraph)