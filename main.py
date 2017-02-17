import microface
import faceidgenerate
import saveface
import searchface
import face_recognition_real
import sendNameByMMS
import time

try:
	PHONENO = "34554045671+"
	PHONENO = PHONENO[::-1]
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
			sendNameByMMS.sendText(url, stringnames + " is at your front door. Should this person come in?", PHONENO)
		else:
			sendNameByMMS.sendText(url, stringnames + " are at your front door. Should they come in?", PHONENO)
		time.sleep(30)
	else:
		sendNameByMMS.sendText(url, "There is an unidentified person at your front door.  Should he/she come in?", PHONENO)
		time.sleep(30)
		sendNameByMMS.sendSMS("Please enter the name of this person, or type no to ignore.", PHONENO)
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


    

