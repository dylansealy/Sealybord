# Imports all necessary libraries
import pygame
import random
import tkinter as tk
import tkinter.font as tkFont
import keyboard
import time
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


# Image variables and setup
pawns = [Image.open("images/original/c++.png"), Image.open("images/original/css.png"), Image.open("images/original/dart.png"),
         Image.open("images/original/html.png"), Image.open("images/original/java.png"), Image.open("images/original/js.png"),
         Image.open("images/original/php.png"), Image.open("images/original/python.png"), Image.open("images/original/sql.png")]
pawnsName = ["c++.png", "css.png", "dart.png", "html.png", "java.png", "js.png", "php.png", "python.png", "sql.png"]
# Resizes the pawn images with a maximum height or width, but keeping the aspect ratio and saves them
for i in range(0, len(pawns)):
    pawns[i].thumbnail((50, 50))
    pawns[i].save("images/resized/" + pawnsName[i])

pawns = [pygame.image.load("images/resized/c++.png"), pygame.image.load("images/resized/css.png"), pygame.image.load("images/resized/dart.png"),
         pygame.image.load("images/resized/sql.png"), pygame.image.load("images/resized/html.png"), pygame.image.load("images/resized/java.png"),
         pygame.image.load("images/resized/js.png"), pygame.image.load("images/resized/php.png"), pygame.image.load("images/resized/python.png")]
gameBoard = pygame.image.load("images/original/spelbord.png")
windowIcon = pygame.image.load("images/original/littleSealy.png")
titleFrameImage = Image.open("images/original/sealy.jpg")
titleFrameImage.thumbnail((60, 60))
titleFrameImage.save("images/resized/sealy.jpg")

# Initial user setup
# Defines and sets the setUp window and sets the properties window title, window icon, window size and window resize
def userSetUp():
    # Defines the variables as global variables instead of scoped variables
    global playersTotal, playersName, stageProgram

    # Stops not defined variable error in program
    stageProgram = 0

    # Sets two windows one root and one Toplevel. Defining a and withdrawing a root window so Tkinter doens't create one
    root = Tk()
    root.withdraw()
    setUp = tk.Toplevel()
    setUp.title("Sealybord")
    setUp.geometry("500x400+600+300")
    setUp.resizable(0, 0)
    setUp.iconphoto(True, tk.PhotoImage(file="images/original/littleSealy.png"))
    # Defines and sets a frame in the setUp window and sets its background color propertie
    titleFrame = LabelFrame(setUp, bg="white")
    titleFrame.grid(row=0, column=0)

    image = ImageTk.PhotoImage(Image.open("images/resized/sealy.jpg"))
    titleFrameImage = Label(titleFrame, image=image)
    # Sets an image on the left side in the titleFrame
    titleFrameImage.grid(row=0, column=0, padx=(25, 0), sticky=W)

    titleFont = tkFont.Font(size=25)
    title = Label(titleFrame, text="Welkom bij Sealybord", bg="white", font=titleFont)
    title.grid(row=0, column=0, padx=(120,65), sticky=E)
    # Defines a Tkinter variable and sets its default value
    playersTotal = IntVar()
    playersTotal.set("1")

    bodyFont = tkFont.Font(size=11)
    totalPlayers = Label(setUp, text="Hoeveel spelers willen er spelen?", font=bodyFont)
    totalPlayers.grid(row=1, column=0, padx=(40, 0), pady=(5, 0), sticky=W)
    #Sets a dropdown menu in the setUp window
    totalPlayers = OptionMenu(setUp, playersTotal, "1", "2", "3", "4", "5", "6", "7", "8", "9")
    totalPlayers.grid(row=1, column=0, padx=(295, 0), pady=(5, 0), sticky=W)

    playersName = StringVar()
    namePlayers = Label(setUp, text="Vul de namen van de spelers in gescheiden doormiddel van \", \".", font=bodyFont)
    namePlayers.grid(row=2, column=0, padx=(40, 0), pady=(5, 0), sticky=W)
    # Sets an input field in the setUp window
    namePlayers = Entry(setUp, textvariable=playersName, width=50, bg="grey", fg="white")
    namePlayers.grid(row=3, column=0, pady=(3, 0))

    # Creates a function for the button that requires the user to click on the button for the program to continue
    def button():
        global stageProgram
        setUp.destroy()
        # Sets in which stage the program is and starts the setUp window loop
        stageProgram = 1
        # Starts next stage program
        variables()


    nextButton = Button(setUp, text="Volgende", command=button)
    nextButton.grid(row=4, column=0, padx=(0, 60), pady=(190, 0), sticky=E)
    setUp.mainloop()


