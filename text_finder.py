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
                   , "Tevez" , "Pogba" , "vidal" , "Podolski" , "Ikardi" ,
                   "Red Devil" , "Mia San Mia" , "You'll never walk alone" ,
                   "Pride of London" , "Gunners" , "Noisy Neighburs" ,
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
                print "Blue"
                counter = counter + 1
                break
            elif word in fw[i]:
                if t[ind] and t[ind + 1] in fw[i]:
                    print "Blue"
                    counter = counter + 1
    if counter == 0:
        print "white"

a= "we are Mata fans"
text_finder(a)
