import pygame
import time

audio_file = 'choomah.mp3'

class ChoomahException(Exception):
    pygame.mixer.pre_init(44100, -16, 2, 2048)  # setup mixer to avoid sound lag
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(-1)
    time.sleep(5)
    pygame.quit()

raise ChoomahException("yenaye")
