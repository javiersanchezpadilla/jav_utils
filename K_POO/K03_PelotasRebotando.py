import pygame
import random

pygame.init()
LARGURA, ALTURA = 800, 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption ("Esferas rebotando")

PRETO = (0, 0, 0)

class Esfera:

    def __init__ (self):
        self.x = random.randint (50, LARGURA - 50)
        self.y = random. randint (50, ALTURA - 50)
        self.radio = random.randint (10, 30)
        self.color = [random.randint(0, 255) for _ in range(3)]
        self.vel_x = random.choice([-4, 4])
        self.vel_y = random.choice([-4, 4])

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x - self.radio <= 0 or self.x + self.radio >= LARGURA:
            self.vel_x *= -1
        if self.y - self.radio <= 0 or self.y + self.radio >= ALTURA:
            self.vel_y *= -1


    def desenhar(self, superficie):
        pygame.draw.circle(superficie, self.color, (self.x, self.y), self.radio)

esferas = [Esfera() for _ in range(16)]
clock = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)

    for b in esferas:
        b.mover()
        b.desenhar(tela)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


