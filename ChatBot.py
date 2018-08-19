# Gagandeep Nanda
import os
import random
import getpass
from gtts import gTTS
from pygame import mixer

# chat que and ans
greetings = ['hola', 'hello', 'hi','hey!','Hello','Hi']
questions = ['how are you?','how are you doing?','how life is going on?','how you doing?']
responses = ['I am good and you?','i am fine and you?']
validations = ['yes','yeah','yea','no','nah','good']
verifications = ['are you sure?','you sure?','you sure?','sure?',"sure?","really"]

CONVERSING = True

# conver the text and save it in MP3 format in temp folder and play it
def play(text_voice):
        username = getpass.getuser()
        play = gTTS(text_voice)
        r2 = random.randint(1,10000000)
        r1 = random.randint(1,10000000)
        name = "C:\\Users\\"+ username +"\\AppData\\Local\\Temp\\" + str(r2) + str(r1) +".mp3"
        play.save(name)
        mixer.init()
        mixer.music.load(name)
        mixer.music.play()

# search for the User input
while CONVERSING:
	userInput = raw_input(">>>Me: ")
	#usereInput = str(userInput)
	userInput = userInput.lower()
	if userInput in greetings:
		random_greeting = random.choice(greetings)
		play(random_greeting)
		print(">>>Python: " + random_greeting)
	elif userInput in questions:
		random_response = random.choice(responses)
		play(random_response)
		print(">>>Python: " + random_response)
	elif userInput in verifications:
		random_response = random.choice(validations)
		play(random_response)
		print(">>>Python: " + random_response)
	elif 'bye' in userInput:
 		random_response = "Bye take care !"
 		play(random_response)
 		print(">>>Python: " + random_response)
 		raw_input("Press enter to exit")
 		exit()
	else:
		response = "I am not able to understand you"
		play(response)
		print(">>>Python: " + response)
