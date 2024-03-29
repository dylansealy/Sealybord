#* Imports all necessary libraries
import glob, keyboard, os, random, time, webbrowser
import pygame
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
#! Must be last import
from PIL import Image, ImageTk
#* Initialize images and game variables
# Creates neccesary resized folders
try:
    os.makedirs("./images/resized/pawns/", 666)
    os.makedirs("./images/resized/gameBoardAssets/", 666)
except:
    print("Folder(s) bestaa(t)(n) al.")
# Creates resized images
for file in glob.glob("./images/original/**/*", recursive=True):
    if not os.path.isdir(file):
        name = os.path.basename(file)
        image = Image.open(file)
        if file[18:23] == "pawns":
            # Resizes image with maximum height or width, but keeping aspect ratio
            image.thumbnail((50, 50))
            image.save("./images/resized/pawns/" + name)
        elif file[18:33] == "gameBoardAssets":
            image.thumbnail((70, 70))
            image.save("./images/resized/gameBoardAssets/" + name)
        elif file[18:27] == "sealy.jpg":
            image.thumbnail((60, 60))
            image.save("./images/resized/" + name)
# Creates pawn list
pawns: list[pygame.image] = []
for pawn in glob.glob("./images/resized/pawns/*"):
    pawns.append(pygame.image.load(pawn))
