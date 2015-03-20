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
football_words = ["manchester united" , "man utd" , "man city" , "chelsea"
                  ,"arsenal" , "liverpool" , "F.C barcelona" , "real madrid" ,
                   "bayern munich","B.V.B" , "jueventus" , "A.C milan" ,
                   "inter milan" , "Rooney" , "Van Persie" , "Mata" , "De Gea"
                   , "Falcao" , "Di Maria" , "aguero" , "Toure" , "Nasri" ,
                   "Silva" , "Costa", "Fabregas" , "Lampard" ,"Terry","Welbeck"
                   "Ozil" , "Giroud" , "Sterling" , "sturidge" , "Neymar" ,
                   "messy" , "Suarez" , "Pique" , "Iniesta" , "Ronaldo" , "Bale"
                   , "Benzema" , "Casillas" , "Pepe" , "Robben" , "mueller" ,
                   "Ribery" , "Gotze" , "Neuer" , "Hummels" , "Reus" , "Kagawa"
                   , "Tevez" , "Pogba" , "vidal" , "Podolski" , "Icardi" ,
                   "Red Devil" , "Mia_San_Mia" , "You'll_never_walk_alone" ,
                   "Pride_of_London" , "Gunners" , "Noisy Neighburs" ,
                   "La Decima" , "Tici Taca" , "Cantona" , "CR7" , "6 taii"  ]


def word_spliter(x):
    fw = []
    for word in x:
         s = word.split()
         fw.append(s)
    return fw
fw = word_spliter(football_words)
l = len(fw)

def text_finder(text):
    counter = 0
    t = text.split()
    for word in t :
        ind = t.index(word)
        for i in range(l):
            if word in football_words:
                counter = counter + 1
                return True
            elif word in fw[i]:
                if t[ind] and t[ind + 1] in fw[i]:
                    counter = counter + 1
                    return True
    if counter == 0:
        return False

def analyse_tweets(tweet):
        football_posts =  0
        for post in tweet:
                if text_finder(post) == True:
                        football_posts = football_posts + 1
                else:
                        pass
        if football_posts > 3:
                return True
        else:
                return False
                        
def get_tweets(opener, username):
        page = opener.open('https://twitter.com/' + username)
        soup = BeautifulSoup(page)

        tweets = soup.findAll('p', {'class': 'ProfileTweet-text js-tweet-text u-dir'})
        for i in range(len(tweets)):
                s = tweets[i].contents
                tweets[i] = ''.join(tweet_to_str(tweets[i].contents))

        return tweets

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
