#! /urs/bin/pyhton

import urllib2
import threading

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

def analyse_users(ver2usr, ver2type, index, threads_num, flags):
	opener = setup_opener()

	i = index
	while flags[index]:
		if i >= len(ver2usr):
			continue

		tweets = funcs.get_tweets(opener, ver2usr[i])
		ver2type[i] = funcs.analyse_tweets(tweets)
		i += threads_num


def create_graph(opener, username, max_depth):
	##graph = [[]]
	edges = []

	usr_info = funcs.get_name_info(opener, username)
	usr2ver = {usr_info: 0}
	ver2usr = [str(usr_info[0])]
	ver2type = [None]
	bfs = [(usr_info, 0)]

	threads = []
	threads_num = 4
	flags = [True for i in range(threads_num)]
	for i in range(threads_num):
		threads.append(threading.Thread(None, analyse_users, (), (ver2usr, ver2type, i, threads_num, flags)))
		threads[-1].start()

	while len(bfs):
		user = bfs[0][0]
		depth = bfs[0][1]
		del bfs[0]

		if depth >= max_depth:
			continue


		followings = funcs.get_followings(opener, user[0])

		for f in followings:
			if not f in usr2ver:
				usr2ver[f] = len(usr2ver)
				ver2usr.append(str(f[0]))
				ver2type.append(None)
				##graph.append([])

			bfs.append((f, depth + 1))
			##graph[usr2ver[user]].append(usr2ver[f])
			edges.append((usr2ver[user], usr2ver[f]))


		followers  = funcs.get_followers(opener, user[0])

		for f in followers:
			if not f in usr2ver:
				usr2ver[f] = len(usr2ver)
				ver2usr.append(str(f[0]))
				ver2type.append(None)
				##graph.append([])

			bfs.append((f, depth + 1))
			##graph[usr2ver[f]].append(usr2ver[user])
			edges.append((usr2ver[f], usr2ver[user]))

		##print_graph(graph, ver2usr)
		#graph_drawer.draw(edges, ver2usr, [])


	while None in ver2type:
		continue

	for i in range(threads_num):
		flags[i] = False

	return edges, ver2usr, ver2type


def run_scraper(username, max_depth=2):
	opener = setup_opener()

	edges, ver2usr, ver2type = create_graph(opener, username, max_depth)
	for i in range(len(ver2type)):
		if ver2type[i]:
			ver2type[i] = 'blue'
		else:
			ver2type[i] = 'white'
	graph_drawer.draw(edges, ver2usr, ver2type)
