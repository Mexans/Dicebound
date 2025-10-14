import pygame

def intermission_screen(screen, font, round_number, score, money):
    """Affiche l'écran de fin de manche et propose des choix"""
    clock = pygame.time.Clock()
    selected = 0
    options = ["🏪 Aller à la Boutique", "🎯 Manche suivante", "❌ Quitter le jeu"]
    running = True

    while running:
        screen.fill((25, 25, 35))

        # Titre
        title = font.render(f"🧭 Fin de la Manche {round_number}"), True, (255, 255, 255)
        screen.blit(title, (180, 150))

        # Options
        for i, option in enumerate(options):
            color = (255, 255, 0) if i == selected else (200, 200, 200)
            text = font.render(option, True, color)
            screen.blit(text, (220, 250 + i * 50))

        pygame.display.flip()
        
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        return "shop"
                    elif selected == 1:
                        return "next"
                    elif selected == 2:
                        return "quit"
        clock.tick(30)
