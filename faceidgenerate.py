import httplib, urllib, base64
import json

def get_faceid(url):
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
       
    face = json.loads(data)
    length = len(face)
    facearray = []
    for j in face:
        facearray.append(str(j["faceId"]))
    return facearray

