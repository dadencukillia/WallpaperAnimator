import cv2
import ctypes
from os import chdir
from os.path import dirname
from sys import executable

chdir(dirname(executable))

SPI_SETDESKWALLPAPER = 20 

cap = cv2.VideoCapture('wallpaper.mp4')

if (cap.isOpened()== False): 
  print("Error opening video stream or file")

while 1:
  if cap.isOpened():
    ret, frame = cap.read()
    cv2.imwrite("image.jpg", frame)
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "image.jpg" , 0)
    cv2.waitKey(1000/24)
  else:
    cap = cv2.VideoCapture('wallpaper.mp4')
