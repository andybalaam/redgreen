#!/usr/bin/env python

import pygame
import random

screen_width = 640
screen_height = 480

screen = None
ready_text = None

def start():
    global screen, ready_text
    pygame.init()
    screen = pygame.display.set_mode( ( screen_width, screen_height ) )
    font = pygame.font.Font( None, screen_height / 5 )
    ready_text = font.render( "Ready?", 1, pygame.Color( "white" ) )

def ready_screen():
    textpos = ready_text.get_rect(
        centerx = screen.get_width() / 2,
        centery = screen.get_height() / 2
    )

    screen.blit( ready_text, textpos )
    pygame.display.flip()

def wait():
    time_to_wait = random.randint( 2000, 5000 ) # Between 2 and 5 seconds
    pygame.time.wait( time_to_wait ) # Note bug: can't quit during this time

def shape():
    screen.fill( pygame.Color( "black" ) )
    pygame.display.flip()

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

