import tensorflow as tf
import dlib
import cv2
import os
import numpy as np
from PIL import Image, ImageChops, ImageEnhance
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img


def predict(file):
    model = load_model('deepfake-detection-model.h5')
    input_shape = (128, 128, 3)
    #pr_data = ""
    pr_data=[]
    f=0
    detector = dlib.get_frontal_face_detector()
    cap = cv2.VideoCapture(file)
    frameRate = cap.get(5)
    while cap.isOpened():
        frameId = cap.get(1)
        ret, frame = cap.read()
        if ret != True:
            break
        if frameId % ((int(frameRate)+1)*1) == 0:
            face_rects, scores, idx = detector.run(frame, 0)
            for i, d in enumerate(face_rects):
                x1 = d.left()
                y1 = d.top()
                x2 = d.right()
                y2 = d.bottom()
                crop_img = frame[y1:y2, x1:x2]
                data = np.array(img_to_array(cv2.resize(crop_img, (128, 128))))
                data = data.reshape(-1, 128, 128, 3)
                #print(np.argmax(model.predict(data)))
                pr_data.append(model.predict_classes(data))
                if(model.predict(data)==0):
                   f=1
                   break
    if(f==0):
        pr_data="Video is real!"
    else:
        pr_data="Video is fake!"
    #print(pr_data)
    return pr_data

print(predict(r'''C:\Users\hp\Desktop\minor\fake.mp4'''))

    #print(predict(file))
    #return pr_data
