from random import choice, randint
# from math import round, floor
import typeChart

class Disk:
  def __init__(self, name, type, number, bst, move, star, energy , special = None, mega = None, z = None, fuse = None):
    self.name = name
    self.type = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"].index(type)
    self.number = number
    self.bst = bst
    self.move = [move[0],["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"].index(move[1]),move[2],move[3]] # [name, type, power, ps] # PS = P/S/N
    self.star = star
    self.energy = energy
    self.special = special
    self.mega = mega
    self.level = self.energy/30 # hidden
    if z != None:
      self.z = ["Breakneck Blitz","All-Out Pummeling","Supersonic Skystrike","Acid Downpour","Tectonic Rage","Continental Crush","Savage Spin-Out","Never-Ending Nightmare","Corkscrew Crash","Inferno Overdrive","Hydro Vortex","Bloom Doom","Gigavolt Havoc","Shattered Psyche","Subzero Slammer","Devastating Drake","Black Hole Eclipse","Twinkle Tackle","Catastropika","Sinister Arrow Raid","Malicious Moonsault","Oceanic Operetta","Guardian of Alola","Soul-Stealing 7-Star Strike","Stoked Sparksurfer","Pulverizing Pancake","Extreme Evoboost","Genesis Supernova","10,000,000 Volt Thunderbolt","Light That Burns the Sky","Searing Sunraze Smash","Menacing Moonraze Maelstrom","Let's Snuggle Forever","Splintered Stormshards","Clangorous Soulblaze"].index(z)
    else:
      self.z = None
    self.fuse = fuse # list
    del name, type, number, bst, move, star, energy, special, mega, z, fuse
  def Attack(self, enemy,selfch = [1,1,1,1,1],enemych = [1,1,1,1,1]): # Stat changes: [Attack, Defense, Sp. Atk, Sp. Def, Spe, Crit]
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
        damage = (((2*self.level)/250)*attack/defense*(self.move[2]+powerBonus)+2)*multi
      else:
        attack = (((self.bst[getbst[0]]*2+31+252/4)*self.level)/100+5)*selfch[0]
        defense = (((enemy.bst[getbst[1]]*2+31+252/4)*enemy.level)/100+5)*enemych[1]
        powerBonus = choice([10,10,10,20,20,20,20,30,30,30,50])
        damage = (((2*self.level)/250)*attack/defense*(self.move[2]+powerBonus)+2)*multi
      return damage
      # work in progres
