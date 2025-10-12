import random
import pygame

class Die:
    def __init__(self, x, y, faces=6, color=(255, 255, 255), die_type="normal"):
        self.faces = faces
        self.value = 1
        self.color = color
        self.rect = pygame.Rect(x, y, 60, 60)
        self.font = pygame.font.Font(None, 36)
        self.held = False
        self.type = die_type

    def roll(self):
        if not self.held:
            self.value = random.randint(1, self.faces)  # ✅ ici random est le module
            if self.type == "rouge":
                self.value *= 2
            elif self.type == "bleu":
                self.value += 50
            elif self.type == "doré":
                self.value += random.randint(100, 200)

    def toggle_hold(self):
        self.held = not self.held

    def draw(self, screen):
        if self.type == "rouge":
            base_color = (255, 100, 100)
        elif self.type == "bleu":
            base_color = (100, 100, 255)
        elif self.type == "doré":
            base_color = (255, 215, 0)
        else:
            base_color = self.color

        draw_color = (180, 180, 255) if self.held else base_color
        pygame.draw.rect(screen, draw_color, self.rect, border_radius=8)
        text = self.font.render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
