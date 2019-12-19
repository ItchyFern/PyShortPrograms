correct=0
incorrect=0





print ("Welcome to our quiz program!")
print ("")
print ("To start, please press enter.")
input ("")

#####QUESTION 1#####
print ("Question 1: How many hours are in a day?")
print ("")
ans=input ("Answer: ")
print("")
#Test if the players input is equal to 24, then print out the corresponding statement if itstoiasfouysgfh]
if (int (ans)==24):
    print ("Correct!")
    correct+=1
else:
    print ("You disappoint me...")
    incorrect+=1

print ("")

#####QUESTION 2#####
print ("Question 2: What is a cat?")
print ("")
ans=input ("Answer: An ")
print("")

if (ans.lower()=="animal"):
    print ("Correct!")
    correct+=1
else:
    print ("You really gotta get your shit figured out bro.")
    incorrect+=1

print ("")

#####QUESTION 3#####
print ("Question 3: You are my sunshine, my only ______?")
print ("")
ans=input ("Answer: ")
print("")

if (ans.lower()=="sunshine"):
    print ("Correct!")
    correct+=1
else:
    print ("Okay, this one might have been a little harder...")
    incorrect+=1

print ("")
print ("~~~YOUR SCORES!~~~")
print ("Correct: " + str(correct))
print ("Incorrect: " + str(incorrect))

if (correct>1):
   print("You are smart!")
else:
   print("you suck!")
