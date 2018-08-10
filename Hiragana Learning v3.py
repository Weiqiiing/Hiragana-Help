import random
length = 5 #Change this for second 'program' length

def checkEnabled(check,find,mono):
        x=0
        if find in jap:x = 1
        print(check+"["+mono+"]",end=" ")
        print(("Enabled","Disabled")[x == 0])



jap = [
            #Monographs
            "あ","い","う","え","お",                #∅
            "か","き","く","け","こ",                #K
            "さ","し","す","せ","そ",                #S
            "た","ち","つ","て","と",                #T
            "な","に","ぬ","ね","の",                #N
            "は","ひ","ふ","へ","ほ",                #H
            "ま","み","む","め","も" ,                #M
            "や","ゆ","よ",                                 #Y
            "ら","り","る","れ","ろ",                 #R
            "わ","ゐ","ゑ","を",                         #W
            #Diacritics (Dakuten)
            "が","ぎ","ぐ","げ","ご",                #G
            "ざ","じ","ず","ぜ","ぞ",                #Z
            "だ","ぢ","づ","で","ど",                #D
            "ば","び","ぶ","べ","ぼ",                #B
            "ぱ","ぴ","ぷ","ぺ","ぽ"                 #P
            #Diagraphs
            "きょ","きゅ","きょ", 	                  #K
            "しゃ","しゅ","しょ", 	                  #S
            "ちゃ","ちゅ","ちょ", 	                  #C
            "にゃ","にゅ","にょ", 	                  #N
            "ひゃ","ひゅ","ひょ", 	                  #H
            "みゃ","みゅ","みょ", 	                  #M
            "りゃ","りゅ","りょ" 	                  #R
            


                                                       ]
#When choosing what hiragana you want to use, just add a # to the beginning of each line you want to disable.
#For example, to disable the M,Y and R Monographs, you would change the start of the lines to 

#            "や","ゆ","よ"                                 #Y
#            "ら","り","る","れ","ろ"                 #R
#            "わ","ゐ","ゑ","を"                         #W

#MAKE SURE TO ALSO DO THIS TO THE ENGLISH VERSION, ELSE IT WILL BE MIXED.
#I should have used a nested list to link each of them, but at the time of making this I didn't.
#Will update that in the future.


eng = [
             #Romanji
             "a","i","u","e","o",
             "ka","ki","ku","ke","ko",
             "sa","shi","su","se","so",
             "ta","chi","tsu","te","to",
             "na","ni","nu","ne","no",
             "ha","hi","fu","he","ho",
             "ma","mi","mu","me","mo",
             "ya","yu","yo",
             "ra","ri","ru","re","ro",
             "wa","wi","we","wo",
             #Diacritics (Dakuten)
             "ga","gi","gu","ge","go",
             "za","ji","zu","ze","zo",
             "da","dzi","dzu","de","do", #dzi and dzu, or di, and du - im not sure which are better to use rn. using dzi/dzu based on flashcards
             "ba","bi","bu","be","bo",
             "pa","pi","pu","pe","po"
             #Diagraphs
             "kya","kyu","kyo",
             "sha","shu","sho",
             "cha","chu","cho",
             "nya","nyu","nyo",
             "hya","hyu","hyo",
             "mya","myu","myo",
             "rya","ryu","ryo"


             
                                                        ]
program = input("""Choose Program\n\n
                            1. Write the Hiragana (Needs IME)\n
                            2. Decipher the Monographs (Set length at start of file)\n
                            3. Check what sets are enabled\n> """)
if program == "1":
    
    while True:
        guess = jap[random.randint(0,len(jap)-1)]
        q = input("Write the Hiragana for ["+ str( guess ) +"] : ")

        if q != guess:
            x = 0
            while q != guess:
                q = input(str(x)+": write the hiragana for ["+ str( guess ) +"] : ")
                x +=1


if program == "2":
            
    while True:
        japanese = ""
        english = ""
        for i in range(length):
            word = random.randint(0,len(jap)-1)
            japanese += jap[word]
            english += eng[word]
        print("",japanese)
        q = input("Please input the translation: ")
        q = q.replace(" ","")
        q = q.replace("-","")
            
        if q == english:
            print("correct!")
        else:
            print(english)
        print("\n\n")
if program == "3":
    checkthese = ["あ","か","さ","た","な","は","ま","や","ら","わ","が","ざ","だ","ば","ぱ","きょ","しゃ","ちゃ","にゃ","ひゃ","みゃ","りゃ"]
    letters = ["∅","K","S","T","N","H","M","Y","R","W","G","Z","D","B","P","K​","S​","C​","N​","H​","M​","R​"]
    monographs = [ "あ,い,う,え,お", "か,き,く,け,こ","さ,し,す,せ,そ",
                                "た,ち,つ,て,と", "な,に,ぬ,ね,の", "は,ひ,ふ,へ,ほ",                
                                "ま,み,む,め,も", "や,ゆ,よ", "ら,り,る,れ,ろ",
                                "わ,ゐ,ゑ,を",
                                #Diacritics
                                "が,ぎ,ぐ,げ,ご","ざ,じ,ず,ぜ,ぞ","だ,ぢ,づ,で,ど",
                                "ば,び,ぶ,べ,ぼ","ぱ,ぴ,ぷ,ぺ,ぽ"
                                #Diagraphs
                                "きょ,きゅ,きょ","しゃ,しゅ,しょ","ちゃ,ちゅ,ちょ",
                                "にゃ,にゅ,にょ","ひゃ,ひゅ,ひょ","みゃ,みゅ,みょ",
                                "りゃ,りゅ,りょ"

                   ]
    for i in range(len(checkthese)-1):
        checkEnabled(letters[i],checkthese[i],monographs[i])
        if letters[i]=="W":
            print("\nDiacritics")
        if letters[i] =="P":
            print("\nDiagraphs")
    

