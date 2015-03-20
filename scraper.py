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
	##graph = [[]]
	edges = []

	usr_info = funcs.get_name_info(opener, username)
	usr2ver = {usr_info: 0}
	ver2usr = [str(usr_info[0])]
	bfs = [(usr_info, 0)]

	while len(bfs):
		user = bfs[0][0]
		depth = bfs[0][1]
		del bfs[0]

		if depth >= max_depth:
			continue


		followings = funcs.get_followings(opener, user[0])
		followers  = funcs.get_followers(opener, user[0])

		for f in followings:
			if not f in usr2ver:
				usr2ver[f] = len(usr2ver)
				ver2usr.append(str(f[0]))
				##graph.append([])

			bfs.append((f, depth + 1))
			##graph[usr2ver[user]].append(usr2ver[f])
			edges.append((usr2ver[user], usr2ver[f]))

		for f in followers:
			if not f in usr2ver:
				usr2ver[f] = len(usr2ver)
				ver2usr.append(str(f[0]))
				##graph.append([])

			bfs.append((f, depth + 1))
			##graph[usr2ver[f]].append(usr2ver[user])
			edges.append((usr2ver[f], usr2ver[user]))

		##print_graph(graph, ver2usr)
		#graph_drawer.draw(edges, ver2usr, [])


	return edges, ver2usr


def run_scraper(username, max_depth=2):
	baseurl = "https://twitter.com/"

	opener = setup_opener()

	edges, ver2usr = create_graph(opener, username, max_depth)
	graph_drawer.draw(edges, ver2usr, [])
