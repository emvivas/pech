import os, sys, ctypes, time as executionTime
from pygame import *
from chs import tools, ch0, ch1, ch2, extra

init()
chapter, device, clock, bees, bee = -1, ctypes.windll.user32, time.Clock(), None, None
device.SetProcessDPIAware()
screen = [None, [(device.GetSystemMetrics(0), device.GetSystemMetrics(1)), None]]
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen[0] = display.set_mode((int(screen[1][0][0]/1.45), int(screen[1][0][1]/1.15)), RESIZABLE, FULLSCREEN)
display.set_icon(image.load("rsc/img/bee/pech/happy.png"))
display.set_caption("Pech. La historia de una Xunán Kab.")
info = (font.Font("rsc/font/VerdanaPro-Black.ttf", 90).render("P E C H", True, tools.OptionColor.HOVERED.value), font.Font("rsc/font/IndieFlower-Regular.ttf", 24).render("La historia de una Xunán Kab.", True, tools.OptionColor.HOVERED.value), font.Font("rsc/font/SegoeUI.ttf", 14).render("© 2021: Paulina Galindo; Emiliano Vivas.", True, tools.OptionColor.HOVERED.value))
mixer.init()
backgroundImage, start, backgroundSound, startSound = image.load("rsc/img/landscape/cover.jpg"), image.load("rsc/img/control/start.png"), (mixer.Sound("rsc/sound/ES_The Postman - Kikoru.mp3"), mixer.Sound("rsc/sound/forest-2.mp3")), (mixer.Sound("rsc/sound/431532__supersound23__popping.mp3"), mixer.Sound("rsc/sound/481647__joncon-library__bee-buzzing.wav"))
backgroundSound[0].set_volume(0.1)
backgroundSound[1].set_volume(0.3)
mixer.Sound.play(backgroundSound[0], -1)
mixer.Sound.play(backgroundSound[1], -1)
startSound[0].set_volume(1)
startSound[1].set_volume(0.085)
while True:
    clock.tick(60)
    screen[1][1] = (display.get_surface().get_width(), display.get_surface().get_height())
    screen[0].fill(tools.OptionColor.HOVERED.value)
    if chapter == -1:
        backgroundImage = tools.setBackgroundImage(screen[1][1], backgroundImage)
        start = transform.scale(image.load("rsc/img/control/start.png"), (175, 175))
        startArea = start.get_rect(center=(screen[1][1][0]//2, screen[1][1][1]//3 + 30))
        if mouse.get_pressed()[0] and startArea.collidepoint(mouse.get_pos()) or key.get_pressed()[K_RETURN]: start = transform.scale(start, (150, 150))
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            elif bee == None and (e.type == MOUSEBUTTONDOWN and startArea.collidepoint(e.pos) or e.type == KEYDOWN and e.key == K_RETURN):
                startSound[0].play()
                bee = tools.createBee(screen[1][0])
                limit = (-3 * bee[1].get_width(), screen[1][0][0] + 2 * bee[1].get_width())
                backgroundSound[0].set_volume(0.05)
                backgroundSound[1].set_volume(0.25)
                startSound[1].play()
        screen[0].blit(backgroundImage, (0, 0))
        bees = tools.drawBees(screen[0], screen[1][0], 50, bees)
        tools.setWriteArea(screen[0], (screen[1][1][0], screen[1][1][1]//4), [0, screen[1][0][1] - 340], tools.OptionColor.DEFAULT, 200)
        screen[0].blit(start, (screen[1][1][0]//2 - start.get_width()//2, screen[1][1][1]//4))
        screen[0].blit(info[0], (screen[1][1][0]//2 - info[0].get_width()//2, screen[1][0][1] - 330))
        screen[0].blit(info[1], (screen[1][1][0]//2 - info[1].get_width()//2 + 2, screen[1][0][1] - 220))
        screen[0].blit(info[2], (50, screen[1][1][1] - 2 * info[2].get_height()))
        if bee != None:
            bee[0][0] += bee[2]
            bee[0][1] -= 5
            screen[0].blit(bee[1], bee[0])
            if not(limit[0] < bee[0][0] < limit[1]):
                backgroundSound[0].stop()
                chapter, ch0.execution, bees, bee = 0, executionTime.time() + 5, None, None
    elif chapter == 0:
        auxiliar = ch0.start(screen, backgroundSound[1])
        chapter, backgroundSound, ch1.execution = auxiliar[0], auxiliar[1], executionTime.time() + 5
    elif chapter == 1:
        auxiliar = ch1.start(screen, backgroundSound)
        chapter, backgroundSound, ch2.execution = auxiliar[0], auxiliar[1], executionTime.time() + 5
    elif chapter == 2: chapter = ch2.start(screen, backgroundSound)
    else:
        extra.start(screen)
        sys.exit()
    display.flip()