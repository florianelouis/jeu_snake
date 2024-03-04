import pygame
from random import randint
import mes_fonctions as mfn
# initianlisation des variables
pygame.init()



##############################################################################
# avant de commencer
##############################################################################

# on définit la taille de l'écran 60 cases de 16 pixels par 40 cases de 16 pixels
width, height = 16*60, 16*40
# on définit l'écran
ecran = pygame.display.set_mode((width, height))
# vitesse d'affichage pour l'animation
horloge = pygame.time.Clock()

# on charge les images
anneau = pygame.image.load("images/violet.png").convert_alpha()
champignon = pygame.image.load("images/champignonviolet.png").convert_alpha()
pomme = pygame.image.load("images/pommeviolette.png").convert_alpha()
mur = pygame.image.load("images/murbleu.png").convert_alpha()

# pour écrire on déinfit une fonte de caractères et sa taille
font = pygame.font.SysFont(None, 24)



##############################################################################
# on définit le snake comme une liste
##############################################################################

# création du snake, attention la tête est en dernière position
snake = [[width//2+i*16, height//2] for i in range(3)]


# déplacement par défaut de 16 pixels vers la droite et 0 pixel vers le bas
deplacement = [16,0]



##############################################################################
# on définit la liste des aliments
##############################################################################
champignons = [[randint(1,59)*16,randint(1,39)*16] for i in range(5)]
pommes = [[randint(1,59)*16,randint(1,39)*16] for i in range(1)]



##############################################################################
# on commence l'animation
##############################################################################

continuer = True

while continuer:
    # nombre d'images par seconde : ici 10 images/s
    # en général c'est plutôt 30 ou 60 images/s
    horloge.tick(7)
    # rafraichissement de l'image pour éviter les superpositions
    # ici on remet un feuille blanche
    pygame.draw.rect(ecran, (000, 150, 255), (0, 0, width, height))
    # un cadre en mur de murs
    for x in range(0,width,16):
        # ligne du haut
        ecran.blit(mur, [x,0])
        # ligne du bas
        ecran.blit(mur, [x,height-16])
    for y in range(1,height-16,16):
        # ligne de gauche
        ecran.blit(mur, [0,y])
        # ligne de droite
        ecran.blit(mur, [width-16,y])


    # gestion des événements
    for event in pygame.event.get():
        # pour quitter le jeu
        if event.type == pygame.QUIT:
            continuer = False
        # pour diriger le snake en changeant de direction uniquement quand on presse une touche flèche
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                deplacement = [-16,0]
            elif event.key == pygame.K_RIGHT:
                deplacement = [16,0]
            elif event.key == pygame.K_UP:
                deplacement = [0,-16]
            elif event.key == pygame.K_DOWN:
                deplacement = [0,16]
            # pas de else :



    # gestion des collisions et déplacement
    trouve = mfn.manger_champignon(snake, deplacement, champignons, width, height)
    aie = mfn.manger_snake(snake, deplacement, width, height)
    if aie :
        continuer = False
    elif  trouve != -1 :
        # le snake a mangé un champignon, il doit grandir d'une tête
        # on rajoute un anneau au snake
        snake.append(champignons[trouve])
        # on déplace le champignon
        champignons[trouve] = [randint(1,59)*16,randint(1,39)*16]
    else :
        # deplacement du snake
        mfn.avancer(snake, deplacement, width, height)


    # affichage des champignons
    for i in range(len(champignons)):
        ecran.blit(champignon, champignons[i])



    # gestion des collisions et déplacement
    trouve = mfn.manger_pomme(snake, deplacement, pommes, width, height)
    aie = mfn.manger_snake(snake, deplacement, width, height)
    if aie :
        continuer = False
    elif  trouve != -1 :
        # le snake a mangé une pomme, il doit grandir de trois têtes
        # on rajoute trois anneaux au snake
        snake.append(pommes[trouve])
        snake.append(pommes[trouve])
        snake.append(pommes[trouve])
        # on déplace la pomme
        pommes[trouve] = [randint(1,59)*16,randint(1,39)*16]
    else :
        # deplacement du snake
        mfn.avancer(snake, deplacement, width, height)


    # affichage des pommes
    for i in range(len(pommes)):
        ecran.blit(pomme, pommes[i])


    # affichage du snake
    for i in range(len(snake)):
        ecran.blit(anneau, snake[i])


    # on affiche la taille du snake
    score = font.render('taille du snake '+str(len(snake)), True, (0,255,255))
    ecran.blit(score,(25,25))

    # on applique tous ces changements (les blit)
    pygame.display.flip()


pygame.draw.rect(ecran, (0, 150, 255), (0, 0, width, height))
game = font.render('GAME OVER', True, (200,0,200))
ecran.blit(game, game.get_rect(center = (width//2, height//2)))
score = font.render('la taille du snake était de '+str(len(snake)), True, (0,255,255))
ecran.blit(score,score.get_rect(center=(width//2, height//2+20)))
pygame.display.flip()
# pause de 3000 millisecondes soit 3 secondes
pygame.time.wait(3000)
# le programme est fini
pygame.quit()