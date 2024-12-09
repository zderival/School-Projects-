import pygame
pygame.init()
WIDTH, HEIGHT = 1000, 652
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0, 0, 0))
Black = ((0, 0, 0))
Red = ((255, 0, 0))
white = ((255, 255, 255))
def pause():
    # Set width and height pause screen
    width = 770
    height = 770
    over_screen = pygame.Surface((width, height))
    over_screen.fill(white)
    screen.blit(over_screen, (100, 0))
    # Font
    font = pygame.font.Font("Hitchcut-Regular.ttf", 48)
    pause = font.render("Pause...", True, Black)
    # Blit Font:
    over_screen.blit(pause, (255, 100))
    screen.blit(over_screen, (175, 0))
    # X Button:
    restart_button = pygame.image.load('restart-icon.png').convert_alpha()
    button_surf_width = 150
    button_surf_height = 150
    button_surface = pygame.Surface((button_surf_width, button_surf_height))
    button_rect2 = pygame.draw.circle(screen, (white), (650, 395), 75)
    X_icon = pygame.image.load('X-icon.png').convert_alpha()
    # Resize button
    X_icon_w = int(restart_button.get_width() * 0.330)
    X_icon_h = int(restart_button.get_height() * 0.330)
    X_icon_resize = pygame.transform.scale(X_icon, (X_icon_w, X_icon_h))
    screen.blit(X_icon_resize, (597, 340))
    # Play Button
    button_surf_width = 150
    button_surf_height = 150
    button_surface = pygame.Surface((button_surf_width, button_surf_height))
    button_rect = pygame.draw.circle(screen, (white), (450, 395), 75)
    play_button = pygame.image.load('Play button.png').convert_alpha()
    # Resize button
    restart_button_w = int(restart_button.get_width() * 0.380)
    restart_button_h = int(restart_button.get_height() * 0.380)
    resize_button = pygame.transform.scale(play_button, (restart_button_w, restart_button_h))
    screen.blit(resize_button, (390, 335))
    pygame.display.flip()
    return button_rect,button_rect2
running = True
while running:
    button_rect, button_rect2 = pause()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_rect2.collidepoint((mouse_x, mouse_y)):
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_rect.collidepoint((mouse_x, mouse_y)):
                running = False
    pygame.display.flip()