import httplib, urllib, base64
import json

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
    'url':'https://scontent-ort2-1.xx.fbcdn.net/v/t31.0-8/16179396_10155070442993678_2865845033378000667_o.jpg?oh=29f2ee64953ba7495b9d6f80c8153a5e&oe=59130D64',
    }
try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
