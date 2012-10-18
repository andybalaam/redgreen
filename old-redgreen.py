#!/usr/bin/env python

import random
import pygame

pygame.init()
pygame.font.init()

#screen_size = pygame.display.list_modes()[0]
#font_size = screen_size[1] / 3

#white = pygame.Color( "white" )
#black = pygame.Color( "black" )

#screen = pygame.display.set_mode( screen_size, pygame.FULLSCREEN )
#surface = pygame.display.get_surface()

#font = pygame.font.SysFont( "Arial", font_size )

#ready_writing = font.render( "Ready!", True, black )

seconds_timer_id = pygame.USEREVENT

green_time = 10
red_time = 3
number_of_turns = 5

class RedGreenScreen( object ):

    def ready( self, score ):
        print "ready (score=%d)" % score

    def red( self, time ):
        print "red (time=%d)" % time

    def green( self, time ):
        print "green (time=%d)" % time

    def score( self, score ):
        print "score=%d" % score



def wait_one_second():
    pygame.time.set_timer( seconds_timer_id, 1000 )
    pygame.event.wait()
    pygame.time.set_timer( seconds_timer_id, 0 )
    return False


def green_button( rgscreen ):
    clicked = False
    for time in range( green_time, 1, -1 ):
        rgscreen.green( time )
        clicked = wait_one_second()
        if clicked:
            break
    success = clicked
    return success

def red_button( rgscreen ):
    clicked = False
    for time in range( red_time, 0, -1 ):
        rgscreen.red( time )
        clicked = wait_one_second()
        if clicked:
            break
    success = not clicked
    return success


def single_game():
    score = 0

    rgscreen = RedGreenScreen()

    for i in range( number_of_turns ):

        rgscreen.ready( score )

        colour = random.choice( ("green", "red") )

        if colour == "green":
            success = green_button( rgscreen )
        else:
            success = red_button( rgscreen )

        if success:
            score += 1

    rgscreen.score( score )


single_game()

#surface.fill( white )
#surface.blit( ready_writing, ( 0,0 ) )
#pygame.display.flip()
#
#pygame.event.wait()

#for event in pygame.event.get():
#    





