import random, time as executionTime
from enum import Enum
from pygame import *

init()
fonts = (font.Font("rsc/font/Mali-Light.ttf", 15), font.Font("rsc/font/AveriaLibre-Bold.ttf", 18), font.Font("rsc/font/Handlee-Regular.ttf", 30))
duration, dialogueNumber, dialogueStatus = [0, 0], 0, False

class OptionColor(Enum):
    AFFIRMATIVE = Color(90, 156, 92)
    BASE = Color(0, 0, 0)
    DEFAULT = Color(56, 86, 161)
    HOVERED = Color(255, 255, 255)
    MAYBE = Color(189, 117, 45)
    NEGATIVE = Color(186, 56, 67)

def setBackgroundImage(screen, backgroundImage):
    reason = backgroundImage.get_height()*screen[0]//backgroundImage.get_width()
    if screen[0] < screen[1] or reason < screen[1]: reason = ((backgroundImage.get_width()*screen[1])//backgroundImage.get_height(), screen[1])
    else: reason = (screen[0], reason)
    return transform.scale(backgroundImage, reason)

def setWriteArea(screen, size, position, color, alpha):
    rectangle = Surface(size)
    rectangle.set_alpha(alpha)
    rectangle.fill(color.value)
    screen.blit(rectangle, position)
    return rectangle

def createBee(screenSize):
    pech = image.load("rsc/img/bee/pech/happy.png")
    bee = [[-500 if random.randint(0,1)==0 else screenSize[0]+250, random.randint(250, screenSize[1]-500)], None, None]
    bee[1] = transform.scale(transform.flip(pech, True, False) if bee[0][0]!=-500 else pech, (500, 500))
    bee[2] = 25 if bee[0][0] == -bee[1].get_width() else -25
    return bee

def createBees(screenSize, dialogueNumber):
    bee = image.load("rsc/img/bee/worker.png")
    bees = [[], [], [[], []]]
    for index in range(dialogueNumber):
        reason = random.randint(10, 50)
        bees[0].append(transform.scale(transform.flip(bee, True, False) if index%2==0 else bee, (reason, reason)))
        bees[2][0].append(random.randint(-50, screenSize[0] + 50) if index%3!=0 else (screenSize[0] + 50 if random.randint(0, 1)==0 else -50))
        bees[2][1].append(random.randint(-100, -50) if index%2==0 else (screenSize[1]//2 if index%3==0 else random.randint(screenSize[1] + 50, screenSize[1] + 100)))
        bees[1].append(random.randint(1, 2) * (1 if bees[2][1][index] < screenSize[1]//2 else -1))
    return bees

def drawBees(screen, screenSize, dialogueNumber, bees):
    if bees == None: bees = createBees(screenSize, dialogueNumber)
    for index in range(len(bees[0])):
            if bees[2][0][index] % 257 == 0: bees[1][index] = random.randint(-1, 1)
            bees[2][0][index]+=2 if index % 2 == 0 else -2
            bees[2][1][index]+=bees[1][index]
            screen.blit(bees[0][index], (bees[2][0][index], bees[2][1][index]))
    for index in range(len(bees[0])):
        if -50 < bees[2][0][index] < screenSize[0] + 50: break
        elif index == len(bees[0]) - 1: bees = createBees(screenSize, dialogueNumber)
    return bees

def createText(text, width, indentation):
    textLine = text.split("\n")
    if font.Font.size(fonts[0], text)[0] > width:
        auxiliar = [[], textLine]
        textLine = []
        for index in range(len(auxiliar[1])):
            auxiliar[0] = [" " * 10 if indentation else "", auxiliar[1][index].split()]
            for string in auxiliar[0][1]:
                length = len(auxiliar[0][0])
                auxiliar[0][0] += string + ' '
                if font.Font.size(fonts[0], auxiliar[0][0])[0] > width - 30:
                    textLine.append(auxiliar[0][0][:length])
                    auxiliar[0][0] = string + ' '
            textLine.append(auxiliar[0][0])
            if index < len(auxiliar[1]) - 1: textLine.append("")
    return textLine

def createNarration(screen, surfaceSize, text):
    textLine = createText(text, surfaceSize[0], True)
    rectangle = setWriteArea(screen, [surfaceSize[0], len(textLine) * font.Font.size(fonts[0], ' ')[1] + 25], (0, 0), OptionColor.BASE, 200)
    for index in range(len(textLine)): screen.blit(fonts[0].render(textLine[index], True, OptionColor.HOVERED.value), (20, index * font.Font.size(fonts[0], ' ')[1]+10))
    return rectangle.get_size()

def createDialogue(screen, character, text, width, position, time):
    global duration, dialogueNumber, dialogueStatus
    if time == None: time = (0, 0)
    elif time[1] > 0:
        if not dialogueStatus:
            duration = [executionTime.time() + time[0], 0]
            duration[1] = duration[0] + time[1]
            dialogueStatus = True
        if duration[1] < executionTime.time():
            dialogueStatus = False
            dialogueNumber += 1
    if duration[0] < executionTime.time():
        if width == None: width = font.Font.size(fonts[0], max(text.split("\n"), key=len))[0]
        width += 35
        text = createText(text, width, False)
        height = len(text) * font.Font.size(fonts[0], ' ')[1]
        dialogue = ((0 if position else -width) + character[0].get_width()//2 + character[1][0], character[1][1] - character[0].get_height()//10 - height)
        setWriteArea(screen, (width, height + 20), dialogue, OptionColor.HOVERED, 200)
        for index in range(len(text)): screen.blit(fonts[0].render(text[index], True, OptionColor.BASE.value), (dialogue[0] + 15, dialogue[1] + (index * font.Font.size(fonts[0], ' ')[1]+10)))
    return dialogueNumber

def closeDialogueEscene():
    global duration, dialogueNumber, dialogueStatus
    duration = [0, 0]
    dialogueNumber = 0
    dialogueStatus = False
    
def createButtons(screen, surfaceSize, text, hoverColor):
    buttons = [[text, []], [0, surfaceSize[1] - 65 ,0]]
    buttons[1][0] = surfaceSize[0] // (len(buttons[0][0]) + 1)
    buttons[1][2] = (surfaceSize[0] - len(buttons[0][0])*buttons[1][0])//(len(buttons[0][0]) + 1)
    for index in range(len(buttons[0][0])):
        auxiliar = [fonts[1].render(buttons[0][0][index], True, OptionColor.HOVERED.value), [(index + 1)*buttons[1][2] + index*buttons[1][0], buttons[1][1]]]
        buttons[0][1].append(Rect(auxiliar[1][0], auxiliar[1][1], buttons[1][0], font.Font.size(fonts[1], ' ')[1]+10))
        if buttons[0][1][index].collidepoint(mouse.get_pos()):
            auxiliar[0] = fonts[1].render(buttons[0][0][index], True, OptionColor.BASE.value)
            draw.rect(screen, OptionColor.HOVERED.value, buttons[0][1][index], border_radius=10)
        else: draw.rect(screen, hoverColor[index].value if hoverColor != None else OptionColor.DEFAULT.value, buttons[0][1][index], border_radius=10)
        screen.blit(auxiliar[0], (auxiliar[1][0] + (buttons[1][0] - auxiliar[0].get_width())//2, auxiliar[1][1] + (buttons[0][1][index].height - auxiliar[0].get_height())//2))
    return buttons[0][1][0] if len(buttons[0][0]) == 1 else buttons[0][1]