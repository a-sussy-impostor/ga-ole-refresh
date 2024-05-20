# from os import system as sys
# sys("pip install colorama")
from colorama import Fore as fore
from colorama import Style as style
from colorama import init as cInit

cInit(autoreset=True)

cRed = fore.RED
cGreen = fore.GREEN
cOrange = fore.YELLOW
cBlue = fore.BLUE
cPurple = fore.MAGENTA
cBlack = fore.BLACK
cBlue2 = fore.CYAN
cWhite = fore.WHITE
cReset = fore.RESET

cGray = fore.LIGHTBLACK_EX
cLime = fore.LIGHTGREEN_EX
cCyan = fore.LIGHTBLUE_EX
cYellow = fore.LIGHTYELLOW_EX
cPink = fore.LIGHTMAGENTA_EX

sDim = style.DIM
sBright = style.BRIGHT
sReset = style.NORMAL

rReset = style.RESET_ALL
