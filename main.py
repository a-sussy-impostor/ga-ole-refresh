from prerun import *
from battle import *

from os import getenv
import requests
from sys import exit as gameexit

version = '0.1.0'

newVers = requests.get("https://raw.githubusercontent.com/a-sussy-impostor/ga-ole-refresh-server/main/version.txt")
newVers = newVers.split(",")

if os.getenv("GITHUB_ACTIONS") == "true":
  print("Running on github actions")
  sys("pip3 install pickle")
  sys("pip install logging")

import logging
from base import *

logging.basicConfig(level=logging.INFO, filename="latest.log", filemode="w", format="%(asctime)s [%(levelname)s]: %(message)s")

testing = Disk("Pikachu","Electric",25,[35,55,40,50,50,90],["Thunderbolt","Electric",90,"S",None,None],2,1500)
testing2 = Disk("Charmander","Fire",25,[35,55,40,50,50,90],["Flamethrower","Fire",90,"S",None,None],2,1500)

print(cBlue,"==== Pokemon Ga-Olé Refresh ====")
print("")
print("Welcome! This is a remake and free version of the arcade game 'Pokemon Ga-Olé'.")
print(f"Made by {cRed}{sBright}@a-sussy-impostor{rReset} (Not Sus Impostor")
if newVers[0] == version:
  print("The game is up-to-date with the newest version.")
elif newVers[1] == version:
  print(cYellow,"You are using a beta version of the game.")
  logging.warning("Running on beta")
elif newVers[2] == version:
  print(cRed,"You are using the ALPHA version of the game. There may be bugs and your save file might be damaged.")
  logging.warning("Running on ALPHA")
else:
  print("Not updated to newest stable version. New version availiable: ",version)
  logging.info("Update availiable")

energy = 50 # unused
energyMax = 50 #unused

wait(2)
clear()
while True:
  print(cGreen,"~~~~ Main Menu ~~~~")
  print(cYellow,f"Energy: {energy}/{energyMax}")
  print(cBlue,f"Pokedollar: ₽{playerData[4]}")
  print("Actions performable: ")
  print("(1) Battle Catch")
  print("(2) Catch Immediately (Coming Soon in v0.3.0/1.0.0)")
  print("(3) Shop")
  print("(4) Achievements List (Coming Soon in v0.2.0)")
  print()
  print("* Utility Actions *")
  
