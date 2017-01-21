from fbrecog import recognize
path = 'Face1.png' #Insert your image file path here
access_token = "EAACEdEose0cBAH7UZAekaSWT0JrR7Sp7xVuSD1nGJXoU0JpxygteCeVc3wh59IxI8BTcQnR7RrxgNSrLGdLkIPj1bxDZC7XyIxZBgAAbgW5CILigeHMDiK9ar68JZCEJcMas2iiFLvfJi9sCtxGybNKpE18vbhKdNYbguN2xJQZDZD" #Insert your access token obtained from Graph API explorer here
cookie = '###' #Insert your cookie string here
fb_dtsg = '###' #Insert the fb_dtsg parameter obtained from Form Data here.
print(recognize(path,access_token,cookie,fb_dtsg))


