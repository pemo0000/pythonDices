import pygame
from random import randint

class dice:
    def __init__(self):
        return

    def roll(self):
        self.result = randint(1, 6)
        return self.result

    def speak(self):
        pygame.mixer.init()
        pygame.mixer.music.load(str(self.result) + 'se.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

