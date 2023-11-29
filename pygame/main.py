import pygame
def score():
    global p
    p =int(pygame.time.get_ticks()/221)-time
    b = pygame.font.SysFont('showcardgothic', 22)
    screen_scr = b.render(f"Score:{p}", False, ("Gray"))
    screen.blit(screen_scr,(0,0))

def end_game():
    final_sco = pygame.font.SysFont('simsunextb', 30)
    final_score = final_sco.render(f"Your score:{p}", False, "Red")
    screen.blit(final_score, (280, 190))
def enemy_inc():
    pass

pygame.init()
X=800
Y=400
screen=pygame.display.set_mode((X,Y))
pygame.display.set_caption("Snail")
text_font=pygame.font.SysFont('showcardgothic',26)
text_screen=text_font.render("Runner Game",True,("Green"))
game_end=pygame.font.SysFont('simsunextb',30)
game_over=game_end.render("""GAME OVER PRESS SPACE FOR RESTART""",True,("Red"))

image_1=pygame.image.load("001-olympic.png").convert_alpha()
clock=pygame.time.Clock()
background_music=pygame.mixer.Sound("Fluffing-a-Duck.mp3")
background_music.set_volume(0.5)
background_music.play(loops= -1)
jump_music=pygame.mixer.Sound("208956297.mp3")
jump_music.set_volume(7) #control the volume
falling_sound=pygame.mixer.Sound("175911684.mp3")
falling_sound.set_volume(7)
enemy_get=pygame.image.load("001-ghost.png").convert_alpha()
enemy_scr=enemy_get.get_rect(bottomright=(754,310))
image_ground=pygame.image.load("wallground.jpg").convert_alpha()
player_set=pygame.image.load("001-running.png").convert_alpha()
player_suf=player_set.get_rect(midbottom=(70,310))
time=0
player_gra=0
player_move=0
game_start=True
#game loop
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()


        #get co-ordinates using mousemotion never be deleted it
        if game_start:
            if event.type==pygame.MOUSEMOTION:
                print(event.pos)
            #when jumping a player incresing the score
            #m = (pygame.time.get_ticks()) // 224
            #score(m)


          #Here user control player by pressing keys
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    if player_suf.bottom==305:
                        player_gra=-20
                        jump_music.play()
                if event.key==pygame.K_LEFT:
                    if player_suf.bottom==305:
                        player_move =+ 1
                        player_suf.x=-20
                if event.key==pygame.K_RIGHT:
                    player_move=0
        #When restart the game
        else:

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    time=pygame.time.get_ticks()
                    game_start = True
                    player_gra = -20
                    enemy_scr.x = 790
                    player_suf.x= 23
                    player_move=0
                    #print score after restart the game
                    time=pygame.time.get_ticks()//221
                    #score when game over


#main game loop
    if game_start:
        screen.fill("Black")
        screen.blit(image_1,((100,-20)))
        screen.blit(text_screen,((300, 0)))
        screen.blit(image_ground,((3,300)))
        player_gra +=1
        #player_move+=1
        #player_suf.x =+1
        player_suf.y += player_gra
        player_suf.x += player_move
        if player_suf.bottom >= 300: player_suf.bottom = 305
        screen.blit((player_set),(player_suf))
        if enemy_scr.x <= -150: enemy_scr.x = 790
        screen.blit(enemy_get,enemy_scr)
        #player_suf.left += 1 ;
        enemy_scr.right -=5
        score()


        #game over condition
        if pygame.Rect.colliderect(player_suf,enemy_scr)==True:
            game_start=False
            falling_sound.play()
    #This is game over screen
    else:
        screen.fill("Black")

        screen.blit(game_over,(150,150))
        end_game()
    #how to get collision point using mouse_pos
    #mouse_pos=pygame.mouse.get_pos()
    #if player_suf.collidepoint(mouse_pos):
        #print("collision")

    pygame.display.update()
    clock.tick(60)


