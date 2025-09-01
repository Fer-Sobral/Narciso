import pygame
import sys
import random
from save_system import carregar_jogo
from game_screen import tela_jogo
pygame.init()
LARGURA, ALTURA = 800, 600
tela=pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Narciso")
clock=pygame.time.Clock()
ROXO_NEON = (255, 0, 255)
BRANCO=(255, 255, 255)
PRETO=(0, 0, 0)
CINZA=(180, 180, 180)
fonte=pygame.font.SysFont(None, 20)
CORES_NEON=[
    (57, 255, 20),
    (0, 255, 255),
    (255, 20, 147),
    (0, 191, 255),
    (255, 0, 255),
]


FORMAS = ["circulo", "quadrado", "triangulo"]

class FormaFlutuante:
    def __init__(self):
        self.reset()

    def reset(self):
        self.forma = random.choice(FORMAS)
        self.x = random.randint(0, LARGURA)
        self.y = random.randint(0, ALTURA)
        self.tamanho = random.randint(10, 20)
        self.velocidade = random.uniform(0.2, 1.0)
        self.cor = random.choice(CORES_NEON)
        self.transparencia = random.randint(60, 150)

    def atualizar(self):
        self.y -= self.velocidade
        self.transparencia -= 0.3
        if self.y < -self.tamanho or self.transparencia <= 0:
            self.reset()

    def desenhar(self, superficie):
        forma_surf = pygame.Surface((self.tamanho * 2, self.tamanho * 2), pygame.SRCALPHA)

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
                (0, 0, self.tamanho * 2, self.tamanho * 2)
            )

        elif self.forma == "triangulo":
            meio = self.tamanho
            pontos = [
                (meio, 0),
                (0, self.tamanho * 2),
                (self.tamanho * 2, self.tamanho * 2)
            ]
            pygame.draw.polygon(
                forma_surf,
                (*self.cor, int(self.transparencia)),
                pontos
            )

        superficie.blit(forma_surf, (self.x - self.tamanho, self.y - self.tamanho))


formas = [FormaFlutuante() for _ in range(60)]


def desenhar_botao(texto, x, y, largura, altura):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()
    botao_ret = pygame.Rect(x, y, largura, altura)

    if botao_ret.collidepoint(mouse):
        pygame.draw.rect(tela, ROXO_NEON, botao_ret, border_radius=15)
        if clique[0]:  #se clicou com o botão esquerdo
            return True
    else:
        pygame.draw.rect(tela, PRETO, botao_ret, border_radius=15)

    texto_render = fonte.render(texto, True, BRANCO)
    texto_rect = texto_render.get_rect(center=botao_ret.center)
    tela.blit(texto_render, texto_rect)
    return False



def menu():
    rodando = True
    while rodando:
        
        tela.fill((0, 0, 0))

        
        for forma in formas:
            forma.atualizar()
            forma.desenhar(tela)

        
        if desenhar_botao("Novo Jogo", 300, 200, 200, 60):
            tela_jogo()

        if desenhar_botao("Carregar Jogo", 300, 300, 200, 60):
            carregar_jogo()

        if desenhar_botao("Sair", 300, 400, 200, 60):
            pygame.quit()
            sys.exit()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    menu()