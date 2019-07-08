import pygame
from pygame.mixer import Sound
from gpiozero import MotionSensor
from time import sleep
import random

pygame.init()
pygame.mixer.init()

sounds = [
        pygame.mixer.Sound("/home/pi/sound_files/03.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/04.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/05.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/07.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/09.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/10.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/11.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/12.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/13.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/14.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/15.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/16.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/17.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/18.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/19.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/20.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/21.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/22.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/23.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/24.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/25.ogg"),
        pygame.mixer.Sound("/home/pi/sound_files/26.ogg")
        ]

pir = MotionSensor(4)

while True:
    if pir.motion_detected:
        print("Motion detected!")
        playSound = random.choice(sounds)
        playSound.play()
        sleep(15)
        playSound.stop()
