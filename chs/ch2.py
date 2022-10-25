import sys, time as executionTime
from pygame import *
from chs.tools import OptionColor, fonts, closeDialogueEscene, createButtons, createDialogue, createNarration, drawBees, setBackgroundImage

init()
clock, execution, bees, screen = time.Clock(), 0, None, None
info = (fonts[1].render("Capítulo 2.", True, OptionColor.BASE.value), fonts[2].render("Aru, una vieja amiga.", True, OptionColor.BASE.value))
text = ["Aru ha sido la mejor amiga de Pech durante gran parte de su vida. Ambas se conocieron desde los primeros instantes después de nacer. Desde ese entonces, han sido más que colegas en su rol como abejas obreras.", ["¡Uf!...", "Un respiro más.", "Estoy a punto de colapsar...", "¡No puedo más!", "Y eso que hay menos..."], [". . .", "Sí.", "Tienes razón, nos están exterminando..."]]
options = ["... ¿abejas?", "... ¿flores?", "... ¿néctar?", "... ¿humanos?"]
backgroundSound = (mixer.Sound("rsc/sound/ES_It's Not Me - Arthur Benson.mp3"), mixer.Sound("rsc/sound/forest-5.mp3"))
backgroundSound[0].set_volume(0.1)
backgroundSound[1].set_volume(0.1)
pech, aru = [transform.scale(transform.flip(image.load("rsc/img/bee/pech/happy.png"), True, False), (180, 180)), None], [transform.scale(image.load("rsc/img/bee/aru/worried.png"), (180, 180)), None]

