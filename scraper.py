#! /urs/bin/pyhton

import urllib2

import funcs
import graph_drawer

def get_cookie():
	return 'auth_token=2f8aa9cd05956234a428cf281c10e53ced90504f'

def setup_opener():
	proxy = urllib2.ProxyHandler({'https': '127.0.0.1:8580'})
	opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)

	opener.addheaders.append(('Cookie', get_cookie()))

	return opener


def print_graph(graph, ver2usr):
	print '-' * 100
	for i in range(len(graph)):
		print ver2usr[i], '\t', graph[i]
	print '-' * 100

def create_graph(opener, username, max_depth):
	pass


def run_scraper(username, max_depth=2):
	baseurl = "https://twitter.com/"

	opener = setup_opener()

	edges, ver2usr = create_graph(opener, username, max_depth)
	graph_drawer.draw(edges, ver2usr, [])
