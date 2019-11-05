import PIL.ImageGrab
import time
import os

for x in range(1):
	im = PIL.ImageGrab.grab()       
	save_path = "E:\\Barak Computer\\Studies\\Studies\\Year B\\Semester A\\Python-2019A-ll\\Review\\MySnapshot1.jpg"
	im.save(save_path)
	im1 = PIL.ImageGrab.grab()  
	save_path = "E:\\Barak Computer\\Studies\\Studies\\Year B\\Semester A\\Python-2019A-ll\\Review\\MySnapshot2.jpg"
	im.save(save_path)
print(im==im1)


