import cognitive_face as CF
import httplib, urllib, base64
import json 

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '60f05be193e248b7ae0a4d8d13960ca8',
}

params = urllib.urlencode({})

body = {
    'faceId1':'b7e86696-d381-4008-9238-95dbff1c2746',
    'faceId2':'b28a34fb-1367-46df-9b7a-f8313ecdfd95'
}

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/verify?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

dd = json.loads(data)

if dd['isIdentical'] == True:
    print "hello"
