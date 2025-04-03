import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

pre_sky_surface = pygame.image.load('graphics/Gemini_sky_game.jpg').convert()
sky_surface = pygame.transform.scale(pre_sky_surface, (800, 400))
pre_ground_surface = pygame.image.load('graphics/Gemini_ground.jpg').convert()
ground_surface = pygame.transform.scale(pre_ground_surface,(800,400))
text_surface = test_font.render('My game', False, 'black')

pre_snail_surface = pygame.image.load('graphics/snail.jpg').convert_alpha()
snail_surface = pygame.transform.scale(pre_snail_surface,(100,100))
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

pre_player_surface = pygame.image.load('graphics/dragon_character.JPG').convert_alpha()
player_surface = pygame.transform.scale(pre_player_surface,(150,150))
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    player_rect.left += 1
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)