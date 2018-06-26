import ossaudiodev
# import pygame
from random import randint
from wave import open as waveOpen
from ossaudiodev import open as ossOpen
from time import sleep

class dice:
    def __init__(self):
        return
        #pygame.mixer.init()

    def roll(self):
        self.result = randint(1, 6)
        return self.result

    def speak(self):
        #pygame.mixer.music.load(str(self.result) + 'se.wav')
        #pygame.mixer.music.play()
        #while pygame.mixer.music.get_busy() == True:
        #    continue
        s = waveOpen(str(self.result) + 'se.wav', 'rb')
        (nc, sw, fr, nf, comptype, compname) = s.getparams()
        dsp = ossOpen('/dev/dsp', 'w')
        try:
            from ossaudiodev import AFMT_S16_NE
        except ImportError:
            from sys import byteorder
            if byteorder == "little":
                AFMT_S16_NE = ossaudiodev.AFMT_S16_LE
            else:
                AFMT_S16_NE = ossaudiodev.AFMT_S16_BE
        dsp.setparameters(AFMT_S16_NE, nc, fr)
        data = s.readframes(nf)
        s.close()
        dsp.write(data)
        # little sleep, otherwise .wavs are played too fast
        sleep(0.35)
        dsp.close()