# Global variables program
def variables():
    global boardFields, totalPlayers, namePlayers, positionPlayers, turnPlayer, xPlayers, yPlayers, valueDice

    # X,Y positions board
    boardFields = [[145, 715], [294, 715], [373, 715], [445, 715], [526, 715], [603, 715], [691, 715], [782, 715], [855, 710],
                   [950, 680], [1019, 625], [1065, 565], [1100, 505], [1120, 435], [1120, 355], [1105, 275], [1080, 210], [1035, 150],
                   [955, 85], [845, 45], [755, 40], [675, 40], [600, 40], [520, 40], [442, 40], [360, 40], [290, 40], [210, 70],
                   [148, 115], [100, 165], [70, 225], [55, 295], [55, 375], [75, 445], [115, 500], [165, 555], [225, 595],
                   [300, 615], [375, 615], [450, 615], [527, 615], [607, 615], [695, 615], [780, 615], [860, 600], [940, 550],
                   [995, 480], [1010, 410], [1015, 335], [990, 270], [925, 195], [845, 150], [730, 145], [620, 145], [527, 145],
                   [440, 145], [365, 145], [290, 160], [205, 225], [175, 340], [190, 410], [235, 470], [305, 500], [370, 310]]

    totalPlayers = playersTotal.get()
    # Converts the user input into names and stores it in an array
    namePlayers = playersName.get()
    namePlayers = namePlayers.split(", ")

    # Keeps track of the positions of the players
    positionPlayers = [0] * totalPlayers
    # Variable for keeping track which players turn it its
    turnPlayer = 0

    # Variables for keeping track the x,y coordinates of all players
    xPlayers = [0] * totalPlayers
    yPlayers = [0] * totalPlayers

    valueDice = 0
    errors()
    # wie het hoogste gooit mag beginnen


# User setup errors
def errors():
    global stageProgram
    if namePlayers[0] == "":
        stageProgram = 0
        # Sets a window for the message box, but hides it immediately
        error = Tk()
        error.withdraw()
        # Sets a message box with the properties title and text
        messagebox.showerror("Sealybord", "Het namen veld mag niet leeg zijn!")
        userSetUp()
    elif len(namePlayers) != totalPlayers:
        stageProgram = 0
        error = Tk()
        error.withdraw()
        messagebox.showerror("Sealybord", "Het aantal namen komt niet overeen met het aantal spelers!")
        userSetUp()


# Starts user set up
userSetUp()


# Program setup
if stageProgram > 0:
    # Starts pygame and sets the height and width of the programs window and its position
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,32"
    windowSize = [1400, 800]
    # Not RESIZABLE, because of changing x,y coordinats
    window = pygame.display.set_mode(windowSize)
    # Sets the window properties icon, title and frame rate
    pygame.display.set_icon(windowIcon)
    pygame.display.set_caption("Sealybord")
    frameRate = pygame.time.Clock()


    # Main loop program
    while stageProgram < 3:
        # Graphics
        # background color
        window.fill((255, 255, 255))
        # Gets the dimension of the game board and matches the window size
        gameBoardDimensions = gameBoard.get_rect()
        window.blit(gameBoard, gameBoardDimensions)
        # Gets the x,y positions of the players and draws their pawn
        for i in range(0, len(positionPlayers)):
            xPlayers[i] = boardFields[positionPlayers[i]][0]
            yPlayers[i] = boardFields[positionPlayers[i]][1]
            window.blit(pawns[i], (xPlayers[i], yPlayers[i]))

        #Sets the font and prints a sentene in the game window
        fontStyle = pygame.font.SysFont(None, 30)
        diceText = "De laatste worp " + str(valueDice)
        label = fontStyle.render(diceText, 1, (0, 0, 0))
        window.blit(label, (390, 470))

        turnText = "Aan de beurt " + str(turnPlayer + 1)
        label = fontStyle.render(turnText, 1, (0, 0, 0))
        window.blit(label, (390, 495))


        # Updates graphics
        frameRate.tick(60)
        pygame.display.flip()


        # Eventisteners
        for event in pygame.event.get():
            # Stops the program when the user clicks on exit
            if event.type == pygame.QUIT: stageProgram = 3
            # Stops the program when the users holds ALT and F4
            elif keyboard.is_pressed("F4") and keyboard.is_pressed("ALT"): stageProgram = 3
            # Stops the program when the users holds CTRL and W
            elif keyboard.is_pressed("CTRL") and keyboard.is_pressed("W"): stageProgram = 3
            elif keyboard.is_pressed("ESC"):
                restart = Tk()
                restart.withdraw()
                result = messagebox.askquestion("Sealybord", "Wil je opnieuw beginnen?")
                if result == "yes": userSetUp()
                else: stageProgram = 3
            if stageProgram == 1:
                if keyboard.is_pressed("SPACE"):
                    # Throws a dice
                    valueDice = random.randint(1, 6)
                    # Sends players back if their next position is greater than 63
                    if positionPlayers[turnPlayer] + valueDice > 63: positionPlayers[turnPlayer] = 63 - (positionPlayers[turnPlayer] + valueDice - 63)
                    # Updates the current players position in a normal situation
                    else: positionPlayers[turnPlayer] += valueDice
                    # Stops program when someones position is 63
                    if positionPlayers[turnPlayer] == 63: stageProgram = 2
                    # Sets the next players turn
                    else: turnPlayer += 1
                    # Resets turnPlayers for the next round of turns
                    if turnPlayer + 1 > totalPlayers: turnPlayer = 0
                    # Stops program from interpreting multiple key stroke after each other
                    time.sleep(0.1)
                # elif event.key == pygame.K_BACKSPACE: Placeholder
            elif stageProgram == 2:
                time.sleep(0.5)
                winner = Tk()
                winner.withdraw()
                messagebox.showinfo("Sealybord", namePlayers[turnPlayer] + " heeft gewonnen!")
                time.sleep(0.5)
                result = messagebox.askquestion("Sealybord", "Wil je nog een keer spelen?")
                if result == "yes": userSetUp()
                else: stageProgram = 3


# Stop program
pygame.quit()