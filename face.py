from PIL import Image

import glob
image_list = []
for filename in glob.glob('/Users/duanyuqin/Documents/knockknock/group.JPG'): 
	im = Image.open(filename)
	image_list.append(im)