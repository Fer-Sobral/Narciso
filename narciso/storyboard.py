import pygame
import sys

def introducao(tela):
   
    branco = (255, 255, 255)
    preto = (0, 0, 0)

    
    fonte = pygame.font.SysFont(None, 48)

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                
                rodando = False

        tela.fill(branco)
        texto = fonte.render("Tudo pronto! Pressione qualquer tecla...", True, preto)
        rect_texto = texto.get_rect(center=(tela.get_width() // 2, tela.get_height() // 2))
        tela.blit(texto, rect_texto)

        pygame.display.flip()