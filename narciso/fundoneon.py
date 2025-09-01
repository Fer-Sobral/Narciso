import pygame
import random
import sys
import math


pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Fundo Neon Dinâmico com Formas")
clock = pygame.time.Clock()

#rgb
CORES_NEON = [
    (57, 255, 20),     #verde neon
    (0, 255, 255),     #azul neon
    (255, 20, 147),    #rosa neon
    (0, 191, 255),     #azul claro neon
    (255, 0, 255),     #magenta neon
]


FORMAS = ["circulo", "quadrado", "triangulo"]

class FormaFlutuante:
    def __init__(self):
        self.reset()

    def reset(self):
        self.forma = random.choice(FORMAS)
        self.x = random.randint(0, largura)
        self.y = random.randint(0, altura)
        self.tamanho = random.randint(10, 20)
        self.velocidade = random.uniform(0.2, 1.0)
        self.cor = random.choice(CORES_NEON)
        self.transparencia = random.randint(60, 150)

    def atualizar(self):
        self.y -= self.velocidade
        self.transparencia -= 0.5

        if self.y < -self.tamanho or self.transparencia <= 0:
            self.reset()

    def desenhar(self, superficie):
        forma_surf = pygame.Surface((self.tamanho*2, self.tamanho*2), pygame.SRCALPHA)

        if self.forma == "circulo":
            pygame.draw.circle(
                forma_surf,
                (*self.cor, int(self.transparencia)),
                (self.tamanho, self.tamanho),
                self.tamanho
            )

        elif self.forma == "quadrado":
            pygame.draw.rect(
                forma_surf,
                (*self.cor, int(self.transparencia)),
                (0, 0, self.tamanho*2, self.tamanho*2)
            )

        elif self.forma == "triangulo":
            meio = self.tamanho
            pontos = [
                (meio, 0),  #topo
                (0, self.tamanho*2),  #canto inferior esquerdo
                (self.tamanho*2, self.tamanho*2)  #canto inferior direito
            ]
            pygame.draw.polygon(
                forma_surf,
                (*self.cor, int(self.transparencia)),
                pontos
            )

        superficie.blit(forma_surf, (self.x - self.tamanho, self.y - self.tamanho))


formas = [FormaFlutuante() for _ in range(60)]


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill((0, 0, 0))  
    
    for f in formas:
        f.atualizar()
        f.desenhar(tela)

    pygame.display.flip()
    clock.tick(60)