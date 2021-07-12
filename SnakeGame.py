import pygame
import random
import math

#pygame window size
WIDTH , HEIGHT = 900,500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake game")
FPS = 15 #speed of the game

#size of the objects example apple and snake 
OBJECT_SIZE =20 #can be changed to any number

#both of these methods get random x and y value
def randomx():
    rannum =OBJECT_SIZE*random.randint(0, math.floor((WIDTH-OBJECT_SIZE) /OBJECT_SIZE ))
    return rannum 

def randomy():   
    rannum =OBJECT_SIZE*random.randint(0,math.floor( (HEIGHT-OBJECT_SIZE) /OBJECT_SIZE)) 
    return rannum

#starting size and position of snake
NEXT_MOVE= "RIGHT"
SNAKE_HEAD= [randomx(),randomy()]
SNAKE_BODY = [list(SNAKE_HEAD),[SNAKE_HEAD[0],SNAKE_HEAD[1]-OBJECT_SIZE],[SNAKE_HEAD[0],SNAKE_HEAD[1]-OBJECT_SIZE]]
APPLE_SPAWNED = True
apple_pos=[randomx(), randomy()] 

#colors of the game
GREEN = (0,255,0)
BLACK = (0,0,0)
RED = (255,0,0)

#draws the snake 
def draw_snake():
    for Position in SNAKE_BODY:
        snake_draw = pygame.draw.rect(win,GREEN,pygame.Rect(Position[0],Position[1],OBJECT_SIZE ,OBJECT_SIZE ))

#checks if apple was eaten by snake
def apple_eaten(APPLE_SPAWNED):
    if apple_pos[0] == SNAKE_BODY[0][0] and apple_pos[1] ==SNAKE_BODY[0][1]: #comparest apple position to the head of the snake by x and y if botht he same dont pop the sanek and 
        APPLE_SPAWNED =False                                                 #keep extra tail 
    else:
        SNAKE_BODY.pop() #remvoes the extra tail
    return APPLE_SPAWNED  

#snake travels by adding 10 to x or y on each body and reprinting 
def read_move(NEXT_MOVE):
    keys_pressed = pygame.key.get_pressed()
    PREVIOUS_MOVE = NEXT_MOVE

    if keys_pressed[pygame.K_LEFT]:
        NEXT_MOVE= "LEFT"
    if keys_pressed[pygame.K_RIGHT]:
        NEXT_MOVE= "RIGHT"      
    if keys_pressed[pygame.K_UP]:    
        NEXT_MOVE= "UP"      
    if keys_pressed[pygame.K_DOWN]:
        NEXT_MOVE= "DOWN"

    #make it where if prevois input is right next input cannot be left 
    # if prevois is right and new input is left then change new to old input
    if NEXT_MOVE == "LEFT" and PREVIOUS_MOVE == "RIGHT":
        NEXT_MOVE = PREVIOUS_MOVE
    if NEXT_MOVE == "RIGHT" and PREVIOUS_MOVE =="LEFT":
        NEXT_MOVE = PREVIOUS_MOVE
    if NEXT_MOVE == "UP" and PREVIOUS_MOVE =="DOWN":
        NEXT_MOVE = PREVIOUS_MOVE
    if NEXT_MOVE == "DOWN" and PREVIOUS_MOVE =="UP":
        NEXT_MOVE = PREVIOUS_MOVE

    if NEXT_MOVE == "LEFT":
        SNAKE_HEAD[0] = SNAKE_HEAD[0] - OBJECT_SIZE
    if NEXT_MOVE == "RIGHT":
        SNAKE_HEAD[0] = SNAKE_HEAD[0] + OBJECT_SIZE
    if NEXT_MOVE == "UP":
        SNAKE_HEAD[1] = SNAKE_HEAD[1] - OBJECT_SIZE
    if NEXT_MOVE == "DOWN":
        SNAKE_HEAD[1] = SNAKE_HEAD[1] + OBJECT_SIZE

    #condition to see if snake hits wall
    if SNAKE_HEAD[0] > WIDTH-OBJECT_SIZE or SNAKE_HEAD[1] > HEIGHT-OBJECT_SIZE or SNAKE_HEAD[0] < 0 or SNAKE_HEAD[1] < 0: 
        pygame.quit()
    #condition to see if snake hits itself
    for Position in SNAKE_BODY:  
        if Position[0] == SNAKE_HEAD[0] and Position[1] == SNAKE_HEAD[1]:
            pygame.quit() 
    #adds new had to body             
    SNAKE_BODY.insert(0,list(SNAKE_HEAD)) 
    draw_snake()
    pygame.display.update()    
    return NEXT_MOVE

def check_apple(APPLE_SPAWNED,apple_pos): 
      #spawns in the apple if apple is not spawned
    if APPLE_SPAWNED == False:
       
        apple_pos=[randomx(),randomy()]
        for Position in SNAKE_BODY:  
            if apple_pos[0] == Position[0] and apple_pos[1] == Position[1]: #check to see if the apple does not spawn in the snakes body
                apple_pos=[randomx(),randomy()]
        apple_draw= pygame.draw.rect(win,RED,pygame.Rect(apple_pos[0],apple_pos[1],OBJECT_SIZE ,OBJECT_SIZE )) #check if the appple spwan possition is one of the body if true then spawn again
        APPLE_SPAWNED= True
    else:
        apple_draw= pygame.draw.rect(win,RED,pygame.Rect(apple_pos[0],apple_pos[1],OBJECT_SIZE ,OBJECT_SIZE ))
    return APPLE_SPAWNED, apple_pos

#main
run = True
clock = pygame.time.Clock()
while run: 
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #resets the window to black to update the postion of objects
    win.fill((BLACK))
    
    #draws the snake of the window
    draw_snake()
    
    #checks if apple is spawned if apple exist then redraw if not spawn new apple
    APPLE_SPAWNED, apple_pos = check_apple(APPLE_SPAWNED,apple_pos)

    #reads the user move ands updates NEXT_MOVE
    NEXT_MOVE = read_move(NEXT_MOVE) 

    #checks if apple is on the window
    APPLE_SPAWNED= apple_eaten(APPLE_SPAWNED)

    pygame.display.update()
pygame.quit()



