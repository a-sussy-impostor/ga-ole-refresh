import logging
from prerun import *
from threading import Thread as thread

import time

# Initialize player's and NPC's integers
enemyPow = [0,0]
allyPow = [0,0]

# Function to handle player's input
def player_input():
    global allyPow, running
    while max(enemyPow[0],enemyPow[1]) < 100 and max(allyPow[0],allyPow[1]) < 100:
        user_input = input()
        allyPow[0] += 5
        allyPow[1] += 5
        print(f"Your allies' power are now: {allyPow.join(', ')}")

# Function to simulate NPC's integer increase
def npc_action():
    global enemyPow
    while max(enemyPow[0],enemyPow[1]) < 100 and max(allyPow[0],allyPow[1]) < 100:
        enemyPow[0] += 10
        print(f"Enemies' power are now: {enemyPow.join(', ')}")
        time.sleep(1)  # Delay for 1 second

player_thread = threading.Thread(target=player_input)
npc_thread = threading.Thread(target=npc_action)

# def cheerUp():
  # global aldata
  # temp1 = input()
  # aldata[0] = aldata[0]
  # to be continued

def getPercent(num):
  return str(floor(num*1000)/10)+"%"
    
def battle(allies,enemies,extra=False,countdown = 8,bossLevel = None,support = None):
  try:
    if (len(allies) > 4 and not extra) or (len(allies) > 5):
      logging.warning("Too many allies")
  except TypeError:
    logging.error("Incorrect input for 'extra' argument in battle()")
    return
  hp = []
  currentSelf = [0,1]
  for j in allies:
    if allies[j].name != "Shedinja":
      hp[j] = (round(allies[j].bst[0]*2+31+252/4)*allies[j].level)/100+10+allies[j].level
    else:
      hp[j] = 1
  aldata = [[[0,0,0,0,0,0],50,hp[0]],[[0,0,0,0,0,0],50,hp[1]],[[0,0,0,0,0,0],50,hp[2]],[[0,0,0,0,0,0],50,hp[3]]] # [[[stat],spirit,hp]...
  try:
    if extra:
      aldata[2] += [[0,0,0,0,0,0],50,maxHP[4]]
  except TypeError:
    logging.error("Incorrect input for 'extra' argument in battle()")
  enMHP = [(round(enemies[0].bst[0]*2+31+252/4)*enemies[0].level)/100+10+enemies[0].level,(round(enemies[1].bst[0]*2+31+252/4)*enemies[1].level)/100+10+enemies[1].level]
  endata = [[[0,0,0,0,0,0],100,(round(enemies[0].bst[0]*2+31+252/4)*enemies[0].level)/100+10+enemies[0].level],[[0,0,0,0,0,0],50,(round(enemies[1].bst[0]*2+31+252/4)*enemies[1].level)/100+10+enemies[1].level]] # [[stat,spirit,hp]...]
  print(f"{cyan}A battle between {yellow}{allies[0].name}, {allies[1].name} and {enemies[0].name}, {enemies[1].name} {cyan}has started!")
  logging.info(f"Battle between {yellow}{allies[0].name}, {allies[1].name} and {enemies[0].name}, {enemies[1].name} has started.")
  for x in range(countdown):
    status = []
    for y in allies:
      if aldata[y][2] < 1:
        status[y] = "Fainted"
      elif y in currentSelf:
        status[y] = "Current"
    print(cPink,sBright,f"~ Turn {x} ~ ")
    print(cLime,sBright,countdown - x," turns left")
    print(cCyan,"====== Pokemon Info ======")
    print("| Allies |")
    print(f"1. ({status[0]}) {allies[0].name} - {getPercent(aldata[0][2]/hp[0])} HP ({aldata[0][2]}/{hp[0]}); Fighting Spirit: {aldata[0][1]}%")
    print(f"2. ({status[1]}) {allies[1].name} - {getPercent(aldata[1][2]/hp[1])} HP ({aldata[1][2]}/{hp[1]}); Fighting Spirit: {aldata[1][1]}%")
    print(f"3. ({status[2]}) {allies[2].name} - {getPercent(aldata[2][2]/hp[2])} HP ({aldata[2][2]}/{hp[2]}); Fighting Spirit: {aldata[2][1]}%")
    print(f"4. ({status[3]}) {allies[3].name} - {getPercent(aldata[3][2]/hp[3])} HP ({aldata[3][2]}/{hp[3]}); Fighting Spirit: {aldata[3][1]}%")
    if extra:
      print(f"5. ({status[4]}) {allies[4].name} - {getPercent(aldata[4][2]/hp[4])} HP ({aldata[4][2]}/{hp[4]}); Fighting Spirit: {aldata[4][1]}%")
    enemyPow = [50,50]
    catchchance = [False,False]
    allyPow = [randint(1,30),randint(1,30)]
    plThread = thread(target=player_input)
    enThread = thread(target=npc_action)
    plThread.start()
    enThread.start()
    plThread.join()
    enThread.join()
    while max(enemyPow[0],enemyPow[1]) < 100 and max(allyPow[0],allyPow[1]) < 100:
      pass
    plThread.terminate()
    enThread.terminate()
    # enemy attacks
    if max(enemyPow[0],enemyPow[1]) >= 100:
       _defender = choice(allies)
       if enemyPow[0] >= 100:
           _ret = enemies[0].Attack(_defender)
           if _ret[1] != [0,0,0,0,0,0]:
              for _k in _ret[1]:
                  endata[0][0][_k] += _ret[1][_k]
           if _ret[2] != [0,0,0,0,0,0]:
              for _l in _ret[2]:
                  aldata[allies.index(_defender)][0][_l] += _ret[2][_l]
       else:
           _ret = enemies[1].Attack(_defender)
           if _ret[1] != [0,0,0,0,0,0]:
              for _k in _ret[1]:
                  endata[1][0][_k] += _ret[1][_k]
           if _ret[2] != [0,0,0,0,0,0]:
              for _l in _ret[2]:
                  aldata[allies.index(_defender)][0][_l] += _ret[2][_l]
       speEffect = _defender.Defense(_dmg)
       if specEffect == 2:
           endata[0][2] *= 0.88
           endata[1][2] *= 0.88
           endata[0][2] = round(endata[0][2])
           endata[1][2] = round(endata[1][2])
       elif specEffect == 1:
           aldata[allies.index(_defender)][0][1] += 1
       aldata[allies.index(_defender)][2] -= _dmg
       del _defender, _dmg, _ret, _specEffect
    elif max(allyPow[0],allyPow[1]) >= 100:
       # ally attacks
       _defender = choice(enemies)
       if allyPow[0] >= 100:
           _ret = allies[currentSelf[0]].Attack(_defender)
           if _ret[1] != [0,0,0,0,0,0]:
              for _m in _ret[1]:
                  aldata[currentSelf[0]][0][_m] += _ret[1][_m]
           if _ret[2] != [0,0,0,0,0,0]:
              for _n in _ret[2]:
                  endata[enemies.index(_defender)][0][_n] += _ret[2][_n]
       else:
           _ret = allies[currentSelf[1]].Attack(_defender)
           if _ret[1] != [0,0,0,0,0,0]:
              for _m in _ret[1]:
                  aldata[currentSelf[1]][0][_m] += _ret[1][_m]
           if _ret[2] != [0,0,0,0,0,0]:
              for _n in _ret[2]:
                  endata[enemies.index(_defender)][0][_n] += _ret[2][_n]
       speEffect = _defender.Defense(_dmg)
       if specEffect == 2:
           aldata[currentSelf[0]][2] *= 0.88
           aldata[currentSelf[1]][2] *= 0.88
           aldata[currentSelf[0]][2] = round(endata[0][2])
           aldata[currentSelf[1]][2] = round(endata[1][2])
       elif specEffect == 1:
           endata[enemies.index(_defender)][0][1] += 1
       endata[enemies.index(_defender)][2] -= _dmg
       del _defender, _dmg, _ret, _specEffect
    else:
        logging.error("Accidentally jumped out of loop")
        return -1
    clear()
    if aldata[currentSelf[0]][2] <= 0:
       print("Oh no! Your 1st Pokemon has fainted! Replace with new pokemon:")
       _replica = int(input())
       currentSelf[0] = _replica
       print(f"You sent out {allies[currentSelf[0]].name}!")
    if aldata[currentSelf[1]][2] <= 0:
       print("Oh no! Your 2nd Pokemon has fainted! Replace with new pokemon:")
       _replica = int(input())
       currentSelf[1] = _replica
       print(f"You sent out {allies[currentSelf[1]].name}!")
    if endata[0][2] <= 0:
       print(f"Your enemy, {enemies[0].name} has fainted! Catch chance!")
       catchchance[0] = True
    if endata[0][2] <= 0:
       print(f"Your enemy, {enemies[1].name} has fainted! Catch chance!")
       catchchance[1] = True
    if catchchance == [True,True]
       print("Both enemies have fainted! Catch time!")
       pass
       # work in progress
    elif allies[0][2] <= 0 and allies[1][2] <= 0 and allies[2][2] <= 0 and allies[3][2] <= 0:
       if extra and allies[4][2] > 0:
          pass
       else:
          print("All of your pokemon has fainted!")
          # not completed yet
