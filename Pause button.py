import pygame
pygame.init()
WIDTH,HEIGHT = 200,200
white = ((225,225,225))
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(white)
def pause_button():
    pause_button = pygame.image.load('Pause game.jpg').convert_alpha()
    pause_button_w = int(pause_button.get_width() * 0.38)
    pause_button_h = int(pause_button.get_height() * 0.38)
    button_resize = pygame.transform.scale(pause_button, (pause_button_w, pause_button_h))
    screen.blit(button_resize, (53,45))
    pause_button_rect = pygame.Rect(53,45,pause_button_w,pause_button_h)
    pygame.display.flip()
    return pause_button_rect
running = True
paused = False
while running:
    pause_button_rect = pause_button()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pause_button_rect.collidepoint(mouse_pos):
                paused = True
            if paused:
                from Pause import pause
    pygame.display.flip()
