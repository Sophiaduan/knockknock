import cognitive_face as CF

KEY = '030ac8b8f1d2458aaa0166ba72a5e19c'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.detect(img_url)
print result
# ########### Python 2.7 #############
# import httplib, urllib, base64

# headers = {
#     # Request headers
#     'Content-Type': 'application/json',
#     'Ocp-Apim-Subscription-Key': 'dbab4420632b4dba8e8d198f5095d0ff ',
# }

# params = urllib.urlencode({
# })

# try:
#     conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
#     conn.request("POST", "/face/v1.0/verify?%s" % params, "{body}", headers)
#     response = conn.getresponse()
#     data = response.read()
#     print(data)
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))

# ####################################