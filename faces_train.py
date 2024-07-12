import os
import cv2 as cv
import numpy as np


people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield','Madona', 'Mindy Kaling']



DIR = r'C:\Users\hp\Documents\OpenCV\archive\train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')


# # data dir, create list and append directly from dir
# P = []
# for i in os.listdir(r'C:\Users\hp\Documents\OpenCV\archive\train'):
#     P.append(i)
# print(P) 

features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training Don!!!!')
# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')


features = np.array(features, dtype='object')
labels = np.array(labels)
#face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#train
face_recognizer.train(features, labels)
#save it to be used later
face_recognizer.save('face_trained.yml')
np.save('feature.npy', features)
np.save('labels.npy', labels)