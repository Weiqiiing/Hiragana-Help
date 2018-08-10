from random import randint


def checkEnabled(check,find,mono):
        x=0
        for i in PLAYWITH:
                if find == i[0]:
                        x = 1
                        break


        print(check+"  ["+mono+"]",end=" ")
        print(("✓ Enabled","✕ Disabled")[x == 0])

##Required Lists Start
monograph = [
["あ","a"],["い","i"],["う","u"],["え","e"],["お","o"],                      #∅
["か","ka"],["き","ki"],["く","ku"],["け","ke"],["こ","ko"],  	    #K
["さ","sa"],["し","shi"],["す","su"],["せ","se"],["そ","so"], 	    #S
["た","ta"],["ち","chi"],["つ","tsu"],["て","te"],["と","to"],  	    #T
["な","na"],["に","ni"],["ぬ","nu"],["ね","ne"],["の","no"],  	    #N 
["は","ha"],["ひ","hi"],["ふ","fu"],["へ","he"],["ほ","ho"],   	    #H 
["ま","ma"],["み","mi"],["む","mu"],["め","me"],["も","mo"],      #M 
["や","ya"],["ゆ","yu"],["よ","yo"],                      		    #Y
["ら","ra"],["り","ri"],["る","ru"],["れ","re"],["ろ","ro"],  	    #R
["わ","wa"],["ゐ","wi"],["ゑ","we"],["を","wo"]            	    #W 
]

diacritic = [ #Monographs & Dakuten
["が","ga"],["ぎ","gi"],["ぐ","gu"],["げ","ge"],["ご","go"],               #G
["ざ","za"],["じ","ji"],["ず","zu"],["ぜ","ze"],["ぞ","zo"],                  #Z
["だ","da"],["ぢ","dzi"],["づ","dzu"],["で","de"],["ど","do"],           #D, dzi and dzu can be considered ji and zu 
["ば","ba"],["び","bi"],["ぶ","bu"],["べ","be"],["ぼ","bo"],              #B
["ぱ","pa"],["ぴ","pi"],["ぷ","pu"],["ぺ","pe"],["ぽ","po"]       #P
]

digraph = [ 
["きゃ","kya"],["きゅ","kyu"],["きょ","kyo"],         
["しゃ","sha"],["しゅ","shu"],["しょ","sho"],         
["ちゃ","cha"],["ちゅ","chu"],["ちょ","cho"],         
["にゃ","nya"],["にゅ","nyu"],["にょ","nyo"],         
["ひゃ","hya"],["ひゅ","hyu"],["ひょ","hyo"],         
["みゃ","mya"],["みゅ","myu"],["みょ","myo"],     
["りゃ","rya"],["りゅ","ryu"],["りょ","ryo"]            
]

digrdiac = [ #Digraphs & Diacritics
["ぎゃ","gya"],["ぎゅ","gyu"],["ぎょ","gyo"],
["じゃ","zya"],["じゅ","zyu"],["じょ","zyo"], #can be considered as ja, ju and jo
["ぢゃ","dya"],["ぢゅ","dyu"],["ぢょ","dyo"], #can also be considered as, ja, ju and jo
["びゃ","bya"],["びゅ","byu"],["びょ","byo"],
["ぴゃ","pya"],["ぴゅ","pyu"],["ぴょ","pyo"],
]
PLAYWITH = monograph+diacritic+digraph+digrdiac
##Remove things from here to not have them in play
##you can also comment out lines within each list using # to disable them 
LENGTH = 5
##You can change how many characters appear in game 2 changing this.

###Required Stuff End

program = input("""Choose Program\n\n
                            1. Write the Hiragana (Needs IME)\n
                            2. Decipher the Monographs (Set length at start of file)\n
                            3. Check what characters are enabled\n
                            4. Instructions for each Program\n> """)