def scene1(lastBackgroundSound):
    global bees, screen, aru, pech
    dialogue, time , backgroundImage = 0, executionTime.time() + 0.3, image.load("rsc/img/landscape/ch2-sc1.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        if execution > executionTime.time():
            screen[0].fill(OptionColor.HOVERED.value)
            screen[0].blit(info[0], (screen[1][1][0]//2 - info[0].get_width()//2, screen[1][1][1]//2 - 50))
            screen[0].blit(info[1], (screen[1][1][0]//2 - info[1].get_width()//2, screen[1][1][1]//2))
            if time < executionTime.time():
                lastBackgroundSound.set_volume(lastBackgroundSound.get_volume() - 0.01)
                time += 0.3
        else:
            if bees == None:
                lastBackgroundSound.stop()
                mixer.Sound.play(backgroundSound[0], -1)
                mixer.Sound.play(backgroundSound[1], -1)
            backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
            screen[0].blit(backgroundImage, (0, 0))
            bees = drawBees(screen[0], screen[1][0], 25, bees)
            reason = createNarration(screen[0], screen[1][1], text[0])[1]
            aru[1] = (screen[1][1][0]//4 - aru[0].get_width()//4, reason + (screen[1][1][1] - reason - aru[0].get_height())//3)
            pech[1] = (3*screen[1][1][0]//4 - 3*pech[0].get_width()//4, reason + (screen[1][1][1] - reason - pech[0].get_height())//3)
            screen[0].blit(aru[0], aru[1])
            screen[0].blit(pech[0], pech[1])
            if dialogue == 0: dialogue = createDialogue(screen[0], aru, text[1][0], None, True, (5, 5))
            elif dialogue == 1: dialogue = createDialogue(screen[0], aru, text[1][1], None, True, (0.5, 2.5))
            elif dialogue == 2: dialogue = createDialogue(screen[0], aru, text[1][2], None, True, (0.5, 2.5))
            elif dialogue == 3: dialogue = createDialogue(screen[0], aru, text[1][3], None, True, (0.5, 2.5))
            elif dialogue == 4: dialogue = createDialogue(screen[0], aru, text[1][4], None, True, (0.5, 2.5))
            else:
                createDialogue(screen[0], aru, text[1][4], None, True, None)
                createDialogue(screen[0], pech, text[2][0], None, False, None)
                buttons = createButtons(screen[0], screen[1][1], options, None)
            for e in event.get():
                if e.type == QUIT:
                    quit()
                    sys.exit()
                if dialogue > 4 and e.type == MOUSEBUTTONDOWN and e.button==1:
                    closeDialogueEscene()
                    pech[0], aru[0] = transform.scale(transform.flip(image.load("rsc/img/bee/pech/grave.png"), True, False), (180, 180)), transform.scale(image.load("rsc/img/bee/aru/worried.png"), (180, 180))
                    for index in range(len(buttons)):
                        if buttons[index].collidepoint(mouse.get_pos()):
                            if index == 0:
                                text[1] = ["¡Nos están aniquilando!", "Parece que no basta con hacerse cargo de la colmena, alimentar y cuidar a las hermanas, producir bastante cera, ir en búsqueda de néctar para la miel...", "Sí... Esto debe ser por culpa de..."]
                                return 2
                            elif index == 1 or index == 2:
                                text[1] = ["Todo esto debe ser culpa de..."]
                                return 2.3
                            elif index == 3:
                                text[1] = ["¿En serio?", "Estás bromeando, ¿verdad?", "Sería mejor si así fuera..."]
                                return 2.2
        display.flip()

def scene2_0():
    global bees, screen, aru, pech
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch2-sc1.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        bees = drawBees(screen[0], screen[1][0], 25, bees)
        aru[1] = (screen[1][1][0]//4 - aru[0].get_width()//4, (screen[1][1][1] - aru[0].get_height())//3)
        pech[1] = (3*screen[1][1][0]//4 - 3*pech[0].get_width()//4, (screen[1][1][1] - pech[0].get_height())//3)
        screen[0].blit(aru[0], aru[1])
        screen[0].blit(pech[0], pech[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], aru, text[1][0], None, True, (0.5, 2.5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], aru, text[1][1], 200, True, (0.5, 6.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], pech, text[2][1], None, False, (0.5, 2.5))
        elif dialogue == 3: dialogue = createDialogue(screen[0], pech, text[2][2], 200, False, (0.5, 4.5))
        elif dialogue == 4: dialogue = createDialogue(screen[0], aru, text[1][2], None, True, (0.5, 2.5))
        else:
            createDialogue(screen[0], aru, text[1][2], None, True, None)
            createDialogue(screen[0], pech, text[2][0], None, False, None)
            buttons = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if dialogue > 4 and e.type == MOUSEBUTTONDOWN and e.button==1:
                closeDialogueEscene()
                aru[0] = transform.scale(image.load("rsc/img/bee/aru/angry.png"), (180, 180))
                for index in range(len(buttons)):
                    if buttons[index].collidepoint(mouse.get_pos()):
                        if index < 3:
                            text[1] = ["¿Puedes tomarte esto con un poco de seriedad?", "¿Te has puesto a pensar cuán difícil es ser una abeja obrera?", "Ni siquiera es suficiente el defender la colmena, nutrir a los pequeños, reforzar la colmena, ni  recorrer cientos de flores para obtener la miel..."]
                            text[2][2] = "¡Están acabando con nosotras!"
                            return 2.1
                        else: return 3
        display.flip()

def scene2_1():
    global bees, screen, aru, pech
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch2-sc1.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        bees = drawBees(screen[0], screen[1][0], 25, bees)
        aru[1] = (screen[1][1][0]//4 - aru[0].get_width()//4, (screen[1][1][1] - aru[0].get_height())//3)
        pech[1] = (3*screen[1][1][0]//4 - 3*pech[0].get_width()//4, (screen[1][1][1] - pech[0].get_height())//3)
        screen[0].blit(aru[0], aru[1])
        screen[0].blit(pech[0], pech[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], aru, text[1][0], 200, True, (0.5, 2.5))
        elif dialogue == 1:
            dialogue = createDialogue(screen[0], aru, text[1][1], 200, True, (0.5, 3.5))
            pech[0] = transform.scale(transform.flip(image.load("rsc/img/bee/pech/sad.png"), True, False), (180, 180))
        elif dialogue == 2: dialogue = createDialogue(screen[0], aru, text[1][2], 200, True, (0.5, 6.5))
        elif dialogue == 3: dialogue = createDialogue(screen[0], pech, text[2][1], None, False, (0.5, 2.5))
        elif dialogue == 4: dialogue = createDialogue(screen[0], pech, text[2][2], None, False, (0.5, 3.5))
        else:
            closeDialogueEscene()
            return 3
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
        display.flip()

def scene2_2():
    global bees, screen, aru, pech
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch2-sc1.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        bees = drawBees(screen[0], screen[1][0], 25, bees)
        aru[1] = (screen[1][1][0]//4 - aru[0].get_width()//4, (screen[1][1][1] - aru[0].get_height())//3)
        pech[1] = (3*screen[1][1][0]//4 - 3*pech[0].get_width()//4, (screen[1][1][1] - pech[0].get_height())//3)
        screen[0].blit(aru[0], aru[1])
        screen[0].blit(pech[0], pech[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], aru, text[1][0], None, True, (0.5, 2.5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], aru, text[1][1], None, True, (0.5, 2.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], aru, text[1][2], None, True, (0.5, 2.5))
        else:
            closeDialogueEscene()
            return 3
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
        display.flip()

def scene2_3():
    global bees, screen, aru, pech
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch2-sc1.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        bees = drawBees(screen[0], screen[1][0], 25, bees)
        aru[1] = (screen[1][1][0]//4 - aru[0].get_width()//4, (screen[1][1][1] - aru[0].get_height())//3)
        pech[1] = (3*screen[1][1][0]//4 - 3*pech[0].get_width()//4, (screen[1][1][1] - pech[0].get_height())//3)
        screen[0].blit(aru[0], aru[1])
        screen[0].blit(pech[0], pech[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], aru, text[1][0], None, True, (0.5, 2.5))
        else:
            createDialogue(screen[0], aru, text[1][0], None, True, None)
            createDialogue(screen[0], pech, text[2][0], None, False, None)
            buttons = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if dialogue > 0 and e.type == MOUSEBUTTONDOWN and e.button==1:
                closeDialogueEscene()
                aru[0] = transform.scale(image.load("rsc/img/bee/aru/angry.png"), (180, 180))
                for index in range(len(buttons)):
                    if buttons[index].collidepoint(mouse.get_pos()):
                        if index < 3:
                            text[1] = ["¿Por qué no puedes tomarte esto seriamente?", "¿Has pensado cuán agotador es ser una de nosotras?", "Ni siquiera es suficiente recorrer cientos de kilómetros para buscar néctar, criar a los pequeños, ¡ni  mucho menos ser la especie de abeja sin contar con un aguijón!..."]
                            text[2][2] = "Esto no suena nada bien."
                            return 2.1
                        else:
                            return 3
        display.flip()

def scene3():
    global screen, text
    dialogue, backgroundImage, aru, bee = 0, image.load("rsc/img/landscape/ch2-sc3-0.png"), [transform.scale(image.load("rsc/img/bee/aru/baby.png"), (85, 85)), None], [[transform.scale(transform.flip(image.load("rsc/img/bee/worker.png"), True, False), (85, 85)), None] for index in range(3)]
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        reason = createNarration(screen[0], screen[1][1], text[0])[1]
        aru[1] = (screen[1][1][0]//4 - aru[0].get_width()//4, reason + (screen[1][1][1] - reason - aru[0].get_height())//3)
        bee[0][1] = (5*screen[1][1][0]//8 - 5*bee[0][0].get_width()//8, reason + (screen[1][1][1] - reason - bee[0][0].get_height())//3)
        bee[1][1] = (3*screen[1][1][0]//4 - 3*bee[1][0].get_width()//4, reason + 2*(screen[1][1][1] - reason - bee[1][0].get_height())//3)
        bee[2][1] = (7*screen[1][1][0]//8 - 7*bee[2][0].get_width()//8, reason + (screen[1][1][1] - reason - bee[2][0].get_height())//3)
        screen[0].blit(aru[0], aru[1])
        screen[0].blit(bee[0][0], bee[0][1])
        screen[0].blit(bee[1][0], bee[1][1])
        screen[0].blit(bee[2][0], bee[2][1])
        if dialogue == 0: dialogue = createDialogue(screen[0], aru, text[1][0], None, True, (7, 5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], aru, text[1][1], 200, True, (0.5, 3.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], aru, text[1][2], None, True, (0.5, 3.5))
        elif dialogue == 3: dialogue = createDialogue(screen[0], bee[1], text[2][0], None, False, (0.5, 2.5))
        elif dialogue == 4: dialogue = createDialogue(screen[0], bee[1], text[2][1], None, False, (0.5, 2.5))
        elif dialogue == 5: dialogue = createDialogue(screen[0], bee[2], text[3][0], 200, False, (0.5, 2.5))
        else:
            closeDialogueEscene()
            text = ["A lo lejos, vio como un grupo de humanos se preparaban para realizar ciertas acciones que nunca antes había visto. Instantes después de su llegada, solamente pudo observar cómo sus mentores eran capturados. Desgraciadamente, ella jamás volvió a saber algo de ellos.", ["¡¿Qué está ocurriendo?!", "¡¿A dónde se los llevan?!", "¡Nooooo!"], ["¡No puede ser!", "¡Sal de aquí, Aru!", "¡Vamos! ¡Huye!"]]
            return [4, [aru, bee[2]]]
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
        display.flip()

def scene4(characters):
    global screen, text, options
    dialogue, backgroundImage, aru, bee = 0, image.load("rsc/img/landscape/ch2-sc3-1.png"), characters[0], characters[1]
    aru[0] = transform.scale(image.load("rsc/img/bee/aru/scared.png"), (85, 85))
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        reason = createNarration(screen[0], screen[1][1], text[0])[1]
        aru[1] = (screen[1][1][0]//4 - aru[0].get_width()//4, reason + (screen[1][1][1] - reason - aru[0].get_height())//3)
        screen[0].blit(aru[0], aru[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], bee, text[2][0], None, True, (7, 2.5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], bee, text[2][1], None, True, (0.5, 3.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], bee, text[2][2], None, True, (0.5, 3.5))
        elif dialogue == 3: dialogue = createDialogue(screen[0], aru, text[1][0], None, True, (0.5, 2.5))
        elif dialogue == 4: dialogue = createDialogue(screen[0], aru, text[1][1], None, True, (0.5, 2.5))
        elif dialogue == 5: dialogue = createDialogue(screen[0], aru, text[1][2], None, True, (0.5, 6.5))
        else:
            closeDialogueEscene()
            text = [None, ["¡Noooooooooo!", "Por favor, dime que no vienen por nosotras.", "Por favor..."], ["Todo está bien, tranquila.", ". . ."]]
            options = ["Relájate.", "Todo estará bien.", "Deberíamos regresar."]
            return 5
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
        display.flip()

def scene5_0():
    global bees, screen, text, aru, pech
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch2-sc1.png")
    pech[0], aru[0] = transform.scale(transform.flip(image.load("rsc/img/bee/pech/worried.png"), True, False), (180, 180)), transform.scale(image.load("rsc/img/bee/aru/scared.png"), (180, 180))
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        bees = drawBees(screen[0], screen[1][0], 25, bees)
        aru[1] = (screen[1][1][0]//4 - aru[0].get_width()//4, (screen[1][1][1] - aru[0].get_height())//3)
        pech[1] = (3*screen[1][1][0]//4 - 3*pech[0].get_width()//4, (screen[1][1][1] - pech[0].get_height())//3)
        screen[0].blit(aru[0], aru[1])
        screen[0].blit(pech[0], pech[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], aru, text[1][0], None, True, (0.5, 2.5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], pech, text[2][0], None, False, (0.5, 2.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], aru, text[1][1], 200, True, (0.5, 2.5))
        elif dialogue == 3: dialogue = createDialogue(screen[0], aru, text[1][2], None, True, (0.5, 2.5))
        else:
            createDialogue(screen[0], aru, text[1][2], None, True, None)
            createDialogue(screen[0], pech, text[2][1], None, False, None)
            buttons = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if dialogue > 3 and e.type == MOUSEBUTTONDOWN and e.button==1:
                closeDialogueEscene()
                backgroundSound[0].stop()
                backgroundSound[1].stop()
                for index in range(len(buttons)):
                    if buttons[index].collidepoint(mouse.get_pos()):
                        if index < 2:
                            text = [None, ["Espera...", "¿A caso los estás defendiendo?"], ["Creo que lo mejor es que regresemos ahora mismo."]]
                            return 5.1
                        else: return 3
        display.flip()

def scene5_1():
    global bees, screen, text, aru, pech
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch2-sc1.png")
    pech[0], aru[0] = transform.scale(transform.flip(image.load("rsc/img/bee/pech/grave.png"), True, False), (180, 180)), transform.scale(image.load("rsc/img/bee/aru/scared.png"), (180, 180))
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        bees = drawBees(screen[0], screen[1][0], 25, bees)
        aru[1] = (screen[1][1][0]//4 - aru[0].get_width()//4, (screen[1][1][1] - aru[0].get_height())//3)
        pech[1] = (3*screen[1][1][0]//4 - 3*pech[0].get_width()//4, (screen[1][1][1] - pech[0].get_height())//3)
        screen[0].blit(aru[0], aru[1])
        screen[0].blit(pech[0], pech[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], aru, text[1][0], None, True, (0.5, 2.5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], aru, text[1][1], None, True, (0.5, 2.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], pech, text[2][0], 200, False, (1, 9))
        else:
            closeDialogueEscene()
            backgroundSound[0].stop()
            backgroundSound[1].stop()
            return 3
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
        display.flip()

def start(mainSurface, backgroundSound):
    global screen, text
    screen = mainSurface
    scene = scene1(backgroundSound)
    if scene == 2:
        scene = scene2_0()
        if scene == 2.1: scene = scene2_1()
    elif scene == 2.2: scene = scene2_2()
    elif scene == 2.3:
        scene = scene2_3()
        if scene == 2.1: scene = scene2_1()
    text = ["Cuando Aru era pequeña, sucedió un hecho que le marcaría de por vida. Un día como cualquier otro fuera de la colmena, mientras ella aprendía el papel que debe seguir toda abeja obrera, fue testigo de una tragedia.", ["¡Qué día tan hermoso!", "Ojalá pueda descansar un buen rato.", "¡Sí, señor!"], ["Venga, Aru.", "Vayamos a aprender cosas nuevas."], ["Qué lindo día para conocer cosas interesantes, ¿no lo creen?"]]
    scene = scene3()
    scene4(scene[1])
    scene = scene5_0()
    if scene == 5.1: scene = scene5_1()
    return scene