import pygame
import pygame.camera
import time

pygame.camera.init()
cams = pygame.camera.list_cameras() #Camera detected or not
cam = pygame.camera.Camera(cams[0],(640,480))
cam.start()
time.sleep(0.3)
img = cam.get_image()
pygame.image.save(img,"filename.jpg")
