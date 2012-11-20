#!/usr/bin/env python

import pygame
import sys

screen_width = 640
screen_height = 480
screen_size = screen_width, screen_height

screen = None
ready_text = None

def start():
    global screen, ready_text
    pygame.init()
    screen = pygame.display.set_mode( screen_size )
    font = pygame.font.Font( None, screen_height / 5 )
    ready_text = font.render( "Ready?", 1, pygame.Color( "white" ) )

def quit():
    pygame.quit()
    sys.exit()

def ready_screen():
    textpos = ready_text.get_rect(
        centerx = screen.get_width() / 2,
        centery = screen.get_height() / 2
    )

    screen.blit( ready_text, textpos )
    pygame.display.flip()

def wait():
    pass

def shape():
    pass

def end():
    pygame.event.clear()
    event_types_that_cancel = pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN
    waiting = True
    while waiting:
        evt = pygame.event.wait()
        if evt.type == pygame.QUIT:
            quit()
        elif evt.type in event_types_that_cancel:
            waiting = False

start()

ready_screen()

wait()

shape()

end()

