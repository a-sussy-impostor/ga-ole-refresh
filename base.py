from random import choice, randint, uniform
from math import floor, ceil, round
import typeChart, time, datetime
from os import system as sys

class Disk:
  def __init__(self, name, type, number, bst, move, star, energy , catchrate = 5, capturedBall = None, ability = None, special = None, mega = None, z = None, fuse = None, shiny = False, lucky = False):
    self.name = name
    self.type = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"].index(type)
    self.number = number
    self.bst = bst
    self.move = [move[0],["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"].index(move[1]),move[2],move[3],move[4],move[5]] # [name, type, power, ps, user stat change, target stat change] # PS = P/S/N
    self.star = star
    self.ability = ability
    self.energy = energy
    self.special = special # ub = Ultra Beast; lg = Legend; my = Mythical ; ss = Super Strong
    self.mega = mega
    self.shiny = shiny # 1/4000 chance
    self.lucky = lucky # 1% chance
    self.level = round(self.energy/30) + 30 # hidden
    if z != None:
      self.z = ["Breakneck Blitz","All-Out Pummeling","Supersonic Skystrike","Acid Downpour","Tectonic Rage","Continental Crush","Savage Spin-Out","Never-Ending Nightmare","Corkscrew Crash","Inferno Overdrive","Hydro Vortex","Bloom Doom","Gigavolt Havoc","Shattered Psyche","Subzero Slammer","Devastating Drake","Black Hole Eclipse","Twinkle Tackle","Catastropika","Sinister Arrow Raid","Malicious Moonsault","Oceanic Operetta","Guardian of Alola","Soul-Stealing 7-Star Strike","Stoked Sparksurfer","Pulverizing Pancake","Extreme Evoboost","Genesis Supernova","10,000,000 Volt Thunderbolt","Light That Burns the Sky","Searing Sunraze Smash","Menacing Moonraze Maelstrom","Let's Snuggle Forever","Splintered Stormshards","Clangorous Soulblaze"].index(z)
    else:
      self.z = None
    self.fuse = fuse # list
    del name, type, number, bst, move, star, energy, special, mega, z, fuse, ability
  def Attack(self, enemy,selfch = [1,1,1,1,1,1],enemych = [1,1,1,1,1,1]): # Stat changes: [Attack, Defense, Sp. Atk, Sp. Def, Spe, Crit]
    selfSC = [0,0,0,0,0,0]
    enemySC = [0,0,0,0,0,0]
    if self.move[4] != None:
      contCheck = [1,1]
      if self.ability == "Contrary":
        contCheck[0] = -1
      if enemy.ability == "Contrary":
        contCheck[1] = -1
      if enemy.ability == "Defiant":
        if min(self.move[5]) < 0:
          enemySC[0] += 2
      if enemy.ability == "Competitive":
        if min(self.move[5]) < 0:
          enemySC[2] += 2
      selfSC[0] += self.move[4][0] * contCheck[0]
      selfSC[1] += self.move[4][1] * contCheck[0]
      selfSC[2] += self.move[4][2] * contCheck[0]
      selfSC[3] += self.move[4][3] * contCheck[0]
      selfSC[4] += self.move[4][4] * contCheck[0]
      selfSC[5] += self.move[4][5] * contCheck[0]
      enemySC[0] += self.move[5][0] * contCheck[1]
      enemySC[1] += self.move[5][1] * contCheck[1]
      enemySC[2] += self.move[5][2] * contCheck[1]
      enemySC[3] += self.move[5][3] * contCheck[1]
      enemySC[4] += self.move[5][4] * contCheck[1]
      enemySC[5] += self.move[5][5] * contCheck[1]
      del contCheck
    if self.move[3] == "P":
      getbst = [1,2]
    elif self.move[3] == "S":
      getbst = [3,4]
    else:
      getbst = None
      
    if self.move[3] != "N":
      stab = 1
      crit = 1
      item = 1
      selfchnew = None
      enemychnew = None
      if self.move[1] == self.type:
        stab *= 1.5
      if randint(1,16) >= 16/selfch[5]:
        crit *= 1.5
        if selfch[(getbst[0] - 1)] < 1:
          selfchnew = 1
        if enemych[(getbst[0] - 1)] > 1:
          enemychnew = 1
      multi = stab*typeChart.match(self.move[1],enemy.type)*crit*item
      if selfchnew != None or enemychnew != None:
        attack = (((self.bst[getbst[0]]*2+31+252/4)*self.level)/100+5)*selfchnew
        defense = (((enemy.bst[getbst[1]]*2+31+252/4)*enemy.level)/100+5)*enemychnew
        powerBonus = choice([10,10,10,20,20,20,20,30,30,30,50])
        damage = round((((2*self.level)/250)*attack/defense*(self.move[2]+powerBonus)+2)*multi*uniform(0.8, 1))
      else:
        attack = (((self.bst[getbst[0]]*2+31+252/4)*self.level)/100+5)*selfch[0]
        defense = (((enemy.bst[getbst[1]]*2+31+252/4)*enemy.level)/100+5)*enemych[1]
        powerBonus = choice([10,10,10,20,20,20,20,30,30,30,50])
        damage = round((((2*self.level)/250)*attack/defense*(self.move[2]+powerBonus)+2)*multi*uniform(0.8, 1))
      del attack, defense, powerBonus, multi, getbst, selfchnew, enemychnew, item, stab, crit
      return [damage,selfSC,enemySC]
    else:
      return [None,selfSC,enemySC]
    # still work in progress
  def Defense(self,damage):
    if damage != None:   
      addEffect = choice([0,1,0,2]) # 1 = +1 defense / 2 = Opponent -12% HP
      return addEffect
    else:
      return None
    # work in progress

def wait(sec): time.sleep(sec)
def clear(): sys("clear")
def enter():
  _i = input()
  del _i
