import os
from time import sleep
def takesnap():
	os.system("fswebcam -F 4 --fs 20 -r 800*600/home/cl2o3/bindu.jpg")
	return
for i in range(10):
	takesnap()
	sleep(5)

