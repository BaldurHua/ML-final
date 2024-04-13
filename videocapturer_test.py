import os
import numpy as np
import cv2 as cv2
from PIL import Image


flag_live = False #True False
flag_model = False #True False

if flag_live == True:
    # Initialize the camere
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("The camera is not available")
        exit()
else:
    cap = cv2.VideoCapture('C:\\Users\\Tom\\Downloads\\1001_DFA_HAP_XX.flv')
    if not cap.isOpened():
        print("The video is not available")
        exit()

while True:
    # Return a boolean if the frame is available and the image
    ret, color_frame = cap.read()  
    #print(color_frame)
    if not ret:
        print("The frame is not available")
        break
    # Convert the captured image to grayscale
    gray_frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2GRAY)
    # Call the OpenCV Face recognition
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    face = face_classifier.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    for (x, y, w, h) in face:
        # Create a rectangule in the image
        rect = cv2.rectangle(color_frame, (x, y), (x + w, y + h), color=(255, 185, 0), thickness=5)
        # Capture the face in the rectangule (used to predict the emotion)
        rect_gray = gray_frame[y:y + w, x:x + h]
        rect_gray = cv2.resize(rect_gray, (48, 48))
        print(rect_gray)

        if flag_model == True:
            emotion_prediction = model.predict(rect_gray)
            emootion_index = np.argmax(emotion_prediction[0])
            emotions = ('surprised', 'sad', 'neutral', 'happy', 'fearful', 'disgusted', 'angry')
            predicted_emotion = emotions[emootion_index]
        else:
            predicted_emotion = 'prediction'

        # Include the emotion prediction in the image
        cv2.putText(rect, predicted_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255,255, 255), thickness=2)
            
    cv2.imshow('frame', color_frame)

    # Include a quit botton (press q to quit)
    if cv2.waitKey(20) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
