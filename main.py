import microface
import faceidgenerate
import saveface
import searchface
import face_recognition_real
import sendNameByMMS
import time

face_recognition_real.activateCamera() #run face detection
url = face_recognition_real.getURLString() #get url of image obtained and uploaded on imgur

facearray = faceidgenerate.get_faceid(url) #get array of face ids

rowdetailsArrs = searchface.isInCSV(facearray) # serach faces in database and return and return values stored

if len(rowdetailsArrs) != 0:
	stringnames = ""
	for row in rowdetailsArrs:
		if len(rowdetailsArrs) != 1:
			stringnames += row[1] + ", "
		else:
			stringnames += row[1]
	if len(rowdetailsArrs) == 1:
		sendNameByMMS.sendText(url, stringnames + " is at your front door", "+17654045543")
	else:
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


    

