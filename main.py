import cv2 as cv
import numpy as np
import pygame
import sys
from RockPaperScissors import evaluate_move

pygame.init() 
moves = ["rock","paper","scissors"]
rock = pygame.image.load('rock.jpg')
paper = pygame.image.load('paper.jpg')
scissors = pygame.image.load('scissors.jpg')

color = [239,228,220]
font_name = 'analoguemedium.ttf'
font = pygame.font.SysFont(font_name, 128)
font2 = pygame.font.SysFont(font_name, 60)
font3 = pygame.font.SysFont(font_name, 30)
font4 = pygame.font.SysFont(font_name, 37)

map = {
    "rock":rock,
    "paper":paper,
    "scissors":scissors
}

def display_move(play):     # maps the play index to the image
    return map[moves[play]]

def wait(i,dim,pos):   # displays the 3...2...1 sequence
    ndim = np.array(dim)
    npos = np.array(pos)
    coord = npos + (ndim/2)
    if i!=4:
        text = font.render('{}'.format(3-i+1), True, [0,0,0], [*color])
        comp_screen.blit(text,coord)                
      

def score(i):  # renders score
    score = font3.render('{}'.format(i), True, [0,0,0], [*color])
    return score 


h = rock.get_height()
w = rock.get_width() 

cam = cv.VideoCapture(0)

FPS = 60


pygame.display.set_caption('Rock Paper Scissors')
# resizable pygame window
screen = pygame.display.set_mode((500,500),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
# screens to display move and camera feed
user_screen = screen.copy()   
comp_screen = screen.copy()

user_won = font2.render('You won!', True, [0,0,0], [*color])
computer_won = font2.render('You lost!', True, [0,0,0], [*color])
no_one = font2.render('Play again!', True, [0,0,0], [*color])
space = font3.render('Press the spacebar to play again.', True, [0,0,0], [*color])
space0 = font3.render('Press the spacebar to play!', True, [0,0,0], [*color])
You = font3.render('You', True, [0,0,0], [*color])
Comp = font3.render('Computer', True, [0,0,0], [*color])

frames = 0
i = 6
games = 0
played = 0
User_score = 0
Comp_score = 0
show_result = False

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    frames+=1
    
    screen.fill([*color])  
    screen_width,screen_height = screen.get_rect().size
    score_height = screen_height//8

    # collecting the video feed and generating a pygame surface for displaying it
    s,full_image = cam.read()
    input_image = (cv.cvtColor(full_image,cv.COLOR_BGR2RGB))[0:300,80:380]
    image = input_image.swapaxes(0, 1)[::-1]
    surf = pygame.surfarray.make_surface(image)
    surf  = pygame.transform.rotozoom(surf,0,2)
    
    user_screen.fill([*color])
    user_screen.blit(surf, (0,10)) 
    comp_screen.fill([*color])
    
    if games == 0: 
        screen.blit(space0,(screen_width//3,120+score_height+screen_height//2))

    if i<=4:
        wait(i,(int(screen_height*w/h/2),int(screen_height/2)), ((screen_width-w)//8,score_height))
        if frames>=30:
            i+=1
            frames = 0

    if i == 5 and games == played+1:
        randmove = np.random.randint(0,3)
        move = display_move(randmove)
        # evaluating the move using the CNN model 
        evalmove = evaluate_move(input_image)

        if (evalmove - randmove)==1 or (evalmove - randmove)==-2:
            winner = user_won
            User_score+=1
        elif  (evalmove - randmove)== -1 or (evalmove - randmove)==2:
            winner = computer_won
            Comp_score+=1
        elif evalmove == randmove:
            winner = no_one

        show_result = True
        played = games 

    
    if show_result:
        comp_screen.blit(move, (0,0)) 
        screen.blit(font4.render('{}'.format(moves[evalmove])+'!', True, [0,0,0], [*color]),(2*screen_width//3,score_height+screen_height//2-screen_height//20)) 

        if frames>30:
            screen.blit(winner,(4*screen_width//10,60+score_height+screen_height//2))
            screen.blit(space,(screen_width//3,120+score_height+screen_height//2))    

    #Displaying the names of players
    screen.blit(You,(int((screen_width-(screen_height/2))),score_height//4))
    screen.blit(Comp,(screen_width//9+int((screen_width-w)/5),score_height//4)) 
    
    #Displaying the score
    screen.blit(score(User_score),(5+int((screen_width-(screen_height/2))),3*score_height//4)) #user
    screen.blit(score(Comp_score),(20+screen_width//9+int((screen_width-w)/5),3*score_height//4)) #comp
    
    # Displaying the moves and cam feed
    screen.blit(pygame.transform.scale(user_screen, (9*screen_height//20,9*screen_height//20)), (int((screen_width-(screen_height/2)))-int(screen_width/8),score_height))
    screen.blit(pygame.transform.scale(comp_screen, (int(1.1*screen_height*w/h/2),int(screen_height/2))), (int((screen_width-w)/5),score_height))
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        elif event.type == pygame.VIDEORESIZE:  # game window resize
            screen = pygame.display.set_mode(event.size, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)   
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # SPACE key pressed
                show_result = False
                i = 1                       # i is for the 3....2....1 sequence
                frames = 0                  # variable that takes care of the delays(like time.sleep())
                games+=1                    
    