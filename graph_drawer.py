#! /usr/bin/python

from igraph import *

def draw(edges, labels, colors):
	graph = Graph(edges=edges, directed=True)

	graph.vs["label"] = labels
	#graph.vs["color"] = colors

	plot(graph, bbox=(1000, 1000), margin=100)
