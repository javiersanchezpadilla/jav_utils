""" Para este ejemplo, se requiere instalar la librería pygame
pip3 install pygame
"""

import pygame
import random

pygame.init()
# Configuración de la pantalla
ancho_pantalla = 400
alto_pantalla = 400
screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
clock = pygame.time.Clock()

carro = pygame.Rect(190, 360, 20, 40)  # Posición y tamaño del carro
obstaculos = []
score = 0   
font = pygame.font.Font(None, 36)

def reset_game():
    global carro, obstaculos, score
    carro.topleft = (190, 360)
    obstaculos.clear()
    score = 0

juego_ejecutandose = True

while juego_ejecutandose:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_ejecutandose = False

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and carro.left > 0:
        carro.x -= 5
    if keys[pygame.K_RIGHT] and carro.right < ancho_pantalla:
        carro.x += 5

    spawn_rate = 0.08 + (score * 0.002) # Aumentar la tasa de aparición de obstáculos con el score
    if random.random() < spawn_rate:
        # obstaculo = pygame.Rect(random.randrange(0, ancho_pantalla - 20), -40, 20, 40)
        # obstaculos.append(obstaculo)
        obstaculos.append(pygame.Rect(random.randrange(0, ancho_pantalla - 20), -40, 20, 40))

    # Generar obstáculos
    if random.randint(1, 20) == 1:  # Aproximadamente un obstáculo cada 20 frames
        obstaculos.append(pygame.Rect(random.randrange(0, ancho_pantalla - 20), 0, 20, 20))

    for obs in obstaculos[:]:
        obs.y += 4 + (score // 10)  # Aumentar velocidad de obstáculos con el score
        if obs.top > alto_pantalla:
            obstaculos.remove(obs)
            score += 1
        if carro.colliderect(obs):
            reset_game()

    screen.fill((0, 0, 0)) # Limpiar pantalla
    pygame.draw.rect(screen, (0, 255, 0), carro)  # Dibujar carro
    for obs in obstaculos:
        pygame.draw.rect(screen, (255, 0, 0), obs)  # Dibujar obstáculos

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

    screen.blit(score_text, (10, 10))           # Mostrar score
    pygame.display.flip()                       # Actualizar pantalla
    clock.tick(60)                              # Limitar a 60 FPS

pygame.quit()

