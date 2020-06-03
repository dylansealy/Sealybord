#Imports all n ecessary libraries and files
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from PIL import Image, ImageTk

#Initial user setup
def userInput():
    global stageProgram, playersTotal, playersName#Defines the variables as global variables
    setUp = Tk(); setUp.title("Sealybord"); setUp.iconphoto(True, tk.PhotoImage(file="images/original/littleSealy.png")); setUp.geometry("500x400")#Defines and sets the setUp window and sets the properties window title, window icon and window size
    titleFrame = LabelFrame(setUp, bg="white"); titleFrame.pack()#Defines and sets a frame in the setUp window and sets its background color propertie
    image = ImageTk.PhotoImage(Image.open("images/resized/sealy.jpg")); titleFrameImage = Label(titleFrame, image=image).grid(row=0, column=0, padx=(25, 0), sticky=W)#Sets an image on the left side in the titleFrame
    titleFont = tkFont.Font(size=25); title = Label(titleFrame, text="Welkom bij Sealybord", bg="white", font=titleFont).grid(row=0, column=0, padx=(120,65), sticky=E)#Sets text on the right side in the titleFrame
    playersTotal = IntVar(); playersTotal.set("1")#Defines a Tkinter variable and sets its default value
    totalPlayers = Label(setUp, text="Hoeveel spelers willen er spelen?").pack()
    totalPlayers = OptionMenu(setUp, playersTotal, "1", "2", "3", "4", "5", "6", "7", "8", "9").pack()#Sets a dropdown menu in the setUp window
    playersName = StringVar()
    namePlayers = Label(setUp, text="Vul de namen van de spelers in gescheiden doormiddel van \", \".").pack()
    namePlayers = Entry(setUp, textvariable=playersName, width=50); namePlayers.pack()#Sets an input field in the setUp window
    setUp.mainloop()
    stageProgram = 1

#Global variables program
def variables():
    global totalPlayers, boardFields, namePlayers, positionPlayers, turnPlayer, xPlayers, yPlayers,  valueDice
    #X,Y positions board
    boardFields = [[145,715],[294,715],[373,715],[445,715],[526,715],[603,715],[691,715],[782,715],[855,710],[950,680],[1019,625],[1065, 565],[1100,505],[1120,435],[1120,355],[1105,275],[1080,210],[1035,150],[955,85],[845,45],[755,40],[675,40],[600,40],[520,40],[442,40],[360,40],[290,40],[210,70],[148,115],[100,165],[70,225],[55,295],[55,375],[75,445],[115,500],[165,555],[225,595],[300,615],[375,615],[450,615],[527,615],[607,615],[695,615],[780,615],[860,600],[940,550],[995,480],[1010,410],[1015,335],[990,270],[925,195],[845,150],[730,145],[620,145],[527,145],[440,145],[365,145],[290,160],[205,225],[175,340],[190,410],[235,470],[305,500],[370,310]]
    totalPlayers = playersTotal.get()
    namePlayers = playersName.get(); namePlayers = namePlayers.split(", ")#Stores the user input players name into an array
    positionPlayers = [0] * totalPlayers#Keeps track of the positions of the players
    turnPlayer = 0#Variable for keeping track which players turn it its
    xPlayers = [0] * totalPlayers; yPlayers = [0] * totalPlayers#Keeps track of the x,y coordinates of all players
    valueDice = 0
    #wie het hoogste gooit mag beginnen