import sys, time as executionTime
from pygame import *
from chs.tools import OptionColor, fonts, closeDialogueEscene, createButtons, createDialogue, createNarration, setBackgroundImage

init()
clock, execution, screen = time.Clock(), 0, None
info = (fonts[1].render("Capítulo 1.", True, OptionColor.BASE.value), fonts[2].render("Ley.", True, OptionColor.BASE.value))
text = ["Ey, Ley. Ten cuidado, acabas de pisar algo..."]
options = ["Ver qué he pisado.", "Continuar."]
backgroundSound = mixer.Sound("rsc/sound/forest-5.mp3")
backgroundSound.set_volume(0.05)
ley, ali = [transform.scale(image.load("rsc/img/people/ley/happy.png"), (350, 350)), None], [transform.scale(image.load("rsc/img/people/ali/happy.png"), (500, 500)), None]

def scene1_0(lastBackgroundSound):
    global execution, screen, text, options
    backgroundImage = image.load("rsc/img/landscape/ch1-sc1-0.jpg")
    time = executionTime.time() + 0.3
    while True:
        clock.tick(60)
        screen[1][1] = [display.get_surface().get_width(), display.get_surface().get_height()]
        if execution > executionTime.time():
            screen[0].fill(OptionColor.HOVERED.value)
            screen[0].blit(info[0], (screen[1][1][0]//2 - info[0].get_width()//2, screen[1][1][1]//2 - 50))
            screen[0].blit(info[1], (screen[1][1][0]//2 - info[1].get_width()//2, screen[1][1][1]//2))
            if time < executionTime.time():
                lastBackgroundSound.set_volume(lastBackgroundSound.get_volume() - 0.01)
                time+=0.3
        else:
            if execution != 0:
                lastBackgroundSound.stop()
                mixer.Sound.play(backgroundSound, -1)
                execution = 0
            backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
            screen[0].blit(backgroundImage, (0, 0))
            createNarration(screen[0], screen[1][1], text[0])
            buttons = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                closeDialogueEscene()
                for index in range(len(buttons)):
                    if buttons[index].collidepoint(mouse.get_pos()):
                        if index==0:
                            text = ["Qué anuncio tan curioso, ¿no lo crees?\nSospechoso... Algo huele mal..."]
                            options = ["Continuar."]
                            return 1.1
                        else:
                            return 2
        display.flip()

def scene1_1():
    global screen
    backgroundImage = image.load("rsc/img/landscape/ch1-sc1-1.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        createNarration(screen[0], screen[1][1], text[0])
        button = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                if button.collidepoint(mouse.get_pos()):
                    return 2
        display.flip()

def scene2():
    global screen, text, options, ley, ali
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch1-sc2.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        ley[1] = (screen[1][1][0] - ley[0].get_width(), screen[1][1][1] - ley[0].get_height())
        ali[1] = (0, screen[1][1][1] - ali[0].get_height())
        screen[0].blit(ley[0], ley[1])
        screen[0].blit(ali[0], ali[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], ali, text[1][0], None, True, (1, 2))
        elif dialogue == 1: dialogue = createDialogue(screen[0], ali, text[1][1], None, True, (0.5, 2.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], ali, text[1][2], None, True, (0.5, 2.5))
        elif dialogue == 3: dialogue = createDialogue(screen[0], ley, text[2][0], None, False, (0.5, 2.5))
        elif dialogue == 4: dialogue = createDialogue(screen[0], ley, text[2][1], None, False, (0.5, 2.5))
        elif dialogue == 5: dialogue = createDialogue(screen[0], ley, text[2][2], None, False, (0.5, 2.5))
        elif dialogue == 6:
            ali[0] = transform.scale(image.load("rsc/img/people/ali/worried.png"), (500, 500))
            dialogue = createDialogue(screen[0], ali, text[1][3], None, True, (1, 3))
        elif dialogue == 7:
            ley[0] = transform.scale(image.load("rsc/img/people/ley/scared.png"), (350, 350))
            dialogue = createDialogue(screen[0], ali, text[1][4], None, True, (0.5, 2.5))
        else:
            closeDialogueEscene()
            text = ["Ley y Ali, su madre, son apicultoras mayas como lo ha sido toda su familia desde que se tiene memoria. Ali es madre soltera y ambas viven en una región agrícola del sur de México en donde la percepción plena de la naturaleza y el canto de las aves es habitual.", ["Estos han sido días muy agotadores, la verdad.", "Las cosas no son las mismas que antes, Ley."], ["Entonces, ma'...", "¿Cómo te fue?", ". . ."]]
            options = ["¿Por qué?", "Ya veo.", "¿En serio?"]
            ley[0], ali[0] = transform.scale(image.load("rsc/img/people/ley/sad.png"), (400, 400)), transform.scale(image.load("rsc/img/people/ali/sad.png"), (500, 500))
            return 3
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
        display.flip()

def scene3_0():
    global screen, text, options, ley, ali
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch1-sc3.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        createNarration(screen[0], screen[1][1], text[0])
        ley[1] = (-ley[0].get_width()//4, screen[1][1][1] - ley[0].get_height())
        ali[1] = (screen[1][1][0] - ali[0].get_width(), screen[1][1][1] - ali[0].get_height())
        screen[0].blit(ley[0], ley[1])
        screen[0].blit(ali[0], ali[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], ley, text[2][0], None, True, (10, 5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], ley, text[2][1], None, True, (0.5, 2.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], ali, text[1][0], 200, False, (0.5, 3.5))
        elif dialogue == 3: dialogue = createDialogue(screen[0], ali, text[1][1], 200, False, (0.5, 2.5))
        else:
            createDialogue(screen[0], ali, text[1][1], 200, False, None)
            createDialogue(screen[0], ley, text[2][2], None, True, None)
            buttons = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if dialogue > 3 and e.type == MOUSEBUTTONDOWN and e.button==1:
                closeDialogueEscene()
                ley[0], ali[0] = transform.scale(image.load("rsc/img/people/ley/scared.png"), (400, 400)), transform.scale(image.load("rsc/img/people/ali/angry.png"), (500, 500))
                for index in range(len(buttons)):
                    if buttons[index].collidepoint(mouse.get_pos()):
                        if index == 0:
                            text = [None, ["Ya no se gana lo mismo que hace tiempo.", "Hace quince años obteníamos más miel que la que obtenemos hoy en día.", "No es ni la mitad que antes...", "¡Ya no sabemos qué hacer!"], [". . ."]]
                            options = ["Tienes razón.", "Debe ser por..."]
                            return 3.1
                        elif index == 1:
                            return 3.2
                        elif index == 2:
                            text = [None, ["¡¿Que no lo ves?!", "¿No te has dado cuenta?", "¡Están acabando con nuestras abejas!"], ["Lo sé...", "Esto cada vez se pone peor. "]]
                            return 3.3
        display.flip()

def scene3_1():
    global screen, text, options, ley, ali
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch1-sc3.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        ley[1] = (-ley[0].get_width()//4, screen[1][1][1] - ley[0].get_height())
        ali[1] = (screen[1][1][0] - ali[0].get_width(), screen[1][1][1] - ali[0].get_height())
        screen[0].blit(ley[0], ley[1])
        screen[0].blit(ali[0], ali[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], ali, text[1][0], 200, False, (1.5, 1.5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], ali, text[1][1], 200, False, (0.5, 2.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], ali, text[1][2], None, False, (0.5, 2.5))
        elif dialogue == 3: dialogue = createDialogue(screen[0], ali, text[1][3], None, False, (0.5, 2.5))
        else:
            createDialogue(screen[0], ali, text[1][3], None, False, None)
            createDialogue(screen[0], ley, text[2][0], None, True, None)
            buttons = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if dialogue > 3 and e.type == MOUSEBUTTONDOWN and e.button==1:
                closeDialogueEscene()
                for index in range(len(buttons)):
                    if buttons[index].collidepoint(mouse.get_pos()):
                        if index == 0:
                            return 3.2
                        else:
                            text = [None, ["... esa soya fuera de lo común...", "Desde un principio supe que estaban sembrando cosas raras.", "¿Tú sabes algo más acerca de todo esto?"], [". . ."]]
                            options = ["Mmm...", "No, no sé nada.", "No puedo creerlo."]
                            return 3.4
        display.flip()

def scene3_2():
    global screen, text, options, ley, ali
    text = [None, ["Sí...", "Desde que comenzaron a deforestar el bosque las cosas cambiaron bastante.", "¡Estoy segura que todo esto es culpa de esos nuevos cultivos!"], ["No te preocupes, mamá.", "Sé que las cosas van a mejorar."]]
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch1-sc3.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        ley[1] = (-ley[0].get_width()//4, screen[1][1][1] - ley[0].get_height())
        ali[1] = (screen[1][1][0] - ali[0].get_width(), screen[1][1][1] - ali[0].get_height())
        screen[0].blit(ley[0], ley[1])
        screen[0].blit(ali[0], ali[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], ali, text[1][0], None, False, (1.5, 1.5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], ali, text[1][1], 200, False, (0.5, 2.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], ali, text[1][2], 200, False, (0.5, 2.5))
        elif dialogue == 3: dialogue = createDialogue(screen[0], ley, text[2][0], None, True, (0.5, 2.5))
        elif dialogue == 4: dialogue = createDialogue(screen[0], ley, text[2][1], None, True, (0.5, 4.5))
        else:
            closeDialogueEscene()
            text = [None, ["Bueno, cariño...", "Es hora de ir a dormir.", "Debes estar cansada."], ["Vayamos ambas, mamá.", "Hoy ha sido un día largo para las dos...", ". . ."]]
            return 4
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
        display.flip()

def scene3_3():
    global screen, text, options, ley, ali
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch1-sc3.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        ley[1] = (-ley[0].get_width()//4, screen[1][1][1] - ley[0].get_height())
        ali[1] = (screen[1][1][0] - ali[0].get_width(), screen[1][1][1] - ali[0].get_height())
        screen[0].blit(ley[0], ley[1])
        screen[0].blit(ali[0], ali[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], ali, text[1][0], None, False, (1.5, 1.5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], ali, text[1][1], None, False, (0.5, 2.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], ali, text[1][2], None, False, (0.5, 2.5))
        elif dialogue == 3: dialogue = createDialogue(screen[0], ley, text[2][0], None, True, (0.5, 2.5))
        elif dialogue == 4: dialogue = createDialogue(screen[0], ley, text[2][1], None, True, (0.5, 4.5))
        else:
            closeDialogueEscene()
            return 3.2
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
        display.flip()

def scene3_4():
    global screen, text, options, ley, ali
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch1-sc3.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        ley[1] = (-ley[0].get_width()//4, screen[1][1][1] - ley[0].get_height())
        ali[1] = (screen[1][1][0] - ali[0].get_width(), screen[1][1][1] - ali[0].get_height())
        screen[0].blit(ley[0], ley[1])
        screen[0].blit(ali[0], ali[1])
        if dialogue == 0: dialogue = createDialogue(screen[0], ali, text[1][0], None, False, (1.5, 1.5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], ali, text[1][1], 200, False, (0.5, 2.5))
        elif dialogue == 2: dialogue = createDialogue(screen[0], ali, text[1][2], 200, False, (0.5, 2.5))
        else:
            createDialogue(screen[0], ali, text[1][2], None, False, None)
            createDialogue(screen[0], ley, text[2][0], None, True, None)
            buttons = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if dialogue > 2 and e.type == MOUSEBUTTONDOWN and e.button==1:
                closeDialogueEscene()
                for index in range(len(buttons)):
                    if buttons[index].collidepoint(mouse.get_pos()):
                        if index < 2:
                            text = [None, ["Bueno, hija...", "Ve a descansar.", "Mañana tienes que ir a clases."], ["¡Oh, cierto!", "Pero antes de ir, te ayudaré a recoger todo esto.", ". . ."]]
                            return 4
                        else:
                            return 3.2
        display.flip()

def scene4():
    global screen, text, options, ley, ali
    dialogue, backgroundImage = 0, image.load("rsc/img/landscape/ch1-sc3.png")
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        backgroundImage = setBackgroundImage(screen[1][1], backgroundImage)
        screen[0].blit(backgroundImage, (0, 0))
        ley[1] = (-ley[0].get_width()//4, screen[1][1][1] - ley[0].get_height())
        ali[1] = (screen[1][1][0] - ali[0].get_width(), screen[1][1][1] - ali[0].get_height())
        screen[0].blit(ley[0], ley[1])
        screen[0].blit(ali[0], ali[1])
        if dialogue == 0:
            ley[0], ali[0] = transform.scale(image.load("rsc/img/people/ley/sad.png"), (400, 400)), transform.scale(image.load("rsc/img/people/ali/sad.png"), (500, 500))
            dialogue = createDialogue(screen[0], ali, text[1][0], None, False, (1.5, 1.5))
        elif dialogue == 1: dialogue = createDialogue(screen[0], ali, text[1][1], None, False, (0.5, 2.5))
        elif dialogue == 2:
            ali[0] = transform.scale(image.load("rsc/img/people/ali/happy.png"), (500, 500))
            dialogue = createDialogue(screen[0], ali, text[1][2], None, False, (0.5, 2.5))
        elif dialogue == 3:
            ley[0] = transform.scale(image.load("rsc/img/people/ley/happy.png"), (400, 400))
            dialogue = createDialogue(screen[0], ley, text[2][0], None, True, (0.5, 2.5))
        elif dialogue == 4: dialogue = createDialogue(screen[0], ley, text[2][1], 200, True, (0.5, 2.5))
        else:
            ley[0] = transform.scale(image.load("rsc/img/people/ley/sad.png"), (400, 400))
            createDialogue(screen[0], ley, text[2][2], None, True, None)
            button = createButtons(screen[0], screen[1][1], options, None)
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if dialogue > 4 and e.type == MOUSEBUTTONDOWN and e.button==1:
                closeDialogueEscene()
                if button.collidepoint(mouse.get_pos()):
                    return [2, backgroundSound]
        display.flip()

def start(mainSurface, backgroundSound):
    global screen, text, options
    screen = mainSurface
    scene = scene1_0(backgroundSound)
    if scene == 1.1:
        scene = scene1_1()
    if scene == 2:
        text = [None, ["¡Hola, Ley!", "¿Cómo te fue hoy?" ,"¿Qué tal la escuela?", "Toma asiento.", "Te contaré mientras cenamos..."], ["¡Hola, ma'!", "Me fue bien, ¿y a ti?", "¿Cómo van las cosas en el trabajo?"]]
        scene2()
        scene = scene3_0()
        if scene == 3.1:
            scene = scene3_1()
            if scene == 3.4:
                scene = scene3_4()
        elif scene == 3.3:
            scene = scene3_3()
        if scene == 3.2:
            scene3_2()
        options = ["Continuar."]
        return scene4()