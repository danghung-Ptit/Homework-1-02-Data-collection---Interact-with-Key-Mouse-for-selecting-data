#!/usr/bin/env python3

import cv2
import os
cam = cv2.VideoCapture(1)
img_counter = 0
path = "/Users/abc/Documents/ảnh chụp" # folder lưu ảnh chụp
while True:
	ret, frame = cam.read()
	if not ret:
		print("Không lấy được khung")
		break
	cv2.imshow("test", frame)
	key = cv2.waitKey(1)
	if key == ord('q'): # nhấn q để thoát
		print("thoát")
		break
	elif key % 256 == 32: #nhấn dấu cách để chụp
		img_name = "{}B18DCDT100E.jpg".format(img_counter)
		cv2.imwrite(os.path.join(path, img_name), frame)
		print("{}".format(img_name))
		img_counter += 1
		
cam.release()
cv2.destroyAllWindows() 