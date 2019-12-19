import random
import sys

file='QuestionSheet.txt'
data=open(file, 'r')
question=[]
answer=[]
player={}
menu=["1. New Game", "2. Exit Game", "3. Help!"]


def readFile(): 
    flag=True
    qFlag=True
    x=0
    while(flag):
        line=data.readline() 
        #Check if file is out of questions        
        if line==None or line=='':
            flag=False
        #Check if line is a commented out line
        elif line.startswith("#"):
            x+=1
        else:
            #Append new question
            if qFlag:
                question.append(line[:len(line)-1])
                qFlag=False #switch question flag to false so you know its an answer next
            else:
                answer.append(line[:len(line)-1])
                qFlag=True #switch question flag to true so you know its a question next
            x+=1 #add one to count (so when calling a line to be read)


def initialize():
    readFile() #takes questions/answers from text and saves info
    
    
def setPlayers():
    print "How many players would you like in this game? (1-4)"
    while (True):
        num=raw_input("Players: ")
        if num in "1234":
            break
        else:
            print "Invalid choice, remember to choose a number between 1 and 4"
    print ""
    print "Set player name(s)"
    print ""    
    for x in range(int(num)): #Loop for amount of players
        print "Player %d:" % (x+1),
        x=raw_input("")
        player[x]=0 #set player name in dictionary and 0 as current score


def showHelp():
    print ""
    print " Help Menu"
    print ""
    print " Sorry, there really is no help yet..."
    print ""        

    
        
def showMenu():
    while (True):
        print ""
        print " Quiz Game"
        print ""
        for x in menu: #using menu 
            print x
        option=raw_input("Choice: ")
        if option in "123":
            break
        else:
            print "Invalid input, remember to choose a number between 1 and 3"
    if 1==int(option):
        playGame()
    elif 2==int(option):
        sys.exit()
    elif 3==int(option):
        showHelp()
        
        
def printScore():
    
    for x in player:
        print "%s: %d" % (x, player[x])
        
               
def setQuestions():
    print "How many questions would you like in this game?"
    print "(%d questions in the input file)" % (len(question))
    
    while (True):
        x=raw_input("Questions: ")        
        try:
            if int(x) in range(1,len(question)+1):
                break
        except:
            print "Invalid input, remember to choose a number between 1 and %d" % (len(question))
        else:
            print "Invalid number, remember to choose a number between 1 and %d" % (len(question))
    
    return int(x)    


def findWinner():
    temp=0
    ret=[]
    x=player.values()
    temp=max(x)
    for name, score in player.iteritems():
        if score == temp:
            ret.append(name)
    return ret
        
                   
def playGame():
    print ""
    print " Welcome to this Quiz Game!"
    print ""
    setPlayers()
    print ""
    numOfQuestions=setQuestions()
    
    usedQuestions=[]
    
    for x in range(numOfQuestions):
        while (True):
            num=random.randint(0,len(question)-1)
            if num not in usedQuestions:
                break
        usedQuestions.append(num)
        for y in player:
            print ""
            print "------------------------"
            print "Question %d:" % (x+1)
            print question[num]
            print ""
            ans=raw_input("%s: " % y)
            if str(ans).lower() == answer[num].lower():
                player[y]+=1
            
        print "------------------------"
        
    print "That's all of them! Let's see what the scores look like!"
    print ""
    printScore()
    print ""
    winner=findWinner()
    if len(winner)>1:
        print "Looks like we have a tie for %d points between:" % (player[winner[0]])
        for x in winner:
            print x
        
        print "Rock paper scissors tournament to see who wins! :D"
        
    else:
        print "Congratulations %s! You got %d points!" % (winner[0], player[winner[0]])
        print ""
    print "Would you like to see all the questions and answers? "
    x=raw_input("(y/n): ")
    if x.lower() == 'y':
        print ""
        print "------------------------"
        count=1
        for x in usedQuestions:
            print "Question %d" % (count)
            print question[x]
            print answer[x]
            print ""
            count+=1
     
     
                
     
            
                
	
        
        

    
            
    
initialize()
showMenu()
          

    








