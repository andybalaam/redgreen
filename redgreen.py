#!/usr/bin/env python

import math
import pygame
import random

screen_width = 640
screen_height = 480

screen = None
rendered_texts = {}

def start():
    global screen, ready_text, ready_text_pos, end_text, end_text_pos
    pygame.init()
    screen = pygame.display.set_mode( ( screen_width, screen_height ) )

def write_text( screen, text, color ):
    global rendered_texts
    if text not in rendered_texts:
        font = pygame.font.Font( None, screen_height / 5 )
        rend = font.render( text, 1, color )
        pos = rend.get_rect(
            centerx = screen.get_width() / 2,
            centery = screen.get_height() / 2
        )
        rendered_texts[text] = rend, pos
    else:
        rend, pos = rendered_texts[text]
    screen.blit( rend, pos )

def ready_screen():
    screen.fill( pygame.Color( "black" ) )
    write_text( screen, "Ready?", pygame.Color( "white" ) )
    pygame.display.flip()

def wait():
    time_to_wait = random.randint( 1500, 3000 ) # Between 1.5 and 3 seconds
    pygame.time.wait( time_to_wait ) # Note bug: can't quit during this time

def green_wait():

    wait_time = 2000     # We will wait for 2 seconds for a keypress
    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < wait_time:
        evt = pygame.event.poll()
        if evt.type == pygame.QUIT:
            raise Exception()
        elif evt.type in ( pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN ):
            return True
        pygame.time.wait( 10 ) # Give the system a little rest

    return False

def smiley_face():
    green = pygame.Color( "green" )
    centre_x = screen.get_width() / 2
    centre_y = screen.get_height() / 2
    centre = centre_x, centre_y
    radius = int( screen.get_height() / 2.5 )
    width = screen.get_height() / 30

    eye_radius = screen.get_height() / 10
    eye1_centre_x = centre_x - ( radius / 3 )
    eye1_centre_y = centre_y - ( 13 * radius / 30 )
    eye2_centre_x = centre_x + ( radius / 3 )
    eye2_centre_y = centre_y - ( 13 * radius / 30 )

    eye1_centre = eye1_centre_x, eye1_centre_y
    eye2_centre = eye2_centre_x, eye2_centre_y

    mouth_left   = centre_x - ( radius / 2 )
    mouth_width  = radius
    mouth_top    = centre_y - ( radius / 10 )
    mouth_height = 2 * radius / 3

    mouth_rect = ( ( mouth_left, mouth_top ), ( mouth_width, mouth_height ) )
    mouth_start = math.pi       # Downwards
    mouth_end   = 2 * math.pi   # Upwards

    screen.fill( pygame.Color( "white" ) )
    pygame.draw.circle( screen, green, centre, radius, width )
    pygame.draw.circle( screen, green, eye1_centre, eye_radius, width )
    pygame.draw.circle( screen, green, eye2_centre, eye_radius, width )
    pygame.draw.arc( screen, green, mouth_rect, mouth_start, mouth_end, width )

def green_success():
    smiley_face()
    write_text( screen, "Well done!", pygame.Color( "green" ) )
    pygame.display.flip()

    while True:
        evt = pygame.event.wait()
        if evt.type == pygame.QUIT:
            raise Exception()
        elif evt.type in ( pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN ):
            break

def green_failure():
    print "Failure!"

def green_shape():
    green = pygame.Color( "green" )
    centre = ( screen.get_width() / 2, screen.get_height() / 2 )
    radius = screen.get_height() / 3

    screen.fill( pygame.Color( "white" ) )
    pygame.draw.circle( screen, green, centre, radius, 0 )

    pygame.display.flip()

    success = green_wait()

    if success:
        green_success()
    else:
        green_failure()

def shape():
    green_shape()


def end():
    screen.fill( pygame.Color( "white" ) )
    write_text( screen, "Thanks for playing!", pygame.Color( "black" ) )
    pygame.display.flip()

    while True:
        evt = pygame.event.wait()
        if (
            evt.type == pygame.QUIT or
            evt.type in ( pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN )
        ):
            break

start()

ready_screen()

wait()

shape()

end()

