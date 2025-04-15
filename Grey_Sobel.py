import cv2
import numpy as np
f=input("Enter File Path:")
img = cv2.imread(f)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grey, (3, 3), 0)

sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

magnitude = cv2.magnitude(sobelx, sobely)
edges = cv2.convertScaleAbs(magnitude)
thresh=cv2.threshold(edges,25, 255, cv2.THRESH_BINARY)
cv2.imwrite(f.split(".")[0]+"_Grey_Sobel."+f.split(".")[1], thresh[1])