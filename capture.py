from random import randint, choice, choices
from datetime import datetime
from prerun import *
from load import playerData, serverData
import save 

# playerdata format: [pokemon, bag, pokedex, achievements, other stats...
  
  
def bagball(bag):
  print("~ Owned Pokeballs ~")
  for _o in bag[0]:
    print(f"{(_o+1)}. {bag.values()[_o]}x {bag.keys()[_o]}")
  while True:
    _p = input("Poke Ball to use: ")
    if _p in bag.keys():
      bag[_p] -= 1
      break
    else:
      print("Invalid input")
  while True:
    _r = input("Poke Ball to use: ")
    if _r in bag.keys():
      bag[_r] -= 1
      break
    else:
      print("Invalid input")
  return [_p,_r]

def catchcalc(target,ballrate,ballname):
  if target.special == 'ub' and not ballname in ["Master Ball","Beast Ball"]:
    n_ballrate = 0.1
  else:
    n_ballrate = ballrate
  _b10 = ((3*100-2*0)*target.catchrate*n_ballrate)/(3*100)*3
  _catchsuc = None
  if _b10 >= 255:
    _catchsuc = True
    del _b10
    return [_catchsuc,None]
  else:
    _g10 = 65536/((255/B)**(3/16))
    _g11 = choices(range(65536),k=4)
    for _g12 in _g11: # 0: fail; 1-2: 1-2 wiggles; 3 & fail: 3 wiggles; 3 & success: success;
      if _g11[_g12] >= _g10:
        _catchsuc = False
        break
    if _catchsuc == None:
      _catchsuc = True
    del _g11, _g10, _b10
    return [_catchsuc,_g12]

