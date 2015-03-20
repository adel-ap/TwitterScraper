#! /usr/bin/python
# -*- coding: utf-8 -*-


from BeautifulSoup import BeautifulSoup
from BeautifulSoup import NavigableString
from BeautifulSoup import Tag

def get_name_info(opener, username):
	page = opener.open('https://twitter.com/' + username)
	soup = BeautifulSoup(page)

	usr_name = soup.find('', {'class': 'u-linkComplex-target'}).next
	scr_name = soup.find('', {'class': 'u-textInheritColor'}).next

	return (usr_name, scr_name)

def tweet_to_str(tweet_contents):
	for i in range(len(tweet_contents)):
		if isinstance(tweet_contents[i], str):
			continue

		if isinstance(tweet_contents[i], NavigableString):
			tweet_contents[i] = str(tweet_contents[i])
		else:
			tweet_contents[i] = ' '.join(tweet_to_str(tweet_contents[i].contents))

	return tweet_contents

def get_tweets(opener, username):
	pass

def get_followings(opener, username):
	page = opener.open('https://twitter.com/' + username + '/following')
	soup = BeautifulSoup(page)

	followings = []
	usr_names = soup.findAll('', {'class': 'u-linkComplex-target'})
	scr_names = soup.findAll('', {'class': 'ProfileNameTruncated-link u-textInheritColor js-nav js-action-profile-name'})

	for i in range(len(scr_names) - 1):
		followings.append((usr_names[i + 2].next, scr_names[i + 1].next[7:-5]))

	return followings

def get_followers(opener, username):
	page = opener.open('https://twitter.com/' + username + '/followers')
	soup = BeautifulSoup(page)

	followings = []
	usr_names = soup.findAll('', {'class': 'u-linkComplex-target'})
	scr_names = soup.findAll('', {'class': 'ProfileNameTruncated-link u-textInheritColor js-nav js-action-profile-name'})

	for i in range(len(scr_names) - 1):
		followings.append((usr_names[i + 2].next, scr_names[i + 1].next[7:-5]))

	return followings
