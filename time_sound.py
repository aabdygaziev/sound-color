import sys
from termcolor import colored, cprint
import threading
import time
import pygame
pygame.init()
pygame.mixer.init()
def music(sound):

            pygame.mixer.music.load('20 Syllables (feat. Jay-Z, Dr. Dre, 50 Cent, Stat Quo & Cashis).mp3')
            pygame.mixer.music.play()



def count(number):
    i = 0
    while True:
        i += 1
        print(str(number) + ' ' + str(i))
        time.sleep(1)
        if i == number:
            t2 = threading.Thread(target=music, args=(0,))
            t2.start()

t1 = threading.Thread(target=count, args=(10,))
t1.start()
