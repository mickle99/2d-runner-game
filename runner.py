import pygame
from sys import exit

def display_score():
    print('score')
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)

# game intitialisation
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surface = test_font.render('My game', False, 'Black')
#score_rect = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800,300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
# gets rectangle of particular surface
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (400,200))

while True:
    
    # event loop checks all possible player inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    print('collision')
                    if player_rect.bottom >= 300:
                        player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('jump')
                    if player_rect.bottom >= 300:
                        player_gravity = -20
        # restarting the game
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print('enetered')
                game_active = True
                snail_rect.left = 800
                start_time = pygame.time.get_ticks

    # current game state
    if game_active:
        
        # blit score, sky and ground
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        display_score()
        # blit score
        #pygame.draw.rect(screen,'Pink',score_rect)
        #pygame.draw.rect(screen,'Pink',score_rect)
        #screen.blit(score_surface,score_rect)

        # blit snail
        snail_rect.x -= 8
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface,snail_rect)

        # blit player
        # player gravity always moving down exponentially
        # unless reset to -20 jump
        player_gravity += 1
        player_rect.y += player_gravity
        
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    # game state is game over
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

        

    pygame.display.update()
    clock.tick(60)