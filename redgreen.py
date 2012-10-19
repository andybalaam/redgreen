#!/usr/bin/env python

import pygame
import random

screen_width = 640
screen_height = 480

screen = None
ready_text = None

def start():
    global screen, ready_text, ready_text_pos
    pygame.init()
    screen = pygame.display.set_mode( ( screen_width, screen_height ) )
    font = pygame.font.Font( None, screen_height / 5 )
    ready_text = font.render( "Ready?", 1, pygame.Color( "white" ) )
    ready_text_pos = ready_text.get_rect(
        centerx = screen.get_width() / 2,
        centery = screen.get_height() / 2
    )

def ready_screen():
    screen.fill( pygame.Color( "black" ) )
    screen.blit( ready_text, ready_text_pos )
    pygame.display.flip()

def wait():
    time_to_wait = random.randint( 1500, 3000 ) # Between 1.5 and 3 seconds
    pygame.time.wait( time_to_wait ) # Note bug: can't quit during this time

def green_shape():
    green = pygame.Color( "green" )
    centre = ( screen.get_width() / 2, screen.get_height() / 2 )
    radius = screen.get_width() / 3

    screen.fill( pygame.Color( "white" ) )
    pygame.draw.circle( screen, green, centre, radius, 0 )

    pygame.display.flip()

def shape():
    green_shape()

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

