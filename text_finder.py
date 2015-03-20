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

a= "we are Mia San Mia fans"
text_finder(a)
def analyse_tweets(tweet):
        football_posts =  0
        for post in tweet:
                if text_finder(post) == True:
                        football_posts = football_posts + 1
                else:
                        pass
        if football_posts > 3:
                print "yeah"
        else:
                print "nope"

tweet = ["we are Mia_San_Mia fans" , "we are Falcao" , "Di Maria my life"
         , "we are Mata fans"]
analyse_tweets(tweet)
