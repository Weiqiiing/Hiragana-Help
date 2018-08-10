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
                                                       ]
#When choosing what hiragana you want to use, just add a # to the beginning of each line you want to disable.
#For example, to disable the M,Y and R Monographs, you would change the start of the lines to 

#            "や","ゆ","よ"                                 #Y
#            "ら","り","る","れ","ろ"                 #R
#            "わ","ゐ","ゑ","を"                         #W


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
             #Diacritics
             "ga","gi","gu","ge","go",
             "za","ji","zu","ze","zo",
             "da","dzi","dzu","de","do", #dzi and dzu, or di, and du - im not sure which are better to use rn. using dzi/dzu based on flashcards
             "ba","bi","bu","be","bo",
             "pa","pi","pu","pe","po"
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
        print("\n\n\n",japanese)
        q = input("Please input the translation: ")
        q = q.replace(" ","")
        q = q.replace("-","")
            
        if q == english:
            print("correct!")
        else:
            print(english)

if program == "3":
    checkthese = ["あ","か","さ","た","な","は","ま","や","ら","わ","が","ざ","だ","ば","ぱ"]
    letters = ["∅","K","S","T","N","H","M","Y","R","W","G","Z","D","B","P"]
    monographs = [ "あいうえお", "かきくけこ","さしすせそ",
                                "たちつてと", "なにぬねの", "はひふへほ",                
                                "まみむめも", "やゆよ", "らりるれろ",
                                "わゐゑを",
                                   #Diacritics
                                "がぎぐげご","ざじずぜぞ","だぢづでど",
                                "ばびぶべぼ","ぱぴぷぺぽ"                         ]

    for i in range(len(checkthese)):
        checkEnabled(letters[i],checkthese[i],monographs[i])
        if letters[i]=="W":
            print("\nDiacritics")
    

