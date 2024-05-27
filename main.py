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

devmode = False
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
  _vinput = False
  while not _vinput:
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
    print(cGeeen,"(C) Console")
    print(cBlue,"(S) Save Manually")
    print(cRed,"(E) Exit Game")
    action = input("What action would you like to do: ")
    if action in H["1","2","3","4"] or action in ["C","S","E"]:
      _vinput = True
      match action:
        case '1':
          # wip
        case '2':
          print("Coming Soon!")
        case '3':
          items = shop(playerData[4])
          if items[0] != None:
            playerdata[1][items[0]] += quan
            playerdata[4] -= items[2]
          wait(2)
          clear()
          del items
        case '4':
          # coming soon
          print("Coming Very Soon!")
        case "C":
          cmd = input("Enter command: ")
          match cmd:
            case "devmode":
              print("Saving disabled (for now).")
              devmode = True
            case "infmasterball":
              if devmode:
                playerdata[1]["masterball"] = 999
              else:
                print("Developer mode required.")
            case _:
              print("Invalid command")
              wait(2)
              clear()
          del cmd
        case "S":
          save.save(playerData)
        case "E":
          resp = input(cYellow,"Are you sure to exit game? Progress will be saved. (Y) Yes")
          if resp == "Y":
            save.save(playerData)
            gameexit()
          else:
            wait(2)
            clear()
            del resp
    else:
      print("Invalid input")
      wait(2)
      clear()
