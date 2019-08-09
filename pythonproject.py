from time import sleep
import sys

def main():
    print("Welcome to my first application in python")
    sleep(1)
    print("Please make a selection below")
    sleep(1)
    print("1.)Encrypt some text and store it in a file")
    print("2.)Decrypt the data stored in the file")
    print("3.)Convert my speech to text and then text to speech")
    print("4.)Getting Bored...Let's play a game")
    print("5.)Exit the program")
    s=eval(input("Please make your selection:"))
    if s==1:
        Encryptmessage()
    elif s==2:
        Decryptmessage()
    elif s==3:
        sttts()
    elif s==4:
        game()
    elif s==5:
        sys.exit()
    else:
        print("U didnot choose from the valid options \nRestarting program")
        main()
        
import getpass
def getPassword():
    userPassword = ''
    attempts = 3
    counter = 0
    print("This application is password protected, you have 3 attempts at the password before the system exits")
    sleep(1)
    storedPassword = 'rajshree'
    userPassword = getpass.getpass('Enter password')
    if userPassword == storedPassword:
        main()
    else:
        while counter != 3:
            print('That was incorrect! You have ' + str(attempts-counter) + ' attempts left:')
            counter += 1
            userPassword = input('Enter password')
            if userPassword == storedPassword:
                main()
            if counter == 3:
                print('Unrecognized user')
                sleep(2)
                sys.exit()

def Encryptmessage():
    input1 = ''
    continue1 = 'yes'
    print("Any data entered here will be encrypted and written to a file")
    while continue1 == 'yes':
        prompt = input("Please enter what you want encrypted:")
        for i in range(0, len(prompt)):
            input1 = input1 + chr(ord(prompt[i]) - 2)
        efile = open('encryptedfile.txt','r+')
        efile.read()
        efile.write(input1+"\n")
        efile.close()
        continue1 = input("Would you like to input anything else(yes or no):")
        if continue1 == 'yes':
            Encryptmessage()
        elif continue1 == 'no':
            print(prompt)
            break
    continue1 = input("Would you like to continue the program(yes or no)")
    if continue1 == 'yes':
        main()
    else:
        sys.exit()

def Decryptmessage():
    output1=''
    dfile=open('encryptedfile.txt','r')
    for i in dfile:
        dfile.seek(0)
        readdata = dfile.read()
        for x in range(len(readdata)):
            output1 = output1 + chr(ord(readdata[x]) + 2)
    print(output1)
    dfile.close()
    continue1 = input("Would you like to continue the program(yes or no)")
    if continue1 == 'yes':
        main()
    else:
        sys.exit()
    
import speech_recognition as sr    
def sttts():
    txt=''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something')
        audio=r.listen(source)
        try:
            txt=r.recognize_google(audio)
            print('You had Spoken')
            print(txt)
        except:
            print("Sorry can't hear you!!!")
            sttts()
    from gtts import gTTS
    import os
    tts=gTTS(text=txt,lang='hi')
    tts.save('My_Audio3.mp3')
    os.system('mpg321 My_Audio3.mp3')
    os.system('start My_Audio3.mp3')
    continue1 = input("Would you like to continue the program(yes or no)")
    if continue1 == 'yes':
        main()
    else:
        sys.exit()

from random import *
def game():
    print('\n------------------GUESS THE NUMBER-----------------------\n')
    print("Let's see how much smart u r in guessing a number....\n")
    sleep(2)
    x=randint(1,100)
    d=''
    count=0
    while(True):
        d=int(input('Enter a number of your choice'))
        if d>x and 1<=(d-x)<=10:
            print("Your guess is high")
        elif d<x and 1<=(x-d)<=10:
            print("Your guess is low")
        elif (x-d)>10:
            print("Your guess is too low")
        elif (d-x)>10:
            print("Your guess is too high")
        else:
            print("You guessed right")
            break
        count+=1
    print("you were able to guess the number in %d attempts"%count)
    continue1 = input("Would you like to continue the program(yes or no)")
    if continue1 == 'yes':
        main()
    else:
        sys.exit()
getPassword()
