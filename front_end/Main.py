import pygame as p

def main():
    gs = GameState()
    running = True
    while running:
        if

main()

from Chess import ChessEngine
from Chess import OtherStates

#Project status: draw by repetition, 50 move rule yet to do
#num 1 priority: work on settings state

WINDOW_WIDTH = 960 #1280
WINDOW_HEIGHT = 600 #800
WIDTH = HEIGHT = 600
DIMENSION = 8
SQ_SIZE = HEIGHT / DIMENSION
FPS = 30
IMAGES = []
PIECES = ["bR", "bN", "bB", "bQ", "bK", "bp", "wp", "wR", "wN", "wB", "wQ", "wK"]
turnLabel = "White's"

def loadImages(pieceStyle):
    #load standard pieces part 1
    stanPieces = OtherStates.SpriteSheet(p.image.load("images/standardpieces.png"), 2, 6)
    standardwK = stanPieces.getSubImageByIndex(0, 0)
    standardwQ = stanPieces.getSubImageByIndex(0, 1)
    standardwB = stanPieces.getSubImageByIndex(0, 2)
    standardwN = stanPieces.getSubImageByIndex(0, 3)
    standardwR = stanPieces.getSubImageByIndex(0, 4)
    standardwp = stanPieces.getSubImageByIndex(0, 5)
    standardbK = stanPieces.getSubImageByIndex(1, 0)
    standardbQ = stanPieces.getSubImageByIndex(1, 1)
    standardbB = stanPieces.getSubImageByIndex(1, 2)
    standardbN = stanPieces.getSubImageByIndex(1, 3)
    standardbR = stanPieces.getSubImageByIndex(1, 4)
    standardbp = stanPieces.getSubImageByIndex(1, 5)
    for piece in PIECES:
        #load standard pieces part 2
        if piece[0] == "b":
            if piece[1] == "K":
                IMAGES.append(p.transform.scale(standardbK, (SQ_SIZE, SQ_SIZE)))
            elif piece[1] == "Q":
                IMAGES.append(p.transform.scale(standardbQ, (SQ_SIZE, SQ_SIZE)))
            elif piece[1] == "R":
                IMAGES.append(p.transform.scale(standardbR, (SQ_SIZE, SQ_SIZE)))
            elif piece[1] == "B":
                IMAGES.append(p.transform.scale(standardbB, (SQ_SIZE, SQ_SIZE)))
            elif piece[1] == "N":
                IMAGES.append(p.transform.scale(standardbN, (SQ_SIZE, SQ_SIZE)))
            elif piece[1] == "p":
                IMAGES.append(p.transform.scale(standardbp, (SQ_SIZE, SQ_SIZE)))
        elif piece[0] == "w":
            if piece[1] == "K":
                IMAGES.append(p.transform.scale(standardwK, (SQ_SIZE, SQ_SIZE)))
            elif piece[1] == "Q":
                IMAGES.append(p.transform.scale(standardwQ, (SQ_SIZE, SQ_SIZE)))
            elif piece[1] == "R":
                IMAGES.append(p.transform.scale(standardwR, (SQ_SIZE, SQ_SIZE)))
            elif piece[1] == "B":
                IMAGES.append(p.transform.scale(standardwB, (SQ_SIZE, SQ_SIZE)))
            elif piece[1] == "N":
                IMAGES.append(p.transform.scale(standardwN, (SQ_SIZE, SQ_SIZE)))
            elif piece[1] == "p":
                IMAGES.append(p.transform.scale(standardwp, (SQ_SIZE, SQ_SIZE)))
        IMAGES.append(p.transform.scale(p.image.load("images/leipzigPieces/leipzig" + piece +".png"), (SQ_SIZE, SQ_SIZE))) #load leipzig pieces

    IMAGES.append(p.transform.scale(p.image.load("images/cover.png"), (1563 / (2560 / WINDOW_WIDTH), 1042 / (1600 / WINDOW_HEIGHT))))
    IMAGES.append(p.transform.scale(p.image.load("images/reddot.png"), (SQ_SIZE, SQ_SIZE)))
    IMAGES.append(p.transform.scale(p.image.load("images/dot.png"), (SQ_SIZE, SQ_SIZE)))
    IMAGES.append(p.transform.scale(p.image.load("images/target.png"), (SQ_SIZE, SQ_SIZE)))

def main():
    p.init()
    screen = p.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(p.Color("white"))
    p.display.set_caption("Chess Engine")
    clock = p.time.Clock()
    ms = OtherStates.MenuState(WINDOW_WIDTH, WINDOW_HEIGHT)
    ss = OtherStates.SettingsState(WINDOW_WIDTH, WINDOW_HEIGHT)
    gs = ChessEngine.GameState()
    loadImages(ss.pieceStyle)
    running = True
    menu_complete = run_menu(screen, clock, ms, ss, running) #runs menu and waits for something to be returned
    if menu_complete:
        #game screen
        sqSelected = ()
        playerClicks = []
        moveMade = False
        p.display.flip()
        legalMoves = gs.getLegalMoves()
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif (e.type == p.MOUSEBUTTONDOWN) & (p.mouse.get_pos()[0] < WIDTH) & (p.mouse.get_pos()[1] < HEIGHT):
                    location = p.mouse.get_pos()
                    column = location[0] / SQ_SIZE
                    row = location[1] / SQ_SIZE
                    if sqSelected == (row, column):
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row, column)
                        playerClicks.append(sqSelected)
                        if len(playerClicks) == 2:
                            move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                            for legalMove in legalMoves:
                                if move == legalMove:
                                    if (legalMove.pawnPromotion) & (not ss.autoQueen):
                                        print("q for queen")
                                        print("n or k for knight")
                                        print("r for rook")
                                        print("b for bishop")
                                        choice = input("Choose a piece to promote to: ")
                                        if (choice == "q") | (choice == "Q"):
                                            legalMove.promotionChoice = "Q"
                                        if (choice == "n") | (choice == "N") | (choice == "k") | (choice == "K"):
                                            legalMove.promotionChoice = "N"
                                        if (choice == "r") | (choice == "R"):
                                            legalMove.promotionChoice = "R"
                                        if (choice == "b") | (choice == "B"):
                                            legalMove.promotionChoice = "B"
                                    gs.makeMove(legalMove)
                                    moveMade = True
                                    sqSelected = ()
                                    playerClicks = []
                            if not moveMade:
                                playerClicks = [sqSelected]
                elif e.type == p.KEYDOWN:
                    if e.key == p.K_BACKSPACE:
                        gs.undoMove()
                        moveMade = True
            if moveMade:
                legalMoves = gs.getLegalMoves()
                moveMade = False
            drawGameState(screen, gs, ss, sqSelected, legalMoves)
            clock.tick(FPS)
            p.display.flip()