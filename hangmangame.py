def main():
    word="telephone"
    guessedletters=""
    usrinput=""
    errors=[]
    maxattempts=6
    while(True):
        while(True):
            usrinput = input("Guess a Letter: ")
            if (len(usrinput.strip()) < 2):
                break
            else:
                print("Only one letter.")

        guessedletters+=usrinput.lower()

        if usrinput.lower() in word:
            print ("Your letter", usrinput.lower(), "was found!")
        else:
            print ("Your letter", usrinput.lower(), "wasn't found.")
            errors.append(usrinput.lower())

        printHangman(len(errors))
        printWord(word, guessedletters)

        if checkSuccess(word, guessedletters):
            break
        elif checkFail(errors, maxattempts, word):
            break
        else:
            print("Guessed letters: {}".format(", ".join(guessedletters)))

def checkFail(errors, maxattempts, word):
    if len(errors) >= maxattempts:
        print ("You've exhausted your attempts. The word was {}".format(word))
        return True
    return False


def checkSuccess(word, guessedletters):
    retflag = True
    for letter in word:
        if letter not in guessedletters:
            return False

    print("Success!")
    return True



def printWord(word, guessedletters):
    for letter in word:
        if letter in guessedletters:
            print(letter, end="")
        else:
            print("*", end="")
    print("")

def printHangman(errors):
    print("   _____   ")
    print("  |     |   ")
    if errors > 0:
        print("  |     O   ")
    else:
        print("  |        ")

    if errors > 3:
        print(r"  |    /|\   ")
    elif errors > 2:
        print("  |    /|   ")
    elif errors > 1:
        print("  |     |   ")
    else:
        print("  |        ")

    if errors > 5:
        print(r"  |    / \   ")

    elif errors > 4:
        print("  |    /   ")
    else:
        print("  |        ")

    print("__|__   ")
    print("")

if __name__ == "__main__":
    main()
