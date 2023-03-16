import cv2
import ctypes
from os import chdir
from os.path import dirname, abspath
from shutil import copyfile
from sys import executable, argv

chdir(dirname(executable))

fps = 10

if len(argv) == 2:
  fps = int(argv[1])

files = ["w"+str(i)+".jpg" for i in range(3)]

SPI_SETDESKWALLPAPER = 20

cap = cv2.VideoCapture('wallpaper.mp4')

if (cap.isOpened()== False): 
  print("Error opening video stream or file")

while 1:
  if cap.isOpened():
    try:
      ret, frame = cap.read()
      fname = files[0]
      files.append(files.pop(0))
      cv2.imwrite(fname, frame)
      ctypes.WinDLL('user32', use_last_error=True).SystemParametersInfoW(20, 0, abspath(fname), 3)
      cv2.waitKey(int(1000/fps))
    except:
      cap = cv2.VideoCapture('wallpaper.mp4')
  else:
    cap = cv2.VideoCapture('wallpaper.mp4')
