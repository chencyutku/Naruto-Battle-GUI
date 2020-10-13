#顯示每秒滑鼠動靜~
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16);
font_height = font.get_linesize()
event_text = []

while True:

    event = pygame.event.wait()
    event_text.append(str(event))
    #獲得時間的名稱
    event_text = event_text[-SCREEN_SIZE[1]//font_height:]
    #這個切片操作保證了event_text裡面只保留一個螢幕的文字

    if event.type == QUIT:
        exit()

    screen.fill((255, 255, 255))

    y = SCREEN_SIZE[1]-font_height
    #找一個合適的起筆位置，最下面開始但是要留一行的空
    for text in reversed(event_text):
        screen.blit( font.render(text, True, (0, 255, 0)), (0, y) )
        #以後會講
        y-=font_height
        #把筆提一行

    pygame.display.update()