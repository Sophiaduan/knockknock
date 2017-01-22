import httplib, urllib, base64
import json

def get_faceid(url): #take url of image (imgur) as input image
    #set params of request
    url = str(url)
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '60f05be193e248b7ae0a4d8d13960ca8',
    }

    params = urllib.urlencode({
        # Request parameters
        'returnFaceId': 'true',
    })

    body = {
    'url':url,
        }
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, str(body), headers)
        response = conn.getresponse()
        data = response.read()
        #print(data)
        conn.close()
    except Exception as e:
       print("[Errno {0}] {1}".format(e.errno, e.strerror))
    #parse json data   
    face = json.loads(data)
    length = len(face)
    facearray = []
    #store faceids in facearray for each id
    for j in face:
        facearray.append(str(j["faceId"]))
    return facearray
#get_faceid("https://scontent-ort2-1.xx.fbcdn.net/v/t1.0-9/11229756_10153604723888678_8829369506583921846_n.jpg?oh=283d514f74528fbb5a212d18e6c47d06&oe=591D2550")
