import cv2

def greyscale(colour):
    return 0.299*colour[2]+0.587*colour[1]+0.114*colour[0]
f=input("Enter File Path:")
img = cv2.imread(f)
blurred = cv2.GaussianBlur(img, (3, 3), 0)

sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

magnitude = cv2.magnitude(sobelx, sobely)
for i in range(len(magnitude)):
    for j in range(len(magnitude[i])):
        magnitude[i][j]=greyscale(magnitude[i][j])
edges = cv2.convertScaleAbs(magnitude)
thresh=cv2.threshold(edges,25, 255, cv2.THRESH_BINARY)
cv2.imwrite(f.split(".")[0]+"_Colour_Sobel."+f.split(".")[1], thresh[1])