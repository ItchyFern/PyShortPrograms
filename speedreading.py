import os
import time
import re

def getFile(loc):
    f = open(loc, "r")
    return f

def getText(f):
    text = f.read()
    text = text.replace("\n", " ")
    return text

def printWordArray(arr, delay = 0.3):
    quoteflag = False
    for word in arr:
        tdelay = delay

        # If the word length is 6 or more characters, increase delay by 10% for readability
        if len(word) >= 6:
            tdelay *= 1.1

        os.system("clear")
        
        # if quotes occur, put words in quotes, until quotes end
        # ex: the man said "hello kind sir" to me
        # the | man | said | " hello " | " kind " | " sir " | to | me
        if '"' in word:
            word = word.replace('"', "")
            quoteflag = not quoteflag
            word = '" {} "'.format(word)
        elif quoteflag:
            word = '" {} "'.format(word)

        print('{0:^20}'.format(word, 'centered'))

        # input ("")
        time.sleep(tdelay)

def getArray(text):
     return text.replace("-\n", "-").replace("\n", " ").replace("  ", " ").split()
    
def main():
    choice = input("Words per minute (avg = 200): ")
    delay = 60 / int(choice)
    
    loc = "/home/seth/speedread.txt"

    f = getFile(loc)
    text = getText(f)
    textarray = getArray(text)
    printWordArray(textarray, delay)
    


if __name__ == "__main__":
    main()
