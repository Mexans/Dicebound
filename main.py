import pygame
from dice import Die

# 🧩 Initialisation de Pygame
pygame.init()

# 🖥️ Paramètres de la fenêtre
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎲 Dicebound Prototype")

# ⏱️ Horloge et police d'écriture
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# 🎲 Création des dés
dice = [
   Die(100, 150, die_type="normal"),
    Die(190, 150, die_type="rouge"),
    Die(280, 150, die_type="vert"),
    Die(370, 150, die_type="violet"),
    Die(460, 150, die_type="arc_en_ciel")
]
total_score = 0

# 🎨 Couleurs
WHITE = (255, 255, 255)
GREEN = (100, 255, 100)
RED = (255, 100, 100)

round_number = 1       # numéro de la manche
money = 0              # argent du joueur
multiplier = 1         # multiplicateur temporaire

# 🌀 Boucle principale du jeu
running = True
while running:
    screen.fill((40, 40, 40))  # fond gris foncé

    # 🧭 Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        elif event.type == pygame.KEYDOWN:
            # Espace = relance tous les dés non gardés
            if event.key == pygame.K_SPACE:
                for die in dice:
                    die.roll()
                total_score = sum(die.value for die in dice)
                round_number += 1
                 # ✅ Calcul de l'argent
                money += total_score * multiplier

                round_text = font.render(f"Manche : {round_number}", True, WHITE)
                money_text = font.render(f"Argent : {money}", True, GREEN)
                screen.blit(round_text, (20, 20))
                screen.blit(money_text, (20, 50))

                # ✅ Passe à la manche suivante
                round_number = 1
                if die.type == "doré":
                    multiplier = 2
                else:
                    multiplier = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # clic gauche
                for die in dice:
                    if die.rect.collidepoint(event.pos):
                        die.toggle_hold()  # garde/libère le dé

    # 🎨 Affichage des dés
    for die in dice:
        die.draw(screen)

    # 🧾 Affichage du score et des instructions
    score_text = font.render(f"Score total : {total_score}", True, GREEN)
    hint_text = font.render("Appuie sur ESPACE pour lancer les dés", True, RED)
    screen.blit(score_text, (180, 50))
    screen.blit(hint_text, (100, 320))

    round_text = font.render(f"Manche : {round_number}", True, WHITE)
    screen.blit(round_text, (20, 20))
    effects_text = font.render(
    f"Effets actifs : {' | '.join([die.type for die in dice if die.type != 'normal'])}",
    True, (255, 255, 0)
)
    screen.blit(effects_text, (20, 80))

    # 🔄 Mise à jour de l'écran
    pygame.display.flip()
    clock.tick(30)
