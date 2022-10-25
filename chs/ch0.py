import sys, time as executionTime
from pygame import *
from chs.tools import OptionColor, fonts, closeDialogueEscene, createButtons, createDialogue, createNarration, drawBees, setBackgroundImage

init()
clock, execution, bees, screen = time.Clock(), 0, None, None
info = (fonts[1].render("Prólogo.", True, OptionColor.BASE.value), fonts[2].render("Xunán Kab: Los antiguos mayas y la miel.", True, OptionColor.BASE.value))
text = ["Los grupos mayas de Yucatán desarrollaron éxitosamente el arte de criar abejas domesticadas por ellos (Melipona beecheii, una especie perteneciente a la familia de los Meliponinae o meliponinos). Se trata de un insecto sin aguijón, conocido como Xunán Kab; estas abejas se desarrollan en el área de Centroamérica y México. Asimismo, poseen una manera original para crear sus nidos, llamados «jobones», en trozos huecos de árboles.\nEn Yucatán, muchos años antes de la introducción de la abeja Apis mellifera (o abeja italiana), las abejas Xunán Kab eran las que se domesticaban y fueron un factor determinante en la economía de los habitantes de la región, ya que su miel no solo endulza, sino que, según las crónicas de la farmacopea maya, tiene propiedades medicinales.", ["¡Mucho gusto, es un placer conocerte!", "Decide sabiamente y mucha suerte en esta aventura."]]
options = ["Continuar"]
backgroundSound = mixer.Sound("rsc/sound/ES_Simple Pleasantries - Arthur Benson.mp3")
backgroundSound.set_volume(0.2)

def scene1(lastBackgroundSound):
    global bees, screen, text
    backgroundImage = image.load("rsc/img/landscape/ch0-sc1.png")
    bee = [transform.scale(image.load("rsc/img/bee/queen.png"), (180, 180)), None]
    time = executionTime.time() + 0.3
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        if execution > executionTime.time():
            screen[0].fill(OptionColor.HOVERED.value)
            screen[0].blit(info[0], (screen[1][1][0]//2 - info[0].get_width()//2, screen[1][1][1]//2 - 50))
            screen[0].blit(info[1], (screen[1][1][0]//2 - info[1].get_width()//2, screen[1][1][1]//2))
            if time < executionTime.time():
                lastBackgroundSound.set_volume(lastBackgroundSound.get_volume() - 0.01)
                time+=0.3
        else:
            if bees == None:
                lastBackgroundSound.stop()
                mixer.Sound.play(backgroundSound, -1)
                dialogue = 0
            backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
            screen[0].blit(backgroundImage, (0, 0))
            bees = drawBees(screen[0], screen[1][0], 25, bees)
            reason = createNarration(screen[0], screen[1][1], text[0])[1]
            button = createButtons(screen[0], screen[1][1], options, None)
            bee[1] = (screen[1][1][0]//2 - bee[0].get_width()//2, reason + (screen[1][1][1] - reason - bee[0].get_height())//3)
            screen[0].blit(bee[0], bee[1])
            if dialogue == 0: dialogue = createDialogue(screen[0], bee, text[1][0], None, False, (2, 28))
            else: createDialogue(screen[0], bee, text[1][1], 200, False, None)
            for e in event.get():
                if e.type == QUIT:
                    quit()
                    sys.exit()
                if e.type == MOUSEBUTTONDOWN and e.button==1:
                    if button.collidepoint(mouse.get_pos()):
                        closeDialogueEscene()
                        text = ["Para los mayas, la miel también fue un ingrediente de gran importancia para la preparación de las bebidas ceremoniales, sobre todo las relacionadas con el maíz. Durante la época prehispánica y la colonia, los excedentes de miel y cera fueron comercializados e intercambiados en regiones cercanas a la Península.\nDe la Xunán Kab obtenían la miel que los mayas usaban como edulcorante y como medicina, además de la cera con la que elaboraban velas.\nOriginalmente, la abeja Xunán Kab era considerada como un regalo de los dioses y por ello era cuidada y reverenciada por meliponicultores especialmente entrenados, gracias a esto la técnica para criar a la Melipona beecheii sigue siendo como en el pasado."]
                        return 2
        display.flip()

def scene2():
    global bees, screen, text
    backgroundImage = image.load("rsc/img/landscape/ch0-sc2.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        bees = drawBees(screen[0], screen[1][0], 25, bees)
        createNarration(screen[0], screen[1][1], text[0])
        button = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                if button.collidepoint(mouse.get_pos()):
                    text = ["Actualmente, esta producción ha sido una alternativa productiva con buenas posibilidades de comercialización. Además, la extracción de la miel y el polen se hace de manera manual apegada a la tradición.\nDesde la domesticación de las abejas, como en el manejo de su producto, se mantiene un equilibrio ecológico, ya que se procura reforestar grandes áreas que promueven el desarrollo de esta especie animal amenazada por el ser humano."]
                    return 3
        display.flip()

def scene3():
    global bees, screen, text, options
    backgroundImage = image.load("rsc/img/landscape/ch0-sc3.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        bees = drawBees(screen[0], screen[1][0], 25, bees)
        createNarration(screen[0], screen[1][1], text[0])
        button = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                if button.collidepoint(mouse.get_pos()):
                    text = [None, ["Hola, mi nombre es Pech.", "Necesitaré tu ayuda durante esta historia.", "¿Estás listo para comenzar?", "Tómate tu tiempo, soy paciente...", ". . .", "¡Solamente presiona el botón!"]]
                    options = ["¡Comencemos!"]
                    return 4
        display.flip()

def scene4():
    global bees, screen
    backgroundImage = image.load("rsc/img/landscape/cover.jpg")
    pech = [transform.scale(image.load("rsc/img/bee/pech/happy.png"), (275, 275)), None]
    dialogue = 0
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        bees = drawBees(screen[0], screen[1][0], 25, bees)
        pech[1] = (screen[1][1][0]//2 - pech[0].get_width()//2, screen[1][1][1]//2 - pech[0].get_height()//2)
        screen[0].blit(pech[0], pech[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], pech, text[1][0], None, True, (0.5, 2.5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], pech, text[1][1], 200, True, (0.25, 3.25))
        elif dialogue == 2: dialogue = createDialogue(screen[0], pech, text[1][2], None, True, (0.5, 29.5))
        elif dialogue == 3:
            pech[0] = transform.scale(image.load("rsc/img/bee/pech/grave.png"), (275, 275))
            dialogue = createDialogue(screen[0], pech, text[1][3], None, True, (1, 19))
        elif dialogue == 4: dialogue = createDialogue(screen[0], pech, text[1][4], None, True, (1, 9))
        else:
            pech[0] = transform.scale(image.load("rsc/img/bee/pech/happy.png"), (275, 275))
            createDialogue(screen[0], pech, text[1][5], None, True, None)
        if dialogue > 1: button = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if dialogue > 1 and e.type == MOUSEBUTTONDOWN and e.button==1:
                if button.collidepoint(mouse.get_pos()):
                    closeDialogueEscene()
                    return [1, backgroundSound]
        display.flip()

def start(mainSurface, backgroundSound):
    global screen
    screen = mainSurface
    scene1(backgroundSound)
    scene2()
    scene3()
    return scene4()