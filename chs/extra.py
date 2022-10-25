import sys
from pygame import *
from chs.tools import OptionColor, fonts, createButtons, drawBees

init()
clock, execution, bees, screen = time.Clock(), 0, None, None
info = (fonts[1].render("¿Qué pasará con Aru y Ali?", True, OptionColor.HOVERED.value), fonts[2].render("Descúbrelo en la segunda temporada.", True, OptionColor.HOVERED.value))
options = ["Continuar."]
backgroundSound = mixer.Sound("rsc/sound/ES_Simple Pleasantries - Arthur Benson.mp3")
backgroundSound.set_volume(0.2)

def scene1():
    global bees, screen
    while True:
        clock.tick(60)
        screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
        screen[0].fill(OptionColor.BASE.value)
        bees = drawBees(screen[0], screen[1][0], 50, bees)
        screen[0].blit(info[0], (screen[1][1][0]//2 - info[0].get_width()//2, screen[1][1][1]//2 - 50))
        screen[0].blit(info[1], (screen[1][1][0]//2 - info[1].get_width()//2, screen[1][1][1]//2))
        button = createButtons(screen[0], screen[1][1], options, [OptionColor.MAYBE])
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                if button.collidepoint(mouse.get_pos()):
                    print("¡Muchas gracias!")
                    return -1
        display.flip()

def start(mainSurface):
    global screen
    screen = mainSurface
    mixer.Sound.play(backgroundSound, -1)
    return scene1()