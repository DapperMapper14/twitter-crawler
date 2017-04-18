import networkx as nx
import datetime as dt

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
	count_nodes=[]
	for date in date_list:
		active_nodes=[]
		for (n, data) in G.nodes(data=True):
			if date > data["date"]:
				G.node[n]["active"]=True
				active_nodes.append(n)
			else:
				continue
		count_nodes.append(len(active_nodes))

	time_series = pd.DataFrame({"date": date_list,"count": count_nodes})
	return time_series
