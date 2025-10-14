import pygame
from dice import Die
from shop import shop

# 🧠 Initialisation Pygame
pygame.init()

# 🖥️ Paramètres de la fenêtre
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎲 Dicebound v0.1d")

# ⏱️ Horloge et police
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# 🎲 Création initiale des dés (uniquement normaux)
dice = [Die(100 + i * 90, 150, die_type="normal") for i in range(5)]

# 💰 Variables de progression
money = 0
total_score = 0
round_number = 1
target_score = 15  # score minimum pour passer la manche
max_rounds = 5

# 🎨 Couleurs
WHITE = (255, 255, 255)
GREEN = (100, 255, 100)
RED = (255, 100, 100)
HUD_BG = (25, 25, 25)

# --------------------------------------------------------
# 📜 FONCTION : Menu post-manche
# --------------------------------------------------------
def post_round_menu(screen, font, round_number, money, total_score):
    """Affiche un écran de fin de manche avec choix Boutique / Continuer"""
    running = True
    choice = None

    while running:
        screen.fill((30, 30, 30))
        text1 = font.render(f"Fin de la manche {round_number}", True, WHITE)
        text2 = font.render(f"Score : {total_score}  |  Argent : {money}", True, GREEN)
        text3 = font.render("Appuie sur [B] pour Boutique  |  [C] pour Continuer", True, RED)

        screen.blit(text1, (120, 120))
        screen.blit(text2, (120, 180))
        screen.blit(text3, (50, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    choice = "shop"
                    running = False
                elif event.key == pygame.K_c:
                    choice = "continue"
                    running = False

        pygame.display.flip()
        clock.tick(30)

    return choice


# --------------------------------------------------------
# 🧩 BOUCLE PRINCIPALE DU JEU
# --------------------------------------------------------
running = True
while running:
    screen.fill((40, 40, 40))

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        elif event.type == pygame.KEYDOWN:
            # Espace = lancer les dés
            if event.key == pygame.K_SPACE:
                for die in dice:
                    die.roll()
                total_score = sum(die.value for die in dice)

                # Vérifie si le joueur a atteint le score requis
                if total_score >= target_score:
                    money += 100  # récompense
                    action = post_round_menu(screen, font, round_number, money, total_score)

                    if action == "shop":
                        money, dice = shop(money, dice)
                    elif action == "continue":
                        round_number += 1
                        total_score = 0
                        if round_number > max_rounds:
                            running = False  # fin du jeu
                else:
                    print("Score insuffisant, rejoue la manche !")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for die in dice:
                    if die.rect.collidepoint(event.pos):
                        die.toggle_hold()

    # HUD en haut de l’écran
    pygame.draw.rect(screen, HUD_BG, pygame.Rect(0, 0, WIDTH, 50))
    hud_text = font.render(
        f"💰 Argent : {money}   🎯 Score : {total_score}   🧭 Manche : {round_number}/{max_rounds}",
        True,
        WHITE
    )
    screen.blit(hud_text, (20, 10))

    # Dessin des dés
    for die in dice:
        die.draw(screen)

    # Texte d’aide
    hint_text = font.render("Appuie sur ESPACE pour lancer les dés", True, RED)
    screen.blit(hint_text, (100, 340))

    pygame.display.flip()
    clock.tick(30)
