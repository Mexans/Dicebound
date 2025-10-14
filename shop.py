import pygame
from dice import Die

def shop(money, dice_list):
    """Boutique visuelle minimaliste"""
    clock = pygame.time.Clock()
    running = True
    selected = 0

    # Définir les articles de la boutique
    SHOP_ITEMS = [
        {"name": "Dé Rouge", "price": 150, "type": "rouge"},
        {"name": "Dé Bleu", "price": 100, "type": "bleu"},
        {"name": "Dé Doré", "price": 250, "type": "doré"}
    ]

    screen = pygame.display.get_surface()
    font = pygame.font.Font(None, 36)

    while running:
        screen.fill((15, 15, 25))

        # Titre
        title = font.render("🏪 Boutique", True, (255, 255, 255))
        screen.blit(title, (220, 50))

        # Affichage des items
        for i, item in enumerate(SHOP_ITEMS):
            color = (255, 255, 0) if i == selected else (200, 200, 200)
            text = font.render(f"{item['name']} - {item['price']}💰", True, color)
            screen.blit(text, (180, 150 + i * 40))

        # Argent actuel
        money_text = font.render(f"Argent : {money}", True, (255, 215, 0))
        screen.blit(money_text, (220, 350))

        # Instructions
        instr = font.render("↑/↓ Sélection | ENTER Acheter | ESC Retour", True, (180, 180, 180))
        screen.blit(instr, (80, 380))

        pygame.display.flip()

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(SHOP_ITEMS)
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(SHOP_ITEMS)
                elif event.key == pygame.K_RETURN:
                    item = SHOP_ITEMS[selected]
                    if money >= item["price"]:
                        money -= item["price"]
                        dice_list.append(Die(100 + len(dice_list) * 90, 200, die_type=item["type"]))
                    else:
                        print("💸 Pas assez d'argent")

        clock.tick(30)

    return money, dice_list
