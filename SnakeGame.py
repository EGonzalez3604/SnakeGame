import pygame
import random
#pygame window size
WIDTH , HEIGHT = 900,500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake game")
FPS = 30 #low fps slower the game
SCORE =0 
#both methods return random x and y values
def randomx():
    rannum =20*random.randint(0,WIDTH /20) 
    return rannum 
def randomy():
    rannum =20*random.randint(0,HEIGHT /20)  
    return rannum

#size of the objects example apple and snake
OBJECT_SIZE =20 
#starting size and position of snake
#snake head is the next move
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
#check if the apple was eaten by the snake  
def apple_eaten(APPLE_SPAWNED):

    if apple_pos[0] == SNAKE_BODY[0][0] and apple_pos[1] ==SNAKE_BODY[0][1]: #comparest apple position to the head of the snake by x and y if botht he same dont pop the sanek and 
        APPLE_SPAWNED =False                                                   #keep extra tail 
     
    else:
        SNAKE_BODY.pop() 
    return APPLE_SPAWNED  
#testing moves the body to the head and tail to the body 
#change x +10 so snake is moving to the right
def read_move(NEXT_MOVE):

   keys_pressed = pygame.key.get_pressed()
   PREVIOUS_MOVE = NEXT_MOVE
 #reads user movement   
   if keys_pressed[pygame.K_LEFT]:
        NEXT_MOVE= "LEFT"
   if keys_pressed[pygame.K_RIGHT]:
        NEXT_MOVE= "RIGHT"      
   if keys_pressed[pygame.K_UP]:    
        NEXT_MOVE= "UP"      
   if keys_pressed[pygame.K_DOWN]:
        NEXT_MOVE= "DOWN"
 #checks if the snake is going backwards
   if NEXT_MOVE == "LEFT" and PREVIOUS_MOVE == "RIGHT":
        NEXT_MOVE = PREVIOUS_MOVE
   if NEXT_MOVE == "RIGHT" and PREVIOUS_MOVE =="LEFT":
        NEXT_MOVE = PREVIOUS_MOVE
   if NEXT_MOVE == "UP" and PREVIOUS_MOVE =="DOWN":
        NEXT_MOVE = PREVIOUS_MOVE
   if NEXT_MOVE == "DOWN" and PREVIOUS_MOVE =="UP":
        NEXT_MOVE = PREVIOUS_MOVE
#this if statements do the movement of the snake
   if NEXT_MOVE == "LEFT":
        SNAKE_HEAD[0] = SNAKE_HEAD[0] - OBJECT_SIZE
   if NEXT_MOVE == "RIGHT":
        SNAKE_HEAD[0] = SNAKE_HEAD[0] + OBJECT_SIZE
   if NEXT_MOVE == "UP":
        SNAKE_HEAD[1] = SNAKE_HEAD[1] - OBJECT_SIZE
   if NEXT_MOVE == "DOWN":
        SNAKE_HEAD[1] = SNAKE_HEAD[1] + OBJECT_SIZE
   if SNAKE_HEAD[0] > WIDTH or SNAKE_HEAD[1] > HEIGHT or SNAKE_HEAD[0] < -0 or SNAKE_HEAD[1] < 0:
        pygame.quit() #kills the game if snake head is out of range 
  #makes the adds the new head to the snake and pops the old tail
   for Position in SNAKE_BODY:  
        if Position[0] == SNAKE_HEAD[0] and Position[1] == SNAKE_HEAD[1]:
            pygame.quit()      
   SNAKE_BODY.insert(0,list(SNAKE_HEAD))
   draw_snake()
   pygame.display.update()  
   return NEXT_MOVE

def kill_snake(run):#kills the snake of the edge is out of the screen
    for Position in SNAKE_BODY:
        if Position[0] > WIDTH or Position[1] > HEIGHT or Position[0] < 0 or Position[1] <0:
            run = False
        else: 
            run = True
    return run
            
#main   
run = True
clock = pygame.time.Clock()
while run: 
   clock.tick(FPS)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
   win.fill((BLACK)) #refreshes screen to delete old moves
   draw_snake()
   #draws apple if not spawned
   if APPLE_SPAWNED == False:
        apple_pos=[randomx(),randomy()]
        for Position in SNAKE_BODY:  
            if apple_pos[0] == Position[0] and apple_pos[1] == Position[1]: #check to see if the apple does not spawn in the snakes body
                apple_pos=[randomx(),randomy()]
        apple_draw= pygame.draw.rect(win,RED,pygame.Rect(apple_pos[0],apple_pos[1],OBJECT_SIZE ,OBJECT_SIZE ))#check if the appple spwan possition is one of the body if true then spawn again
        APPLE_SPAWNED= True
   else:
        apple_draw= pygame.draw.rect(win,RED,pygame.Rect(apple_pos[0],apple_pos[1],OBJECT_SIZE ,OBJECT_SIZE ))
    
   #reads the user move ands updates NEXT_MOVE
   NEXT_MOVE = read_move(NEXT_MOVE) 
   #if apple is eaten update apple spawn to false
   APPLE_SPAWNED= apple_eaten(APPLE_SPAWNED)
 
 

   pygame.display.update()
        
pygame.quit()


