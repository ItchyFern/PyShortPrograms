#-*-coding:utf8;-*-
#qpy:2
#qpy:console

# code made on QPython, i apologize for the simple names
# for everything, typing on the phone is terrible

# this program encodes using a pseudo random number generating
# algorithm that uses a user inputted seed code as a key

dict={"1":"a","2":"b","3":"c","4":"d",
      "5":"e","6":"f","7":"g","8":"h",
      "9":"i","10":"j","11":"k","12":"l",
      "13":"m","14":"n","15":"o","16":"p",
      "17":"q","18":"r","19":"s","20":"t",
      "21":"u","22":"v","23":"w","24":"x",
      "25":"y","26":"z","27":"A","28":"B",
      "29":"C","30":"D","31":"E","32":"F",
      "33":"G","34":"H","35":"I","36":"J",
      "37":"K","38":"L","39":"M","40":"N",
      "41":"O","42":"P","43":"Q","44":"R",
      "45":"S","46":"T","47":"U","48":"V",
      "49":"W","50":"X","51":"Y","52":"Z",
      "53":" ","54":"_","55":"1","56":"2",
      "57":"3","58":"4","59":"5","60":"6",
      "61":"7","62":"8","63":"9","64":"0",
      "65":"!","66":"@","67":"#","68":"$",
      "69":"%","70":"^","71":"&","72":"*",
      "73":"(","74":")","75":"+","76":"-",
      "77":"=","78":'"',"79":"'","80":"/",
      "81":">","82":"<","83":".","84":",",}

def bruh():
    x=[]
    for number, letter in dict.items():
        x.append (letter)

    return x

def checkInput (question, whitelist=[], blacklist=[]):
    while True:
        x=raw_input(question)
        if (x in whitelist) and not (x in blacklist):
            return x


def convertLetter(x):
    for number, letter in dict.items():
        if letter == x:
            return number

def convertNumber (x):
    return dict [str(x)]

def cryptionLetter (x,ret,codetype):
    if codetype=="encode":
        ret*=-1
    val=int (x)+int (ret)
    if val > len (dict):
        val=val-len (dict)
    elif val < 1:
        val=val+len (dict)
    return convertNumber (val)

def cryption (code, seed, codetype):
    x=0
    decipher=[]
    decipherlist=createPseudo (len(code),seed)
    for char in code:
        if char in letterlist:
            charnum=convertLetter(char)
        else:
            print ("Invalid character: %c (replaced with '_')" % char)
            charnum=convertLetter ('_')
        newchar=cryptionLetter(charnum, decipherlist [x], codetype)
        decipher.append(newchar)
        x+=1
    print (''.join (decipher))

def createPseudo (length,seed):
    pseudorand=[]
    count=0
    if int (seed )<10:
        seed="11"
    bot, top=findMid (len (seed))
    for x in range (length):
        seed=int (seed)*int (seed)
        combo=(seed%len (dict))
        mid=len(str (seed))/2
        pseudorand.append (combo)
        newseed=str (seed) [int(mid)-int(bot):int(mid)+int(top)]
        tmp=list (newseed)
        if tmp[0]=="0":
            tmp[0]="5"
            newseed="".join(tmp)
        seed=int (newseed)
        count+=1
    return pseudorand

def menu ():
    print ("1. Encode\n2. Decode")
    x=input ("Option: ")
    x=int (x)
    if x in {1,2}:
        code=input("Enter text: ")
        seed=input("Enter seed: ")
        if x==1:
            cryption(code, seed, "encode")
        elif x==2:
            cryption (code, seed, "decode")
    else:
        pass
    input("")

def findMid (length):
    x=length%2
    ret=length/2
    if x==0:
        return ret, ret
    elif x==1:
        return ret+1, ret

letterlist=bruh ()
menu ()
