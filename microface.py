import cognitive_face as CF
import httplib, urllib, base64
import json
import faceidgenerate
import saveface

#id1 = faceidgenerate.get_faceid('http://i.imgur.com/cX7kkGN.png')
#id2 = faceidgenerate.get_faceid('http://i.imgur.com/WrucVIE.png')



def compareall(id1, id2):
    i = 0
    for idx1 in id1: # splits array into single element and compares each one
        res = facecompare(idx1,id2)
        if res == 1:
            # saveface.saveface("Alp",idx1)
            return True

    return False
            
            

def facecompare(faceID1, faceID2): #we are going to get two id's and compare to see if they are the same people.
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '60f05be193e248b7ae0a4d8d13960ca8',
    }

    params = urllib.urlencode({}) 

    
    body = { #create json with faceid with strings of faceid's that we inputted
        'faceId1':str(faceID1), 
        'faceId2':str(faceID2),
    }

    try: #connect to microsofts api
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/verify?%s" % params, str(body), headers) #run the comparison
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    dd = json.loads(data) ##load the data from json

    try:
        if dd['isIdentical'] == True: #if they people are identical, return 1(true)
            return 1
        else:
            return 0 #if not return false
    except:
        return 0
#print facecompare("30bb1cda-95b7-4d42-97c9-68710b0158f4", "f1eb812c-7c48-4d95-b577-99a407ee7587")
#compareall(id1, id2[0])