def capture(allies,enemies,mode,turn,time = datetime.now(),offguard=False):
  ball = None
  if mode == 1:
    ball = "Master Ball"
  else:
    print("Catching Time!")
    print("Do you want to use the balls you own or use a random one for free?")
    while True:
      _ballpick = input("(B) Use owned balls (R) Random gift")
      if not _ballpick == "B" or _ballpick == "R":
        print("Invalid Choice")
      else:
        break
    if _ballpick == 'R':
      ball = choices(["Poke Ball","Great Ball","Ultra Ball","Master Ball"],[12,8,4,1],k=2)
    else:
      ball = bagball(saveData["bag"])
    del _ballpick
    ballrate = [0,0]
    _q = 0
    match ball[_q]:
      case 'Broken Ball':
        ballrate[_q] = 0.1
      case 'Rusted Ball':
        ballrate[_q] = 0.5
      case 'Poke Ball':
        ballrate[_q] = 1
      case 'Great Ball':
        ballrate[_q] = 1.5
      case 'Ultra Ball':
        ballrate[_q] = 2
      case 'Master Ball':
        ballrate[_q] = 255
      case 'Quick Ball' if turn == 1:
        ballrate[_q] = 7
      case 'Dusk Ball' if (time.hour > 17 or time.hour < 7):
        ballrate[_q] = 3
      case 'Fast Ball' if turn <= 3:
        ballrate[_q] = 4
      case 'Level Ball':
        match enemies[0].star:
          case 1:
            ballrate[_q] = 8
          case 2:
            ballrate[_q] = 4
          case 3:
            ballrate[_q] = 2
          case _:
            ballrate[_q] = 1
      case 'Premier Ball':
        ballrate[_q] = 1
      case 'Repeat Ball' if enemies[0].name in saveData["pokedex"]:
        ballrate[_q] = 3.5
      case 'Timer Ball':
        match turn:
          case 1|2|3:
            ballrate[_q] = 1
          case 4|5|6:
            ballrate[_q] = 1.5
          case 7|8:
            ballrate[_q] = 2
          case 9|10|11:
            ballrate[_q] = 3
          case _:
            ballrate[_q] = 4
      case 'Nest Ball':
        if enemies[_q].energy < 1500:
          ballrate[_q] = 5
        elif enemies[_q].energy < 2000:
          ballrate[_q] = 3
        elif enemies[_q].energy < 2500:
          ballrate[_q] = 2
        else:
          ballrate[_q] = 1
      case 'Luxury Ball':
        ballrate[_q] = 1
      case 'Dream Ball' if (time.hour >= 1 and time.hour < 5):
        ballrate[_q] = 5
      case 'Beast Ball':
        if enemies[_q].special == 'ub':
          ballrate[_q] = 5
        else:
          ballrate[_q] = 0.1
      case 'Strange Ball':
        ballrate[_q] = -1 # 50% chance; bypasses formula
      case 'Net Ball':
        if enemies[_q].name == 'Suicune':
          ballrate[_q] = 8
        elif 6 in enemies[_q].type:
          if 10 in enemies[_q].type:
            ballrate[_q] = 6
          else:
            ballrate[_q] = 3
        elif 10 in enemies[_q].type:
          ballrate[_q] = 3
      # case 'Sport Ball':
        # if (6 in enemies[_q].type) and ('Sport Ball' in serverData[0]):
          # ballrate[_q] = 4
      case _:
        ballrate[_q] = 1
    _q = 1
    match ball[_q]:
      case 'Broken Ball':
        ballrate[_q] = 0.1
      case 'Rusted Ball':
        ballrate[_q] = 0.5
      case 'Poke Ball':
        ballrate[_q] = 1
      case 'Great Ball':
        ballrate[_q] = 1.5
      case 'Ultra Ball':
        ballrate[_q] = 2
      case 'Master Ball':
        ballrate[_q] = 255
      case 'Quick Ball' if turn == 1:
        ballrate[_q] = 7
      case 'Dusk Ball' if (time.hour > 17 or time.hour < 7):
        ballrate[_q] = 3
      case 'Fast Ball' if turn <= 3:
        ballrate[_q] = 4
      case 'Level Ball':
        match enemies[0].star:
          case 1:
            ballrate[_q] = 8
          case 2:
            ballrate[_q] = 4
          case 3:
            ballrate[_q] = 2
          case _:
            ballrate[_q] = 1
      case 'Premier Ball':
        ballrate[_q] = 1
      case 'Repeat Ball' if enemies[0].name in saveData["pokedex"]:
        ballrate[_q] = 3
      case 'Timer Ball':
        match turn:
          case 1|2|3:
            ballrate[_q] = 1
          case 4|5|6:
            ballrate[_q] = 1.5
          case 7|8:
            ballrate[_q] = 2
          case 9|10|11:
            ballrate[_q] = 3
          case _:
            ballrate[_q] = 4
      case 'Nest Ball':
        if enemies[_q].energy < 1500:
          ballrate[_q] = 5
        elif enemies[_q].energy < 2000:
          ballrate[_q] = 3
        elif enemies[_q].energy < 2500:
          ballrate[_q] = 2
        else:
          ballrate[_q] = 1
      case 'Luxury Ball':
        ballrate[_q] = 1
      case 'Dream Ball' if (time.hour >= 1 and time.hour < 5):
        ballrate[_q] = 5
      case 'Beast Ball':
        if enemies[_q].special == 'ub':
          ballrate[_q] = 5
        else:
          ballrate[_q] = 0.1
      case 'Strange Ball':
        ballrate[_q] = -1 # 50% chance; bypasses formula
      case 'Net Ball':
        if enemies[_q].name == 'Suicune':
          ballrate[_q] = 8
        elif 6 in enemies[_q].type:
          if 10 in enemies[_q].type:
            ballrate[_q] = 6
          else:
            ballrate[_q] = 3
        elif 10 in enemies[_q].type:
          ballrate[_q] = 3
      # case 'Sport Ball':
        # if (6 in enemies[_q].type) and ('Sport Ball' in serverData[0]):
          # ballrate[_q] = 4
      case _:
        ballrate[_q] = 1
    _c10 = catchcalc(enemies[0])
    _c11 = catchcalc(enemies[1])
    if _c10[0]:
      print(f"Congratulations! You captured {enemies[0].name}!")
      enemyclone1 = enemies[0]
      enemyclone1.capturedBall = ball
      if randint(1,4096) == 4096:
        enemyclone1.shiny = shiny
      if randint(1,100) == 100:
        enemyclone1.lucky = True
      playerData[0].append(enemyclone2)
      save.save(playerData)
      if not enemyclone2.name in playerdata[2]:
        pass
        # register pokedex; wip
    else:
      match _c10[1]:
        case 0:
          print(f"{enemies[0].name} escaped from the ball...")
        case 1:
          print(f"Almost had{enemies[0].name}!")
        case 2:
          print(f"Had a good chance to get {enemies[0].name}!")
        case 3:
          print(f"Barely failed to get {enemies[0].name}!")
    if _c11[0]:
      print(f"Congratulations! You captured {enemies[1].name}!")
      enemyclone2 = enemies[1]
      enemyclone2.capturedBall = ball
      if randint(1,4096) == 4096:
        enemyclone2.shiny = shiny
      if randint(1,100) == 100:
        enemyclone2.lucky = True
      playerData[0].append(enemyclone2)
      save.save(playerData)
      if not enemyclone2.name in playerdata[2]:
        pass
        # register pokedex; wip
    else:
      match _c11[1]:
        case 0:
          print(f"{enemies[1].name} escaped from the ball...")
        case 1:
          print(f"Almost had{enemies[1].name}!")
        case 2:
          print(f"Had a good chance to get {enemies[1].name}!")
        case 3:
          print(f"Barely failed to get {enemies[1].name}!")
    
