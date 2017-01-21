import speech_recognition

recognizer = speech_recognition.Recognizer()

def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
		#return recognizer.recognize_sphinx(audio)
		return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		return("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""

print "Say something!"
test = 1
temp = listen()
while(temp == "Could not understand audio" and test == 1):
    print listen()
    test = input("Enter 1 to Try Again or enter 2 to stop")
    if (test == 1):
        print "Say something!"
        temp=listen()
        
    
print "I believe you said ",temp