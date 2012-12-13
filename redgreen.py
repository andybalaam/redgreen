#!/usr/bin/env python

import math
import pygame
import random
import sys

screen_width = 640
screen_height = 480

screen = None

wait_time = 2000 # Display each shape for 2 seconds

def start():
    global screen, ready_text, ready_text_pos, end_text, end_text_pos
    pygame.init()
    screen = pygame.display.set_mode(
        ( screen_width, screen_height ), pygame.FULLSCREEN )

def write_text( screen, text, color, big ):
    if big:
        height = screen.get_height() / 5
        up = screen.get_height() / 2
    else:
        height = screen_height / 12
        up = screen.get_height() - ( screen_height / 24 )
    font = pygame.font.Font( None, height )
    rend = font.render( text, 1, color )
    pos = rend.get_rect(
        centerx = screen.get_width() / 2,
        centery = up
    )
    screen.blit( rend, pos )


def quit():
    pygame.quit()
    sys.exit()

def ready_screen( go_number, correct, time_score ):
    screen.fill( pygame.Color( "black" ) )
    write_text( screen, "Ready?", pygame.Color( "white" ), True )

    go_number_str = "Turn: %d   Correct: %d    Score: %d" % (
        ( go_number + 1 ), correct, time_score )

    write_text( screen, go_number_str, pygame.Color( "white" ), False )

    pygame.display.flip()

def is_quit( evt ):
    return (
        evt.type == pygame.QUIT or
        (
            evt.type == pygame.KEYDOWN and
            evt.key == pygame.K_ESCAPE
        )
    )

def timed_wait( time_to_wait, event_types_that_cancel ):
    """
    Wait for the specified time_to_wait, but cancel if we receive an
    event of one of the types in event_types_that_cancel.
    Return True if we were cancelled, or False if the time ran out.
    """

    start_time = pygame.time.get_ticks()

    event_id = pygame.USEREVENT + 1
    pygame.time.set_timer( event_id, time_to_wait )

    try:
        while True:
            evt = pygame.event.wait()
            if is_quit( evt ):
                quit()
            elif evt.type in event_types_that_cancel:
                return ( True, pygame.time.get_ticks() - start_time )
            elif evt.type == event_id:
                return ( False, time_to_wait )
    finally:
        pygame.time.set_timer( event_id, 0 )


def wait():
    time_to_wait = random.randint( 1500, 3000 ) # Between 1.5 and 3 seconds
    timed_wait( time_to_wait, [] )


def shape_wait():
    global wait_time

    pygame.event.clear()
    return timed_wait( wait_time, ( pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN ) )

def tick():
    colour = pygame.Color( "green" )
    w = screen.get_width() / 2
    h = screen.get_height() / 4
    points = (
        ( w - w/5, h - h/9 ),
        ( w,       h + h/5 ),
        ( w + w/3, h - h/3 ),
    )

    screen.fill( pygame.Color( "black" ) )
    pygame.draw.lines( screen, colour, False, points, 20 )


def cross():
    colour = pygame.Color( "red" )
    w = screen.get_width() / 2
    h = screen.get_height() / 4
    left   = w - w/3
    right  = w + w/3
    top    = h - h/3
    bottom = h + h/3

    start1 = left, top
    end1   = right, bottom

    start2 = left, bottom
    end2   = right, top

    screen.fill( pygame.Color( "black" ) )
    pygame.draw.line( screen, colour, start1, end1, 20 )
    pygame.draw.line( screen, colour, start2, end2, 20 )

def result_wait():
    result_time = 3000 # wait for 4 seconds
    timed_wait( result_time, ( pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN ) )

def green_success():
    tick()
    write_text( screen, "Well done!", pygame.Color( "green" ), True )
    write_text(
        screen, "You pressed on green!", pygame.Color( "black" ), False )
    pygame.display.flip()

    result_wait()

def green_failure():
    cross()
    write_text( screen, "Bad luck!", pygame.Color( "red" ), True )
    write_text(
        screen, "Green means press something!", pygame.Color( "black" ), False )

    pygame.display.flip()

    result_wait()


def red_success():
    tick()
    write_text( screen, "Well done!", pygame.Color( "green" ), True )
    write_text(
        screen, "You didn't press on red!", pygame.Color( "black" ), False )
    pygame.display.flip()

    result_wait()

def red_failure():
    cross()
    write_text( screen, "Bad luck!", pygame.Color( "red" ), True )
    write_text(
        screen,
        "Red means don't press anything!",
        pygame.Color( "black" ),
        False
    )

    pygame.display.flip()

    result_wait()


def green_shape():
    green = pygame.Color( "green" )
    centre = ( screen.get_width() / 2, screen.get_height() / 2 )
    radius = screen.get_height() / 3

    screen.fill( pygame.Color( "white" ) )
    pygame.draw.circle( screen, green, centre, radius, 0 )

    write_text( screen, "Press something!", pygame.Color( "black" ), False )

    pygame.display.flip()

    pressed, time = shape_wait()

    if pressed:
        green_success()
        return True, 1, time
    else:
        green_failure()
        return True, 0, time


def red_shape():
    global wait_time

    red = pygame.Color( "red" )
    height = 2 * ( screen.get_height() / 3 )
    left = ( screen.get_width() / 2 ) - ( height / 2 )
    top = screen.get_height() / 6

    screen.fill( pygame.Color( "white" ) )
    pygame.draw.rect( screen, red, ( left, top, height, height ), 0 )

    write_text( screen, "Don't press!", pygame.Color( "black" ), False )

    pygame.display.flip()

    pressed, time = shape_wait()

    if pressed:
        red_failure()
        return False, 0, wait_time
    else:
        red_success()
        return False, 1, 0


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
    write_text( screen, "Thanks for playing!", black, True )

    write_text(
        screen,
        "Correct: %d      Score: %d" % ( correct, time_score ),
        black,
        False
    )

    pygame.display.flip()

    end_time = 10000 # wait for 10 seconds
    timed_wait( end_time, ( pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN ) )

    quit()



# We start from here

start()

num_greens = 10 # How many times we play

correct = 0
time_millis = 0
i = 0
while i < num_greens:
    max_time = i * wait_time
    ready_screen( i, correct, max_time - time_millis )
    wait()
    wasgreen, correct_points, tm_points = shape()
    if wasgreen:
        i += 1
    correct += correct_points
    time_millis += tm_points

max_time = num_greens * wait_time

end( correct, max_time - time_millis )

