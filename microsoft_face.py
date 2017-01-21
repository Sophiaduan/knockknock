import cognitive_face as CF

KEY = '030ac8b8f1d2458aaa0166ba72a5e19c '  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

img_url = '/Users/duanyuqin/Documents/knockknock/Sophia1.jpg'
img_url2 = '/Users/duanyuqin/Documents/knockknock/Sophia2.jpg'
result = CF.face.detect(img_url)
result2 = CF.face.detect(img_url2)
print result
print result2