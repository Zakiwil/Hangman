from turtle import *
from random import randint
import time
import math

wordList = ['abate', 'zaki is amazing','xylophage', 'blandishment','abdicate','abduct',\
            'boisterous', 'dawdle', 'discursive', 'nebulous', 'pungent',\
            'Adversarial', 'Demur',  'Irreconcilable', 'Surmount',\
            'Validate', 'Sparingly', 'Ramify', 'Nuance', 'Freewheeling',\
            'Egregious', 'Dire']
sw = 600
sh = 900
s=getscreen()
s.setup(sw, sh)
s.bgcolor('#4286f4')
t1=getturtle()
t1.speed(0)
faceC1 = -100
faceC2 = 3
faceC3 = -130
faceC4 = 3
t1.hideturtle()

tWriter = Turtle()
tWriter.hideturtle()

tBL = Turtle()
tBL.hideturtle()



# variables to play the game
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
LettersWrong =""
LettersCorrect = ""
secretWord= ""
displayword= ""
fails = 6
fontS = int(sh*0.03)
gameDone = False



#My Defs
def chooseSecretWord():
    global secretWord
    secretWord = wordList[randint(0,len(wordList)-1)]
    print("The secret word is " + secretWord)

def displayText(newText):
    tWriter.clear()
    tWriter.penup()
    tWriter.goto(-int(sw*0.4), -int(sh*0.4))
    tWriter.write( newText, font=("Arial", fontS, "bold"))

def displayBadLetters(newText):
    tBL.clear()
    tBL.penup()
    tBL.goto(-int(sw*0.4), int(sh*0.4))
    tBL.write( newText, font=("Arial", fontS, "bold"))

def makeWordString():
    global displayword, alpha
    displayword = ""
    for l in secretWord:
        if str(l) in alpha:
            if str(l).lower() in LettersCorrect.lower():
                displayword += str(l) + " "
            else:
                displayword += "_" + " "
        else:
            displayword += str(l) + " "

    print(displayword)

def getGuess():
    boxTitle="Letters Used: " + LettersWrong
    guess = s.textinput(boxTitle, "Enter a Guess type $$ to Guess the word")
    return guess

def updateHangman():
    global fails
    if fails == 5:
        drawHead()
    if fails == 4:
        drawTorso()
    if fails == 3:
        drawRLeg()
    if fails == 2:
        drawLleg()
    if fails == 1:
        drawRarm()
    if fails == 0:
        drawFace()

def checkWordGuess():
    global fails, gameDone
    boxTitle="Word Guess"
    guess = s.textinput(boxTitle, "Guess the word")
    if guess == secretWord:
        displayText("YES!!! the word is " + secretWord)
        gameDone = True
    else:
        displayText("No the word is not: " + guess)
        time.sleep(1)
        displayText(displayword)
        fails -=1
        updateHangman()

def restartGame():
    global fails, LettersCorrect, LettersWrong, gameDone
    boxTitle="Want to play again?"
    guess = s.textinput(boxTitle, "Type y/yes to play again")
    if guess.lower == 'y' or guess.lower() == 'yes':
        LettersCorrect = ""
        LettersWrong = ""
        t1.left(45)
        t1.clear()
        drawg()
        chooseSecretWord()
        displayText("Guess a Letter...")
        displayBadLetters("Not in word: [" + LettersWrong + "]")
        time.sleep(1)
        makeWordString()
        displayText(displayword)
        fails =6
        gameDone = False
    else:
        displayBadLetters("Ok, see you later!")

def playGame():
    global gameDone, fails, alpha, LettersCorrect, LettersWrong
    while gameDone == False and fails > 0:
        theGuess = getGuess()
        if theGuess == "$$":
            print("Let them guess word")
            checkWordGuess()
        elif len(theGuess) > 1 or theGuess =="":
                displayText("Sorry I need a letter, guess again")
                time.sleep(1)
                displayText(displayword)
        elif theGuess not in alpha:
            displayText(theGuess + " is not a letter, guess again")
            time.sleep(1)
            displayText(displayword)
        elif theGuess.lower() in secretWord.lower():
            LettersCorrect += theGuess.lower()
            makeWordString()
            displayText(displayword)
        else:
            if theGuess.lower() not in LettersWrong:
                LettersWrong += theGuess.lower() + ", "
                fails -= 1
                displayText(theGuess + " is not in the word")
                time.sleep(1)
                updateHangman()
                displayText(displayword)
                displayBadLetters("Not in word: [" + LettersWrong + "]")
            else:
                displayText(theGuess + " word already guesed. ")
                time.sleep(1)
                displayText(displayword)

        if "_" not in displayword:
            displayText("Yess!!! You Won the word was: " + secretWord)
            gameDone = True

        if fails <=0:
            displayText("Out of guesses the word was: " + secretWord)
            gameDone = True
        if gameDone == True:
            restartGame()

    
def drawg():
    t1.goto(0,0)
    t1.width(7)
    t1.color('black')
    t1.penup()
    t1.goto(-int(sw/4), -int(sh/4) )
    t1.pendown()
    t1.forward(int(sw/2))
    t1.forward(-int(sw/4))
    t1.left(90)
    t1.forward(int(sw/2))
    t1.left(90)
    t1.forward(int(sw/5))
    t1.left(90)
    t1.forward(int(sw/16))


def drawHead():
    headr = sw/15
    t1.penup()
    t1.goto(t1.xcor() -headr, t1.ycor()-headr)
    t1.pendown()
    t1.circle(headr)
    t1.penup()
    t1.goto(t1.xcor() +headr, t1.ycor()-headr)
    t1.pendown()

def drawTorso():
    t1.forward(int(sh*0.10))

def drawRLeg():
    t1.left(45)
    t1.forward(int(sw/10))
    t1.left(180)
    t1.forward(int(sw/10))

def drawLleg():
    t1.left(90)
    t1.forward(int(sw/10))
    t1.left(180)
    t1.forward(int(sw/10))
    t1.left(45)

def drawRarm():
    t1.forward(int(sw/11))
    t1.left(45)
    t1.forward(int(sw/10))
    t1.left(180)
    t1.forward(int(sw/10))
    t1.left(90)
    t1.forward(int(sw/10))

def drawFace(): 
    facer = sw/100
    t1.penup()
    t1.goto(faceC1, faceC2)
    t1.pendown()
    t1.circle(facer)
    t1.penup()
    t1.goto(t1.xcor() +facer, t1.ycor()-facer)
    t1.pendown()
    t1.penup()
    t1.goto(faceC3, faceC4)
    t1.pendown()
    t1.circle(facer)
    t1.penup()
    t1.goto(t1.xcor() +facer, t1.ycor()-facer)
    t1.pendown()  
    t1.penup()
    t1.goto(faceC1 - 20 ,faceC2 - 20)
    t1.pendown()
    t1.circle(10,-90)   #right smile
    t1.penup()



drawg()
drawHead()
drawTorso()
drawRLeg()
drawLleg()
drawRarm()
drawFace()
t1.left(45)

time.sleep(1)
t1.clear()
drawg()
chooseSecretWord()
displayText("Guess a Letter...")
displayBadLetters("Not in word: [" + LettersWrong + "]")

time.sleep(1)
makeWordString()
displayText(displayword)
playGame()