gameBoard = pygame.image.load("images/original/spelbord.png")
windowIcon = pygame.image.load("images/original/littleSealy.png")
cookieImage = pygame.image.load("images/resized/gameBoardAssets/cookie.png")
wifiImage = pygame.image.load("images/resized/gameBoardAssets/wifi.png")
gitHubImage = pygame.image.load("images/resized/gameBoardAssets/github.png")
darkWebImage = pygame.image.load("images/resized/gameBoardAssets/darkweb.png")
internetImage = pygame.image.load("images/resized/gameBoardAssets/internet.png")
appleImage = pygame.image.load("images/resized/gameBoardAssets/apple.png")
internetExplorerImage = pygame.image.load("images/resized/gameBoardAssets/internetexplorer.png")
#* Defines function for user set up
def userSetUp(storePlayersName, storePlayersTotal, storeRulesCheck):
    # Defines variables as global variables instead of scoped variables
    global stageProgram, playersTotal, playersName, rulesCheck
    # Variable for tracking stage program
    stageProgram = 0
    # Defines root window. Withdrawing root window so tkinter doesn't create one.
    root = Tk()
    root.withdraw()
    # Defines setUp window and sets its properties
    # Toplevel window prohibits pygame image error
    setUp = tk.Toplevel()
    # Sets window focus on setUp
    setUp.focus_set()

    setUp.title("Sealybord")
    # Defines window dimensions and its position
    setUp.geometry("500x250+600+300")

    setUp.resizable(0, 0)
    setUp.iconphoto(True, tk.PhotoImage(file="images/original/littleSealy.png"))
    # Defines frame in setUp window and sets its background color propertie
    titleFrame = LabelFrame(setUp, bg="white")
    titleFrame.grid(row=0, column=0)
    # Defines image left side titleFrame
    image = ImageTk.PhotoImage(Image.open("images/resized/sealy.jpg"))
    titleFrameImage = Label(titleFrame, image=image)
    titleFrameImage.grid(row=0, column=0, padx=(25, 0), sticky=W)
    # Defines font tkinter
    titleFont = tkFont.Font(size=25)

    title = Label(titleFrame, text="Welkom bij Sealybord", bg="white", font=titleFont)
    title.grid(row=0, column=0, padx=(120,65), sticky=E)
    # Defines tkinter variable and sets its default value
    playersTotal = IntVar()
    playersTotal.set(storePlayersTotal)

    bodyFont = tkFont.Font(size=11)
    totalPlayers = Label(setUp, text="Hoeveel spelers willen er spelen?", font=bodyFont)
    totalPlayers.grid(row=1, column=0, padx=(40, 0), pady=(5, 0), sticky=W)
    # Defines drop down menu in setUp window
    totalPlayers = OptionMenu(setUp, playersTotal, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
    totalPlayers.grid(row=1, column=0, padx=(295, 0), pady=(5, 0), sticky=W)

    playersName = StringVar()
    playersName.set(storePlayersName)
    namePlayers = Label(setUp, text="Vul de namen van de spelers in gescheiden doormiddel van \", \".\n"
                                    " Let op namen mogen maximaal 15 tekens lang zijn!", font=bodyFont)
    namePlayers.grid(row=2, column=0, padx=(40, 0), pady=(5, 0), sticky=W)
    # Defines input field setUp window
    namePlayers = Entry(setUp, textvariable=playersName, width=50, bg="grey", fg="white")
    namePlayers.grid(row=3, column=0, pady=(3, 0))

    # Defines function for button that requires user to click on button for continuation program
    def button():
        global stageProgram
        # Stops setUp window
        setUp.destroy()

        # Next stage program
        stageProgram = 1
        variables()

    rulesCheck = IntVar()
    rulesCheck.set(storeRulesCheck)
    rulesCheckBox = Checkbutton(setUp, text="Ik wil de spelregels bekijken.", variable=rulesCheck)
    rulesCheckBox.grid(row=4, column=0, padx=(40, 0), pady=(5, 0), sticky=W)
    # Defines button in setUp window
    nextButton = Button(setUp, text="Volgende", command=button)
    nextButton.grid(row=5, column=0, padx=(0, 60), pady=(10, 0), sticky=E)
    # Starts loop setUp window
    setUp.mainloop()
#* Defines function that sets global variables program
def variables():
    global boardFields, gooseFields, totalPlayers, namePlayers, positionPlayers, movePlayerPossible, turnPlayer,\
            previousTurnPlayer, turns, skipTurn, waitTurn, waitTurnPossible, xPlayers, yPlayers,\
            dice, valueDice, eventText, stageProgram
    # Defines x, y board fields
    boardFields = [[145, 715], [294, 715], [373, 715], [445, 715], [526, 715], [593, 705], [682, 705], [782, 715], [855, 710],
                   [930, 665], [1019, 625], [1065, 565], [1100, 505], [1120, 435], [1100, 342], [1105, 275], [1080, 210], [1035, 150],
                   [940, 75], [830, 35], [755, 40], [675, 40], [600, 40], [505, 30], [442, 40], [360, 40], [290, 40], [200, 65],
                   [148, 115], [100, 165], [70, 225], [43, 279], [43, 356], [75, 445], [115, 500], [165, 555], [210, 575],
                   [300, 615], [375, 615], [450, 615], [527, 615], [593, 595], [681, 595], [780, 615], [860, 600], [920, 530],
                   [995, 480], [1010, 410], [1015, 335], [990, 270], [900, 190], [845, 150], [715, 142], [620, 145], [508, 143],
                   [440, 145], [365, 145], [290, 160], [200, 225], [172, 316], [190, 410], [235, 470], [305, 500], [370, 310]]
    # Goose fields
    gooseFields = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
    # Gets playersTotal and playersName from userSetUp and converts namePlayers into list
    storePlayersTotal = playersTotal.get()
    totalPlayers = playersTotal.get()
    storePlayersName = playersName.get()
    namePlayers = storePlayersName.split(", ")
    # Variables keeping track position players and if move is possible
    positionPlayers = [0] * totalPlayers
    movePlayerPossible = True
    # Variables keeping track which players turn it is and the previous player. Also chooses who starts
    turnPlayer = random.randint(0, totalPlayers - 1)
    previousTurnPlayer = turnPlayer - 1
    # Variables keeping track how many turns passed
    turns = 0
    # Variables keeping track if player must skip round or wait until someone else
    skipTurn = [0] * totalPlayers
    waitTurn = [[False, 0]] * totalPlayers
    waitTurnPossible = False
    # Variables keeping track x, y coordinates players
    xPlayers = [0] * totalPlayers
    yPlayers = [0] * totalPlayers
    # Variables keeping track dices and its values
    dice = [0, 0]
    valueDice = 0
    # Defines message game
    eventText = ""

    storeRulesCheck = rulesCheck.get()
    stageProgram = 2
    errors(storePlayersName, storePlayersTotal, storeRulesCheck)
#*Defines function that checks for userSetUp errors
def errors(storePlayersName, storePlayersTotal, storeRulesCheck):
    global stageProgram, namePlayers
    if namePlayers[0] == "":
        # Defines message box error with properties title and text
        messagebox.showerror("Sealybord", "Het namen veld mag niet leeg zijn!")
        # Keeps name input
        userSetUp(storePlayersName, storePlayersTotal, storeRulesCheck)
    elif len(namePlayers) != totalPlayers:
        messagebox.showerror("Sealybord", "Het aantal namen komt niet overeen met het aantal spelers!")
        userSetUp(storePlayersName, storePlayersTotal, storeRulesCheck)
    for i in namePlayers:
        if len(i) > 15:
            messagebox.showerror("Sealybord", "Een naam mag niet langer dan 15 tekens zijn!")
            userSetUp(storePlayersName, storePlayersTotal, storeRulesCheck)
    if stageProgram == 2:
        stageProgram = 3
        # Opens rules page if checked
        rulesView = rulesCheck.get()
        if rulesView == 1: webbrowser.open(url="https://github.com/DylanSealy/Ganzenbord.git")

        program()
#*Defines main loop program
def program():
    global windowIcon, cookieImage, stageProgram, boardFields, gooseFields, gameBoard, xPlayer, yPlayer, dice, valueDice, positionPlayers,\
            turnPlayer, previousTurnPlayer, turns, waitTurn, waitTurnPossible,  eventText, skipTurn, \
            totalPlayers
    #* Program set up
    # Starts pygame
    pygame.init()
    # Defines position (margin top) program window
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,32"
    # Defines height and width program window
    if totalPlayers != 1: windowSize = [1450, 800]
    else: windowSize = [1200, 800]
    # Not RESIZABLE, because of changing x, y coordinats
    window = pygame.display.set_mode(windowSize)
    # Sets window properties
    pygame.display.set_icon(windowIcon)
    pygame.display.set_caption("Sealybord")
    frameRate = pygame.time.Clock()
    #* Main loop program
    while stageProgram < 4:
        #* Window graphics
        # Window background
        window.fill((77, 219, 160))
        # Gets dimension of gameBoard prints image into window
        gameBoardDimensions = gameBoard.get_rect()
        window.blit(gameBoard, gameBoardDimensions)
        # Draws cookies on gooseFields
        for i in gooseFields: window.blit(cookieImage, (boardFields[i]))
        # Draws wifi
        window.blit(wifiImage, boardFields[6])
        window.blit(gitHubImage, boardFields[19])
        window.blit(darkWebImage, boardFields[31])
        window.blit(internetImage, boardFields[42])
        window.blit(appleImage, boardFields[52])
        window.blit(internetExplorerImage, boardFields[58])
        # Gets x, y positionss of players and draws their pawn
        for i in range(0, len(positionPlayers)):
            xPlayers[i] = boardFields[positionPlayers[i]][0]
            yPlayers[i] = boardFields[positionPlayers[i]][1]
            window.blit(pawns[i], (xPlayers[i], yPlayers[i]))
        # Defines font
        fontStyle = pygame.font.SysFont(None, 35)

        if turns != 0:
            # Defines sentence and prints it into window
            diceText = "Laatste worp " + namePlayers[previousTurnPlayer] + ": " + str(dice[0]) + " & " + str(dice[1]) + " = " + str(valueDice)
            label = fontStyle.render(diceText, 1, (0, 0, 0))
            window.blit(label, (390, 473))

            label = fontStyle.render(eventText, 1, (0, 0, 0))
            window.blit(label, (390, 500))
        if totalPlayers != 1:
            turnText = "Aan de beurt: " + str(namePlayers[turnPlayer])
            label = fontStyle.render(turnText, 1, (0, 0, 0))
            window.blit(label, (390, 527))
            # Gets name and position of players and prints it onto window in a table structure
            positionText = "Vak op het bord"
            label = fontStyle.render(positionText, 1, (0, 0, 0))
            window.blit(label, (1215, 20))
            yText = 50
            fontStyle = pygame.font.SysFont(None, 30)
            for i in range(0, len(namePlayers)):
                positionText = str(namePlayers[i]) + ": " + str(positionPlayers[i])
                # Visualizes which players turn it is
                if i == turnPlayer: label = fontStyle.render(positionText, 1, (91, 123, 212))
                else: label = fontStyle.render(positionText, 1, (0, 0, 0))
                window.blit(label, (1230, yText))
                yText += 25
        #* Updates window graphics
        frameRate.tick(60)
        pygame.display.flip()
        #* Defines function that checks game related rules
        def gameRules():
            global gooseFields, dice, positionPlayers, turnPlayer, eventText, skipTurn, waitTurn,\
                    stageProgram
            # First turn dice exception
            if positionPlayers[turnPlayer] - 9 == 0:
                if dice[0] == 4 and dice[1] == 5 or dice[0] == 5 and dice[1] == 4:
                    positionPlayers[turnPlayer] = 53
                    eventText = "Je gooide " + str(dice[0]) + " & " + str(dice[1]) + " dus je mag naar vakje 53."
                if dice[0] == 6 and dice[1] == 3 or dice[0] == 3 and dice[1] == 6:
                    positionPlayers[turnPlayer] = 26
                    eventText = "Je gooide " + str(dice[0]) + " & " + str(dice[1]) + " dus je mag naar vakje 26."
            # Goose field
            if positionPlayers[turnPlayer] in gooseFields:
                # Loads and plays sound
                pygame.mixer.music.load("sounds/cookie.mp3")
                pygame.mixer.music.play(0)

                messagebox.showwarning("Sealybord", "Je kwam terecht op een cookie!")
                addPosition()
            # Bridge field
            if positionPlayers[turnPlayer] == 6:
                positionPlayers[turnPlayer] = 12
                pygame.mixer.music.load("sounds/wifi.mp3")
                pygame.mixer.music.play(0)
                eventText = "Je kwam op wifi!"
            # Hostel field
            elif positionPlayers[turnPlayer] == 19:
                skipTurn[turnPlayer] += 1
                eventText = "Je kwam op GitHub!"
            # Pit field
            elif positionPlayers[turnPlayer] == 31:
                waitTurn[turnPlayer] = [True, 31]
                eventText = "Je kwam op het dark web!"
            # Maze field
            elif positionPlayers[turnPlayer] == 42:
                positionPlayers[turnPlayer] = 39
                eventText = "Je kwam op het internet!"
            # Jail field
            elif positionPlayers[turnPlayer] == 52:
                waitTurn[turnPlayer] = [True, 52]
                pygame.mixer.music.load("sounds/apple.mp3")
                pygame.mixer.music.play(0)
                eventText = "Je kwam op Apple!"
            # Death field
            elif positionPlayers[turnPlayer] == 58:
                positionPlayers[turnPlayer] = 0
                pygame.mixer.music.load("sounds/internetexplorer.mp3")
                pygame.mixer.music.play(0)
                eventText = "Je kwam op Internet Explorer!"
            # Stops program when someones position is 63
            elif positionPlayers[turnPlayer] == 63: stageProgram = 4
        #* Event listeners
        for event in pygame.event.get():
            # Stops program when user clicks on exit
            if event.type == pygame.QUIT: stageProgram = 5
            # Stops program when users holds ALT and F4
            if keyboard.is_pressed("F4") and keyboard.is_pressed("ALT"): stageProgram = 5
            # Stops program when the users holds CTRL and W
            if keyboard.is_pressed("CTRL") and keyboard.is_pressed("W"): stageProgram = 5
            # Defines message box question
            if keyboard.is_pressed("ESC"):
                result = messagebox.askquestion("Sealybord", "Wil je opnieuw beginnen?")
                if result == "yes":
                    # First pygame quit too prevent old window errors
                    pygame.quit()

                    userSetUp("Naam", 1, 0)
                else:
                    result = messagebox.askquestion("Sealybord", "Wil je stoppen?")
                    if result == "yes": stageProgram = 5
                    else:
                        # Resets window focus on window
                        program()

            if stageProgram == 3:
                if keyboard.is_pressed("SPACE"):
                    # Throws a dice and calculates the total value
                    dice = [random.randint(1, 6), random.randint(1, 6)]
                    valueDice = dice[0] + dice[1]
                    #* Defines function for new position player
                    def addPosition():
                        global gooseFields, positionPlayers, movePlayerPossible, turnPlayer, dice, valueDice, eventText, waitTurn
                        movePlayerPossible = True
                        # Checks if board field is emtpy
                        for i in positionPlayers:
                            if int(positionPlayers[turnPlayer] + valueDice) in gooseFields:
                                if int(positionPlayers[turnPlayer] + valueDice * 2) == int(i):
                                    movePlayerPossible = False
                                    eventText = "Er staat al een speler op dat vakje!"
                            if int(positionPlayers[turnPlayer] + valueDice) == int(i):
                                movePlayerPossible = False
                                eventText = "Er staat al een speler op dat vakje!"

                        if movePlayerPossible:
                            # Enables players to move after someone passed
                            for i in waitTurn:
                                if int(positionPlayers[turnPlayer] + valueDice) > int(i[1]):
                                    i[0] = False
                                    i[1] = 0
                            # Sends players back after board field 63
                            if positionPlayers[turnPlayer] + valueDice > 63:
                                positionPlayers[turnPlayer] = 63 - (positionPlayers[turnPlayer] + valueDice - 63)
                                eventText = "Je kwam niet precies op vakje 63!"
                                # Sends player back if their position is a goose
                                if positionPlayers[turnPlayer] in gooseFields:
                                    positionPlayers[turnPlayer] -= valueDice
                                    pygame.mixer.music.load("sounds/cookie.mp3")
                                    pygame.mixer.music.play(0)
                                    messagebox.showwarning("Sealybord", "Je kwam terecht op een cookie, terwijl je terug moest!")
                            # Update players position normally
                            else: positionPlayers[turnPlayer] += valueDice
                            gameRules()

                    # Checks if player is allowed to move
                    if skipTurn[turnPlayer] == 0 and not waitTurn[turnPlayer][0]:
                        eventText = "Er is niets bijzonders!"
                        addPosition()
                    # Decreases skipTurn when player skipped a turn
                    elif skipTurn[turnPlayer] > 0:
                        eventText = "Je moest nog een beurt overslaan!"
                        skipTurn[turnPlayer] -= 1
                    # Checks if waitTurn is possible
                    elif waitTurn[turnPlayer][0]:
                        waitTurnPossible = False
                        for i in positionPlayers:
                            if i < positionPlayers[turnPlayer]: waitTurnPossible = True
                            if not waitTurnPossible:
                               waitTurn[turnPlayer] = [False, 0]
                               eventText = "Beurt overgeslagen, want geen spelers!"
                            else: eventText = "Je moet wachten op hulp!"
                    # Updates turn related variables
                    turnPlayer += 1
                    previousTurnPlayer += 1
                    turns += 1
                    # Resets turn related variables for continuation turn loop
                    if turnPlayer + 1 > totalPlayers:
                        turnPlayer = 0
                        previousTurnPlayer = -1
                    # Stops program from interpreting multiple key strokes after each other
                    time.sleep(0.1)

            # Defines winner program stage
            if stageProgram == 4:
                time.sleep(0.1)
                messagebox.showinfo("Sealybord", namePlayers[turnPlayer] + " heeft gewonnen!")
                time.sleep(0.3)
                result = messagebox.askquestion("Sealybord", "Wil je nog een keer spelen?")
                if result == "yes":
                    pygame.quit()
                    userSetUp("Naam", 1, 0)
                else: stageProgram = 5

        # Stops program
        if stageProgram == 5:
            pygame.quit()
            exit()
#* Starts program loop
userSetUp("Naam", 1, 0)
