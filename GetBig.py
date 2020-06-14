import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Get Big!')
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
blue = (0,80,200)
bright_blue = (0,100,255)
yellow = (180,180,0)
bright_yellow = (220,220,0)
green = (0,200,0)
red = (200,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)


pause = False

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def player(x,y,w,h):
    pygame.draw.rect(gameDisplay, blue, [x, y, w, h])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont('timesnewroman',100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():

    while pause:
        gameDisplay.fill(white)
        message_display('Paused')
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        
        button("Continue",150,450,100,50,green,bright_green,20,unpause)
        button("Quit",550,450,100,50,red,bright_red,20,quitgame)

        pygame.display.update()
        clock.tick(15)


def hit(score):
    global pause
    pause = True

    while pause:
        message_display('Score: ' +str(score))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button('Replay',150,450,100,50,green,bright_green,20,game_loop)
        button('Quit',550,450,100,50,red,bright_red,20,quitgame)

        pygame.display.update()
        clock.tick(15)


def items_picked(count):
    font = pygame.font.SysFont('timesnewroman', 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))


def button(msg,x,y,w,h,ic,ac,size,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("timesnewroman",size)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('calibri',75)
        TextSurf, TextRect = text_objects("Get Big!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        # print(mouse)

        go_button = button('Go!',150,450,100,50,green,bright_green,20,game_loop)
        exit_button = button('Quit',550,450,100,50,red,bright_red,20,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():

    global pause

    pause = False

    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    w = 30
    h = 30
    x_change = 0
    y_change = 0
    player_speed = 0

    thing1_startx = random.randrange(10, display_width-60)
    thing1_starty = -600
    thing1_speed = 3
    thing1_width = 50
    thing1_height = 50

    thing2_startx = -50
    thing2_starty = random.randrange(10,540)
    thing2_speed = 3
    thing2_width = 50
    thing2_height = 50

    thing3_startx = random.randrange(50, display_width-50)
    thing3_starty = random.randrange(50,550)
    thing3_speed = 0

    score = 0


    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -4
                elif event.key == pygame.K_RIGHT:
                    x_change = 4
                elif event.key == pygame.K_UP:
                    y_change = -4
                elif event.key == pygame.K_DOWN:
                    y_change = 4

                elif event.key == pygame.K_SPACE:
                    pause = True
                    paused()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    ######################
        ##
        if (x<0 and x_change<0) or (x>display_width-w and x_change>0):
            x += 0
            hit(score)
        else:
            x += x_change
        if (y<0 and y_change<0) or (y>display_height-h and y_change>0):
            y += 0
            hit(score)
        else:
            y += y_change
        ##
        gameDisplay.fill(white)
        
        # things(thingx, thingy, thingw, thingh, color)
        
        thing3_width = 10
        thing3_height = 10
        things(thing3_startx, thing3_starty, thing3_width, thing3_height, yellow)

        things(thing1_startx, thing1_starty, thing1_width, thing1_height, black)
        thing1_starty += thing1_speed
        things(thing2_startx, thing2_starty, thing2_width, thing2_height, black)
        thing2_startx += thing2_speed

        player(x,y,w,h)

        if 0 < (x - thing1_startx) < 50 or 0 < (thing1_startx - x) < w:
            if 0 < (y - thing1_starty) < 50 or 0 < (thing1_starty - y) < h:
                hit(score)

        if 0 < (x - thing2_startx) < 50 or 0 < (thing2_startx - x) < w:
            if 0 < (y - thing2_starty) < 50 or 0 < (thing2_starty - y) < h:
                hit(score)

        if 0 < (x - thing3_startx) < 10 or 0 < (thing3_startx - x) < w:
            if 0 < (y - thing3_starty) < 10 or 0 < (thing3_starty - y) < h:
                thing3_width = 0
                thing3_height = 0
                w += 2
                h += 2
                things(thing3_startx, thing3_starty, thing3_width, thing3_height, thing3_speed)
                thing3_startx = random.randrange(50, display_width-50)
                thing3_starty = random.randrange(50,550)
                player(x,y,w,h)
                score += 1
        


        # giving the game fresh obstacles
        if thing1_starty > display_height:
            thing1_starty = 0 - thing1_height
            thing1_startx = random.randrange(10,display_width-60)

        if thing2_startx > display_width+50:
            thing2_startx = 0 - thing2_width
            thing2_starty = random.randrange(10,540)


        items_picked(score)
        intro_button = button('Return',750,0,50,25,blue,bright_blue,15,game_intro)
        pygame.display.update()
        clock.tick(100)

game_intro()
game_loop()
pygame.quit()
quit()