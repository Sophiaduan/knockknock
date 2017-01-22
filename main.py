import microface
import faceidgenerate
import saveface
import searchface
import face_recognition_real
import sendNameByMMS
import time

<<<<<<< HEAD
try:
	face_recognition_real.activateCamera()
	url = face_recognition_real.getURLString()

	facearray = faceidgenerate.get_faceid(url)

	rowdetailsArrs = searchface.isInCSV(facearray)
	if len(rowdetailsArrs) != 0:
		stringnames = ""
		for row in rowdetailsArrs:
			if len(rowdetailsArrs) != 1:
				stringnames += row[1] + ", "
			else:
				stringnames += row[1]
		if len(rowdetailsArrs) == 1:
			sendNameByMMS.sendText(url, stringnames + " is at your front door. Should this person come in?", "+17654045543")
=======
face_recognition_real.activateCamera() #run face detection
url = face_recognition_real.getURLString() #get url of image obtained and uploaded on imgur

facearray = faceidgenerate.get_faceid(url) #get array of face ids

rowdetailsArrs = searchface.isInCSV(facearray) # serach faces in database and return and return values stored

if len(rowdetailsArrs) != 0:
	stringnames = ""
	for row in rowdetailsArrs:
		if len(rowdetailsArrs) != 1:
			stringnames += row[1] + ", "
>>>>>>> cf7fe704f0f74807adce364db22f6cb60d112f85
		else:
			sendNameByMMS.sendText(url, stringnames + " are at your front door. Should they come in?", "+17654045543")
		time.sleep(30)
	else:
<<<<<<< HEAD
		sendNameByMMS.sendText(url, "There is an unidentified person at your front door.  Should he/she come in?", "+17654045543")
		time.sleep(30)
		sendNameByMMS.sendSMS("Please enter the name of this person, or type no to ignore.", "+17654045543")
		time.sleep(30)
		with open("smsMessage.txt") as f:
		    f.readline()
		    content = f.readline().split(",")
		if (len(content) >= 1 and (content[0] != "no" and content[0] != "NO" and content[0] != "No")) :
			for i in range(len(content)):
				# print content
				# print facearray
				if (i < len(content) and i < len(facearray)):
					saveface.saveface(content[i], facearray[i])

except:
	print "it crashed"


		# if (len(facearray) >= 1):
		# 	for (int i = 0; i < facearray; i++) {
		# 		saveface.saveface(content[i], facearray[i])
		# 	}
		# 	saveface.saveface(content, facearray[0])
=======
		sendNameByMMS.sendText(url, stringnames + " are at your front door", "+17654045543")
else:
	sendNameByMMS.sendText(url, "There are unidentified people at your front door. Would you like to add a name", "+17654045543")
	time.sleep(40)
	with open("smsMessage.txt") as f:
	    f.readline()
	    content = f.readline()
	if (content != "NO") and (content != "No") and (content != "no") : #check is user does not want to store user in database
		##print facearray
		if (len(facearray) >= 1):
			saveface.saveface(content, facearray[0])
>>>>>>> cf7fe704f0f74807adce364db22f6cb60d112f85


    

