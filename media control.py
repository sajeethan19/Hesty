from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import pygame
import pygame.camera
import time
from pynput.keyboard import Key,Controller

import os

keyboard = Controller()


# Load the model
model = load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


pygame.camera.init()
cams = pygame.camera.list_cameras() #Camera detected or not
cam = pygame.camera.Camera(cams[0],(640,480))
cam.start()
time.sleep(0.3)
while True:
    img = cam.get_image()
    pygame.image.save(img,"filename1.jpg")
    time.sleep(0.3)

    # Replace this with the path to your image
    image = Image.open('filename1.jpg')
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    top = list(prediction[0]).index(max(prediction[0]))
    


    topval= prediction[0][top]
    if topval>0.8:
        if top==2 :
            comm="non"
            
        elif top<2:
            comm="left"
            for i in range(10):
                keyboard.press(Key.media_volume_up)
                keyboard.release(Key.media_volume_up)
                time.sleep(0.1)
            time.sleep(1)
        elif top>2:
            comm="right"
            for i in range(10):
                keyboard.press(Key.media_volume_down)
                keyboard.release(Key.media_volume_down)
                time.sleep(0.1)
            time.sleep(1)
        print(comm)
    
