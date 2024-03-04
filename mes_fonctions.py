def ou_va_tete(snake, deplacement, width, height):
    '''
    renvoie la future position de la tête du snake pour observer des collisions éventuelles
    '''
    x = snake[-1][0] + deplacement[0]
    y = snake[-1][1] + deplacement[1]
    if x== width :
        x=  0
    elif x == 0 :
        x = width
    elif y == height :
        y = 0
    elif y == 0 :
        y = height
    return [x,y]


def manger_champignon(snake, deplacement, champignons, width, height):
    '''
    renvoie l'index du champignon qui va être mangé après deplacement
    si aucun champignon mangé, renvoie -1
    '''
    ou = ou_va_tete(snake, deplacement, width, height)

    for i in range(len(champignons)):
        if ou == champignons[i] :
            return i
    else :
        return -1

def manger_pomme(snake, deplacement, pommes, width, height):
    '''
    renvoie l'index de la pomme qui va être mangée après déplacement
    si aucune pomme mangée, renvoie -1
    '''
    ou = ou_va_tete(snake, deplacement, width, height)

    for i in range(len(pommes)):
        if ou == pommes[i] :
            return i
    else :
        return -1

def ou_va_tete2(snake2, deplacement, width, height):
    '''
    renvoie la future position de la tête du snake2 pour observer des collisions éventuelles
    '''
    x = snake2[-1][0] + deplacement[0]
    y = snake2[-1][1] + deplacement[1]
    if x== width :
        x=  0
    elif x == 0 :
        x = width
    elif y == height :
        y = 0
    elif y == 0 :
        y = height
    return [x,y]

def manger_snake(snake, deplacement, width, height):
    '''
    renvoie vrai si le snake se mange lui-même
    '''
    ou = ou_va_tete(snake, deplacement, width, height)

    for i in range(len(snake)-1):
        if ou == snake[i]:
            return True
    else :
        return False


def avancer(snake, deplacement, width, height):
    '''
    avance d'une case le snake
    '''
    # corps
    for i in range(len(snake)-1):
        snake[i]=snake[i+1]
    # tete
    snake[-1] = ou_va_tete(snake, deplacement, width, height)