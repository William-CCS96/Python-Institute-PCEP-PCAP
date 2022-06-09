"""Cómo usar pip: un programa de prueba simple"""
# Ahora que pygame es finalmente accesible, podemos intentar usarlo en un programa de prueba muy simple. Comentémoslo brevemente.

        # La línea 1: importa pygame y nos permite usarlo.
        # La línea 3: el programa se ejecutará mientras la variable run sea True.
        # Las líneas 4 y 5: determinan el tamaño de la ventana.
        # La línea 6: inicializa el entorno pygame.
        # La línea 7: prepara la ventana de la aplicación y establece su tamaño.
        # La línea 8: crea un objeto que represente la fuente predeterminada de 48 puntos.
        # La línea 9: crea un objeto que represente un texto dado, el texto será suavizado (True) y blanco (255,255,255).
        # La línea 10: inserta el texto en el búfer de pantalla (actualmente invisible).
        # La línea 11: invierte los búferes de la pantalla para que el texto sea visible.
        # La línea 12: el bucle principal de pygame comienza aquí.
        # La línea 13: obtiene una lista de todos los eventos pendientes de pygame.
        # Las líneas 14 a la 16: revisan si el usuario ha cerrado la ventana o ha hecho clic en algún lugar dentro de ella o ha pulsado alguna tecla.
        # La línea 15: si es así, se deja de ejecutar el código.

import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Bienvenido a pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False
