#!/usr/bin/env python

import math
import pygame
import random
import sys

screen_width = 640
screen_height = 480

screen = None
rendered_main_texts = {}
rendered_small_texts = {}

wait_time = 2000 # Display each shape for 2 seconds

def start():
    global screen, ready_text, ready_text_pos, end_text, end_text_pos
    pygame.init()
    screen = pygame.display.set_mode( ( screen_width, screen_height ) )

def write_main_text( screen, text, color ):
    global rendered_main_texts
    if text not in rendered_main_texts:
        font = pygame.font.Font( None, screen_height / 5 )
        rend = font.render( text, 1, color )
        pos = rend.get_rect(
            centerx = screen.get_width() / 2,
            centery = screen.get_height() / 2
        )
        rendered_main_texts[text] = rend, pos
    else:
        rend, pos = rendered_main_texts[text]
    screen.blit( rend, pos )


def write_small_text( screen, text, color ):
    global rendered_small_texts
    if text not in rendered_small_texts:
        font = pygame.font.Font( None, screen_height / 12 )
        rend = font.render( text, 1, color )
        pos = rend.get_rect(
            centerx = screen.get_width() / 2,
            centery = screen.get_height() - ( screen_height / 24 )
        )
        rendered_small_texts[text] = rend, pos
    else:
        rend, pos = rendered_small_texts[text]
    screen.blit( rend, pos )


def quit():
    pygame.quit()
    sys.exit()

def ready_screen( go_number ):
    screen.fill( pygame.Color( "black" ) )
    write_main_text( screen, "Ready?", pygame.Color( "white" ) )

    go_number_str = "Go number: %d" % go_number

    write_small_text( screen, go_number_str, pygame.Color( "white" ) )

    pygame.display.flip()

def timed_wait( time_to_wait, event_types_that_cancel ):
    """
    Wait for the specified time_to_wait, but cancel if we receive an
    event of one of the types in event_types_that_cancel.
    Return True if we were cancelled, or False if the time ran out.
    """

    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < time_to_wait:
        evt = pygame.event.poll()
        if evt.type == pygame.QUIT:
            quit()
        elif evt.type in event_types_that_cancel:
            return ( True, pygame.time.get_ticks() - start_time )
        pygame.time.wait( 10 ) # Give the system a little rest

    return ( False, time_to_wait )


def wait():
    time_to_wait = random.randint( 1500, 3000 ) # Between 1.5 and 3 seconds
    timed_wait( time_to_wait, [] )


def shape_wait():
    global wait_time

    pygame.event.clear()
    return timed_wait( wait_time, ( pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN ) )

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

    mouth_left   = centre_x - ( 3 * radius / 8 )
    mouth_width  = 3 * radius / 4
    mouth_top    = centre_y
    mouth_height = 2 * radius / 3

    mouth_rect = ( ( mouth_left, mouth_top ), ( mouth_width, mouth_height ) )
    mouth_start = math.pi       # Downwards
    mouth_end   = 2 * math.pi   # Upwards

    screen.fill( pygame.Color( "white" ) )
    pygame.draw.circle( screen, green, centre, radius, width )
    pygame.draw.circle( screen, green, eye1_centre, eye_radius, width )
    pygame.draw.circle( screen, green, eye2_centre, eye_radius, width )
    pygame.draw.arc( screen, green, mouth_rect, mouth_start, mouth_end, width )

def sad_face():
    red = pygame.Color( "red" )
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

    mouth_left   = centre_x - ( 3 * radius / 8 )
    mouth_width  = 3 * radius / 4
    mouth_top    = centre_y + ( radius / 5 )
    mouth_height = 2 * radius / 3

    mouth_rect = ( ( mouth_left, mouth_top ), ( mouth_width, mouth_height ) )
    mouth_start = 0
    mouth_end   = math.pi

    screen.fill( pygame.Color( "white" ) )
    pygame.draw.circle( screen, red, centre, radius, width )
    pygame.draw.circle( screen, red, eye1_centre, eye_radius, width )
    pygame.draw.circle( screen, red, eye2_centre, eye_radius, width )
    pygame.draw.arc( screen, red, mouth_rect, mouth_start, mouth_end, width )

def result_wait():
    result_time = 3000 # wait for 4 seconds
    timed_wait( result_time, ( pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN ) )

def green_success():
    smiley_face()
    write_main_text( screen, "Well done!", pygame.Color( "green" ) )
    write_small_text(
        screen, "You pressed on green!", pygame.Color( "black" ) )
    pygame.display.flip()

    result_wait()

def green_failure():
    sad_face()
    write_main_text( screen, "Bad luck!", pygame.Color( "red" ) )
    write_small_text(
        screen, "Green means press something!", pygame.Color( "black" ) )

    pygame.display.flip()

    result_wait()


def red_success():
    smiley_face()
    write_main_text( screen, "Well done!", pygame.Color( "green" ) )
    write_small_text(
        screen, "You didn't press on red!", pygame.Color( "black" ) )
    pygame.display.flip()

    result_wait()

def red_failure():
    sad_face()
    write_main_text( screen, "Bad luck!", pygame.Color( "red" ) )
    write_small_text(
        screen, "Red means don't press anything!", pygame.Color( "black" ) )

    pygame.display.flip()

    result_wait()


def green_shape():
    green = pygame.Color( "green" )
    centre = ( screen.get_width() / 2, screen.get_height() / 2 )
    radius = screen.get_height() / 3

    screen.fill( pygame.Color( "white" ) )
    pygame.draw.circle( screen, green, centre, radius, 0 )

    write_small_text( screen, "Press something!", pygame.Color( "black" ) )

    pygame.display.flip()

    pressed, time = shape_wait()

    if pressed:
        green_success()
        return 1, time
    else:
        green_failure()
        return 0, time


def red_shape():
    global wait_time

    red = pygame.Color( "red" )
    height = 2 * ( screen.get_height() / 3 )
    left = ( screen.get_width() / 2 ) - ( height / 2 )
    top = screen.get_height() / 6
    centre = ( screen.get_width() / 2, screen.get_height() / 2 )
    radius = screen.get_height() / 3

    screen.fill( pygame.Color( "white" ) )
    pygame.draw.rect( screen, red, ( left, top, height, height ), 0 )

    write_small_text( screen, "Don't press!", pygame.Color( "black" ) )

    pygame.display.flip()

    pressed, time = shape_wait()

    if pressed:
        red_failure()
        return 0, wait_time
    else:
        red_success()
        return 1, 0


def shape():
    GREEN = 0
    RED   = 1
    shape = random.choice( [GREEN, RED] )

    if shape == GREEN:
        return green_shape()
    else:
        return red_shape()


def end( correct, time_score ):
    print "You got %d correct answers" % correct
    print "You scored %d" % time_score
    screen.fill( pygame.Color( "white" ) )
    black = pygame.Color( "black" )
    write_main_text( screen, "Thanks for playing!", black )

    write_small_text( screen, "You got %d correct answers." % correct, black )

    pygame.display.flip()

    end_time = 10000 # wait for 10 seconds
    timed_wait( end_time, ( pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN ) )

    quit()



# We start from here

start()

num_goes = 10

correct = 0
time_millis = 0
for i in range( num_goes ):
    ready_screen( i )
    wait()
    correct_points, tm_points = shape()
    correct += correct_points
    time_millis += tm_points

max_time = num_goes * wait_time

end( correct, max_time - time_millis )

