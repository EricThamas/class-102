import cv2

def takesnapshot():
    image= cv2.VideoCapture(0)
    result=True
    while True:
        dummy,frame=image.read()
        print(dummy)
        
        cv2.imshow("myImage",frame)
        cv2.imwrite("MyImage.png",frame)
        cv2.waitKey(0)
        result=False
    image.release()
    cv2.destroyAllWindows()
takesnapshot()