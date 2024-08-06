import pygame as py
from tkinter import messagebox as ms
import random as rd
import json
from colormap import rgb2hex
py.init()
py.mixer.init()
screenWidth = 500
screenHeight = 500
screen = py.display.set_mode((500 , 500))
py.display.set_icon(py.image.load("Icon.png"))
py.display.set_caption("Random Colour Generator")
data = {"rc" : (rd.randint(0 , 255) , rd.randint(0 , 255) , rd.randint(0 , 255)) , "welcomeMessageBool" : False}
data["colourValue"] = "RGB: " + str(data["rc"]) + "\n" + "Hexadecimal: " + rgb2hex(data["rc"][0] , data["rc"][1] , data["rc"][2])
try:
    with open("data.txt") as rcgData:
        data = json.load(rcgData)
except:
    pass
programRunning = True
def newRc():
    global data
    data["rc"] = (rd.randint(0 , 255) , rd.randint(0 , 255) , rd.randint(0 , 255))
if data["welcomeMessageBool"] == False:
    data["welcomeMessageBool"] = True
    py.mixer.music.load("Message.wav")
    py.mixer.music.set_volume(0.4)
    py.mixer.music.play()
    ms.showinfo("Welcome" , "This is a short programming project, that in short is a random colour generator. It can also tell you the colour value.")
    py.mixer.music.load("Message.wav")
    py.mixer.music.set_volume(0.4)
    py.mixer.music.play()
    ms.showinfo("Tutorial" , "You can press Space to change the colour, and Shift to see the colour value.")
while programRunning:
    mouseX , mouseY = py.mouse.get_pos()
    for event in py.event.get():
        if event.type == py.QUIT:
            programRunning = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                data["colourValue"] = "RGB: " + str(data["rc"]) + "\n" + "Hexadecimal: " + rgb2hex(data["rc"][0] , data["rc"][1] , data["rc"][2])
                py.mixer.music.load("NewRc.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
                newRc()
            if event.key == py.K_LSHIFT or event.key == py.K_RSHIFT:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
                ms.showinfo("Colour Value" , data["colourValue"])
            if event.key == py.K_LALT or event.key == py.K_RALT:
                data["rc"] = (255 - (data["rc"][0]) , 255 - (data["rc"][1]) , 255 - (data["rc"][2]))
                data["colourValue"] = "RGB: " + str(data["rc"]) + "\n" + "Hexadecimal: " + rgb2hex(data["rc"][0] , data["rc"][1] , data["rc"][2])
    screen.fill(data["rc"])
    py.display.flip()
py.quit()
with open("data.txt" , "w") as rcgData:
    json.dump(data , rcgData)
