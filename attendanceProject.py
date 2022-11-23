import cv2 as cv
import numpy as np
import face_recognition
import os
from datetime import datetime


path = 'opencv project'
images = []
classnames = []
mylist = os.listdir(path)
print(mylist)
for cl in mylist:
    curImg = cv.imread(f'{path}/{cl}')
    images.append(curImg)
    classnames.append(os.path.splitext(cl)[0])
print(classnames)

def findencodings(image):
    encodelist = []
    for img in images:
        img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

def markAttendance(name):
    with open('attendancesheet3.csv','r+') as f:
        mydatalist = f.readlines()
        namelist = []
        for line in mydatalist:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')


encodelistknown = findencodings(images)
print('encodings complete')


cap = cv.VideoCapture(0)

while True:
    success, img = cap.read()
    imgs = cv.resize(img,(0,0),None,0.25,0.25)
    imgs = cv.cvtColor(imgs,cv.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgs)
    encodescurframe = face_recognition.face_encodings(imgs,facesCurFrame)

    for encodeface,faceloc in zip(encodescurframe,facesCurFrame):
        matches = face_recognition.compare_faces(encodelistknown,encodeface)
        facedis = face_recognition.face_distance(encodelistknown,encodeface)
        print(facedis)
        matchindex = np.argmin(facedis)

        if matches[matchindex]:
            name = classnames[matchindex].upper()
            print(name)
            x1,y1,x2,y2 = faceloc
            x1, y1, x2, y2 =  x1*4,y1*4,x2*4,y2*4
            cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),4)
            cv.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv.FILLED)
            cv.putText(img,name,(x1+6,y2-6),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),4)

            markAttendance(name)

            cv.imshow('webcam',img)
            cv.waitKey(1)
