#simple game
if program == "1":
    while True:
        guess = PLAYWITH[randint(0,len(PLAYWITH)-1)]
        q = input("Write the Hiragana for ["+ str( guess[0] ) +"] : ")
 
        if q != guess[0]:
            x = 1
            while q != guess[0]:
                q = input(str(x)+": Write the Hiragana for ["+ str( guess[0] ) +"] : ")
                x +=1

#decode
if program == "2":
    while True:
        jap=""
        eng=""
        for i in range(LENGTH):
            number = randint(0,len(PLAYWITH)-1)
            jap += (PLAYWITH[number][0])
            eng += (PLAYWITH[number][1])

        q = input(jap+"\nPlease input the translation: ")
        q = q.replace(" ","")
        q = q.replace("-","")
        
        if q == eng:
            print("correct!")
        else:
            print(eng)
        print("\n\n")

if program == "3":
    checkthese = ["あ","か","さ","た","な","は","ま","や","ら","わ","が","ざ","だ","ば","ぱ","きょ","しゃ","ちゃ","にゃ","ひゃ","みゃ","りゃ","ぎゃ","じゃ","ぢゃ","びゃ","ぴゃ"]
    letters = ["∅","K","S","T","N","H","M","Y","R","W","G","Z","D","B","P","K​","S​","C​","N​","H​","M​","R​","G","Z","D","B","P​​"]
    monographs = [ "あ,い,う,え,お", "か,き,く,け,こ","さ,し,す,せ,そ",
                                "た,ち,つ,て,と", "な,に,ぬ,ね,の", "は,ひ,ふ,へ,ほ",                
                                "ま,み,む,め,も", "や,ゆ,よ", "ら,り,る,れ,ろ",
                                "わ,ゐ,ゑ,を",
                                #Diacritics
                                "が,ぎ,ぐ,げ,ご","ざ,じ,ず,ぜ,ぞ","だ,ぢ,づ,で,ど",
                                "ば,び,ぶ,べ,ぼ","ぱ,ぴ,ぷ,ぺ,ぽ",
                                #Digraphs
                                "きょ,きゅ,きょ","しゃ,しゅ,しょ","ちゃ,ちゅ,ちょ",
                                "にゃ,にゅ,にょ","ひゃ,ひゅ,ひょ","みゃ,みゅ,みょ",
                                "りゃ,りゅ,りょ",
                                #Digraphs and Diacritics
                                "ぎゃ,ぎゅ,ぎょ","じゃ,じゅ,じょ","ぢゃ,ぢゅ,ぢょ",
                                "びゃ,びゅ,びょ","ぴゃ,ぴゅ,ぴょ"
                                                                          ]
    for i in range(len(checkthese)):
        checkEnabled(letters[i],checkthese[i],monographs[i])
        if letters[i]=="W":
            print("\nDiacritics")
        if letters[i] =="P":
            print("\nDiagraphs")
        if letters[i] =="R​":
            print("\nDigraphs and Diacritics")

        
#instructions
if program == "4":
    print("""1. Write the Hiragana -
        Set your computers writing to the Japanese IME.
        Using [WIN+SPACE] you can quickly change between your keyboard languages.
        Using [ALT+`] you can change your IME between Hiragana and Half-width alphanumeric.

        For this minigame, you will need to copy the hiragana in the bracket. For example, if you saw
        "Write the Hiragana for ["ひ"] :"
        You need to figure out what ひ is. The romanji for [ひ] in this case is "hi".
        So all you need to do, with the Japanese IME and Hiragana selected, type the answer
        (in this case it is "hi") and click enter twice!""")

    print("""\n2. Decipher the Monographs -
        For this game you will be typing out the romanji of the Hiragana shown on screen.
        Using a standard (Non-IME) keyboard you need to try convert the nonsensical word to be correct. 
        Example:
              "ちはすゆへ
                Please input the translation:"

            The translation is chi-ha-su-yu-he, and it could be inputted in three ways.
            
            1. No spaces [chihasuyuhe]
            2. Spaces [chi ha su yu he]
            3. Dashes [chi-ha-su-yu-he]

            Restart the program and pick a game!""")
        
