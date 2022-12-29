# https://github.com/jhan15/facial_emotion_recognition

import tensorflow as tf

import numpy as np
import cv2
import mediapipe as mp
import time
import glob
import cv2

import sys, os

path = './photo_dir'
path = 'C:/Users/uti1catty/Downloads'

good_emot = ['Neutral', 'Happy', 'Surprise']
bad_emot = ['Angry', 'Disgust', 'Fear', 'Sad']

Downloads_dir_path = sys.argv[1]
path = Downloads_dir_path
photo_dir_list = os.listdir(path)
print(photo_dir_list)

photo_dir_list_len = len(photo_dir_list)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, Dropout, Flatten
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.optimizers import Adam

emotions = {
    0: ['Angry', (0,0,255), (255,255,255)],
    1: ['Disgust', (0,102,0), (255,255,255)],
    2: ['Fear', (255,255,153), (0,51,51)],
    3: ['Happy', (153,0,153), (255,255,255)],
    4: ['Sad', (255,0,0), (255,255,255)],
    5: ['Surprise', (0,255,0), (255,255,255)],
    6: ['Neutral', (160,160,160), (255,255,255)]
}
num_classes = len(emotions)
input_shape = (48, 48, 1)
weights_1 = 'saved_models/vggnet.h5'
weights_2 = 'saved_models/vggnet_up.h5'

class VGGNet(Sequential):
    def __init__(self, input_shape, num_classes, checkpoint_path, lr=1e-3):
        super().__init__()
        self.add(Rescaling(1./255, input_shape=input_shape))
        self.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal'))
        self.add(BatchNormalization())
        self.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same'))
        self.add(BatchNormalization())
        self.add(MaxPool2D())
        self.add(Dropout(0.5))

        self.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same'))
        self.add(BatchNormalization())
        self.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same'))
        self.add(BatchNormalization())
        self.add(MaxPool2D())
        self.add(Dropout(0.4))

        self.add(Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same'))
        self.add(BatchNormalization())
        self.add(Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same'))
        self.add(BatchNormalization())
        self.add(MaxPool2D())
        self.add(Dropout(0.5))

        self.add(Conv2D(512, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same'))
        self.add(BatchNormalization())
        self.add(Conv2D(512, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same'))
        self.add(BatchNormalization())
        self.add(MaxPool2D())
        self.add(Dropout(0.4))

        self.add(Flatten())
        
        self.add(Dense(1024, activation='relu'))
        self.add(Dropout(0.5))
        self.add(Dense(256, activation='relu'))

        self.add(Dense(num_classes, activation='softmax'))

        self.compile(optimizer=Adam(learning_rate=lr),
                    loss=categorical_crossentropy,
                    metrics=['accuracy'])
        
        self.checkpoint_path = checkpoint_path


model_1 = VGGNet(input_shape, num_classes, weights_1)
model_1.load_weights(model_1.checkpoint_path)

model_2 = VGGNet(input_shape, num_classes, weights_2)
model_2.load_weights(model_2.checkpoint_path)

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

def detection_preprocessing(image, h_max=360):
    h, w, _ = image.shape
    if h > h_max:
        ratio = h_max / h
        w_ = int(w * ratio)
        image = cv2.resize(image, (w_,h_max))
    return image

def resize_face(face):
    x = tf.expand_dims(tf.convert_to_tensor(face), axis=2)
    return tf.image.resize(x, (48,48))

def recognition_preprocessing(faces):
    x = tf.convert_to_tensor([resize_face(f) for f in faces])
    return x

def inference(image):
    H, W, _ = image.shape
    
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_image)

    if results.detections:
        faces = []
        pos = []
        for detection in results.detections:
            box = detection.location_data.relative_bounding_box
            # mp_drawing.draw_detection(image, detection)

            x = int(box.xmin * W)
            y = int(box.ymin * H)
            w = int(box.width * W)
            h = int(box.height * H)

            x1 = max(0, x)
            y1 = max(0, y)
            x2 = min(x + w, W)
            y2 = min(y + h, H)

            face = image[y1:y2,x1:x2]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            faces.append(face)
            pos.append((x1, y1, x2, y2))
    
        x = recognition_preprocessing(faces)

        y_1 = model_1.predict(x)
        y_2 = model_2.predict(x)
        l = np.argmax(y_1+y_2, axis=1)

        for i in range(len(faces)):
            cv2.rectangle(image, (pos[i][0],pos[i][1]),
                            (pos[i][2],pos[i][3]), emotions[l[i]][1], 2, lineType=cv2.LINE_AA)
            
            cv2.rectangle(image, (pos[i][0],pos[i][1]-20),
                            (pos[i][2]+20,pos[i][1]), emotions[l[i]][1], -1, lineType=cv2.LINE_AA)
            
            cv2.putText(image, f'{emotions[l[i]][0]}', (pos[i][0],pos[i][1]-5),
                            0, 0.6, emotions[l[i]][2], 2, lineType=cv2.LINE_AA)
            #print(emotions[l[i]][0])
    
    #return image
    return emotions[l[i]][0], image

# from flask import Blueprint, request, render_template, flash, redirect, url_for
# from flask import current_app as current_app
 
# main = Blueprint('main', __name__, url_prefix='/')
 
# @main.route('/main', methods=['GET'])
# def index(emotion):
#     testData = emotion
 
#     return render_template('/main/index.html', testDataHtml=testData)


while(True):
    now_photo_dir_list = os.listdir(path)
    now_photo_dir_list_len = len(now_photo_dir_list)
    found = False
    if now_photo_dir_list_len > photo_dir_list_len:
        for filename in now_photo_dir_list:
            if filename not in photo_dir_list and (filename.endswith('jpg') or filename.endswith('png')):
                target = filename
                found = True
                break
    photo_dir_list = now_photo_dir_list
    now_photo_dir_list_len = photo_dir_list_len
    if found:
        print(target)
        image = cv2.imread(path + '/' + target)
        result, save_img = inference(image)
        
        print(result)
        cv2.imwrite(f'./inference/{result}_{filename}',save_img)
        
        emotion_file = open('current_emotion.txt', 'w')
        if result in good_emot:
            emotion_file.write('good')
        elif result in bad_emot:
            emotion_file.write('bad')
        emotion_file.close()

