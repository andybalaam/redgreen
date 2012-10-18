#!/usr/bin/env python

import pygame

screen_size = 640, 480

def start():
    pygame.init()
    screen = pygame.display.set_mode( screen_size )

def ready_screen():
    pass

def wait():
    pass

def shape():
    pass

def end():
    while True:
        evt = pygame.event.wait()
        if evt.type == pygame.QUIT:
            break

start()

ready_screen()

wait()

shape()

end()

