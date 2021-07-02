import cv2
image= cv2.imread("Big smoke.png",1)
cv2.imshow("MyImage",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(image.shape)