import pygame
import random
#pygame window size
WIDTH , HEIGHT = 900,500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake game")
FPS = 30


#size of the objects
SNAKE_BODY_HEIGHT = 10
SNAKE_BODY_WIDTH = 10
APPLE_HEIGHT =10
APPLE_WIDTH =10

#starting size and position of snake
#snake head is the next move
NEXT_MOVE= "RIGHT"
SNAKE_HEAD= [10,50]
SNAKE_BODY = [[10,50],[10,60],[10,70]]

#colors of the game
GREEN = (0,255,0)
BLACK = (0,0,0)
RED = (255,0,0)


#draws the snake 
def draw_snake():
   
    for Position in SNAKE_BODY:
        snake_draw = pygame.draw.rect(win,GREEN,pygame.Rect(Position[0],Position[1],SNAKE_BODY_WIDTH,SNAKE_BODY_HEIGHT ))
#draws the apple
#currently drawing infinte apples
def draw_apple():
    
    apple_pos=[random.randint(0,WIDTH),random.randint(0,HEIGHT)]
    apple_draw= pygame.draw.rect(win,RED,pygame.Rect(apple_pos[0],apple_pos[1],SNAKE_BODY_WIDTH,SNAKE_BODY_HEIGHT ))
       
#check if the apple was eaten by the snake  
def apple_eaten(apple_pos):
    if apple_pos[0] == SNAKE_BODY[0][0] and apple_pos[1] ==SNAKE_BODY[0][1]: #comparest apple position to the head of the snake by x and y
        draw_apple()
#testing moves the body to the head and tail to the body 
#change x +10 so snake is moving to the right
def read_move(NEXT_MOVE):

   keys_pressed = pygame.key.get_pressed()
     
   if keys_pressed[pygame.K_LEFT]:
        NEXT_MOVE= "LEFT"
   if keys_pressed[pygame.K_RIGHT]:
        NEXT_MOVE= "RIGHT"      
   if keys_pressed[pygame.K_UP]:    
        NEXT_MOVE= "UP"      
   if keys_pressed[pygame.K_DOWN]:
        NEXT_MOVE= "DOWN"
 
   if NEXT_MOVE == "LEFT":
        SNAKE_HEAD[0] = SNAKE_HEAD[0] - 10
   if NEXT_MOVE == "RIGHT":
        SNAKE_HEAD[0] = SNAKE_HEAD[0] + 10
   if NEXT_MOVE == "UP":
        SNAKE_HEAD[1] = SNAKE_HEAD[1] - 10
   if NEXT_MOVE == "DOWN":
        SNAKE_HEAD[1] = SNAKE_HEAD[1] + 10
   SNAKE_BODY.insert(0,list(SNAKE_HEAD))
   SNAKE_BODY.pop()
   return NEXT_MOVE

   
run = True
clock = pygame.time.Clock()
while run: 
   clock.tick(FPS)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
   win.fill((BLACK)) #refreshes screen to delete old moves
   draw_snake()
   draw_apple()
   NEXT_MOVE = read_move(NEXT_MOVE)
   pygame.display.update()
        
pygame.quit()


