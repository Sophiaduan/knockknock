import microface
import faceidgenerate
import saveface
import searchface
import face_recognition_real

face_recognition_real.activateCamera()
url = face_recognition_real.getURLString()

facearray = faceidgenerate.get_faceid(url)

rowdetails = searchface.isInCSV(facearray)

if rowdetails != None:
    sendpicname
else:
    newName = sendpicaskname
    if newName != "NO":
        saveface.saveface(newName,rowdetails[0])


    
