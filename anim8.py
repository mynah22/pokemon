from clear import clear
from time import sleep

class bob(object):
    pass

a=bob()

def animation(fps=5):
    clear()
    while True:
        frames=['0000','1000','1100','1110', '1111', '0111','0011', '0001']
        while frames:
            print frames.pop()
            sleep(1.0/fps)
            clear()