import microface
import faceidgenerate
import saveface
import searchface
import face_recognition_real
import sendNameByMMS
import time

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
		sendNameByMMS.sendText(url, stringnames + " is at your front door", "+17654045543")
	else:
		sendNameByMMS.sendText(url, stringnames + " are at your front door", "+17654045543")
else:
	sendNameByMMS.sendText(url, "There is an unidentified person at your front door.  Should he/she come in? Provide name please", "+17654045543")
	time.sleep(40)
	with open("smsMessage.txt") as f:
	    f.readline()
	    content = f.readline()
	if (content != "NO") and (content != "No") and (content != "no") :
		##print facearray
		if (len(facearray) >= 1):
			saveface.saveface(content, facearray[0])


    

