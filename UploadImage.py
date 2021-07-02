import cv2
import random
import time
import dropbox
from dropbox.dropbox_client import _DropboxTransport
from pkg_resources import normalize_path
startTime=time.time()

def takesnapshot():
    number=random.randint(0,100)
    image= cv2.VideoCapture(0)
    result=True
    while result:
        dummy,frame=image.read()
        #print(dummy)
        imageName="img"+ str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time
        result=False
    return imageName
    print("SnapShotTaken")    
    image.release()
    cv2.destroyAllWindows()
def uploadFiles(imageName):
    accessToken="ara6m__wLogAAAAAAAAAAUljw-hs_j7i5qwbGbqm7S2eT4StHgqg1KklgbommEON"
    FileFrom=imageName
    file2="/ericFolder/"+(imageName)
    dbx= dropbox.Dropbox(accessToken)
    with open(FileFrom,"rb")as f:
        dbx.files_upload(f.read(),file2,mode=dropbox.files.WriteMode.overwrite)
        print("FileUploaded")
def setup():
    while True:
        if((time.time()-startTime)>=5):
            Name=takesnapshot()
            uploadFiles(Name)
setup()                   