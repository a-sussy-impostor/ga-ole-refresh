class Type():
  def __init__(self, weak, resist, immune):
    self.weak = weak
    self.resist = resist
    self.immune = immune
    del weak, resist, immune

tNormal = 0; tFighting = 0; tFlying = 0; tBug = 0; tGrass = 0; tFire = 0; tWater = 0; tElectric = 0; tGround = 0; tRock = 0; tSteel = 0; tPoison = 0; tGhost = 0; tDark = 0; tFairy = 0; tPsychic = 0; tDragon = 0; tIce = 0; 
tNormal = Type([tFighting],[],[tGhost])
tFighting = Type([tFlying,tPsychic,tFairy],[tBug,tRock,tDark],[])
tFlying = Type([tElectric,tIce,tRock],[tBug,tGrass,tFighting],[tGround])
tBug = Type([tFire,tFlying,tRock],[tGrass,tGround,tFighting],[])
tGrass = Type([tFire,tFlying,tBug,tPoison,tIce],[tGrass,tWater,tElectric,tGround],[])
tFire = Type([tWater,tRock,tGround],[tBug,tGrass,tSteel,tFairy,tIce,tFire],[])
tWater = Type([tElectric,tGrass],[tFire,tIce,tWater,tSteel],[])
tElectric = Type([tGround],[tElectric,tFlying,tSteel],[])
tGround = Type([tGrass,tWater,tIce],[tPoison,tRock],[tElectric])
tRock = Type([tGround,tFighting,tGrass,tWater,tSteel],[tNormal,tPoison,tFlying,tFire],[])
tSteel = Type([tGround,tFighting,tFire],[tNormal,tFlying,tBug,tGrass,tRock,tSteel,tFairy,tPsychic,tDragon,tIce],[tPoison])
tPoison = Type([tGround,tPsychic],[tBug,tPoison,tFighting,tGrass,tFairy],[])
tGhost = Type([tGhost,tDark],[tPoison,tBug],[tNormal,tFighting])
tDark = Type([tFairy,tFighting,tBug],[tGhost,tDark],[tPsychic])
tFairy = Type([tPoison,tSteel],[tDark,tFighting,tBug],[tDragon])
tPsychic = Type([tGhost,tDark,tBug],[tFighting,tPsychic],[])
tDragon = Type([tDragon,tIce,tFairy],[tGrass,tFire,tWater,tElectric],[])
tIce = Type([tFire,tRock,tSteel,tFighting],[tIce],[])

def match(attackType,defenseType):
  attackT = [tNormal,tFighting,tFlying,tBug,tGrass,tFire,tWater,tElectric,tGround,tRock,tSteel,tPoison,tGhost,tDark,tFairy,tPsychic,tDragon,tIce][attackType]
  defenseT[0] = [tNormal,tFighting,tFlying,tBug,tGrass,tFire,tWater,tElectric,tGround,tRock,tSteel,tPoison,tGhost,tDark,tFairy,tPsychic,tDragon,tIce][defenseType]
  if len(defenseT) > 1:
    defenseT[1] = [tNormal,tFighting,tFlying,tBug,tGrass,tFire,tWater,tElectric,tGround,tRock,tSteel,tPoison,tGhost,tDark,tFairy,tPsychic,tDragon,tIce][defenseType]
  totalmulti = 1
  if attackT in defenseT[0].weak:
    totalmulti *= 2
  elif attackT in defenseT[0].resist:
    totalmulti *= 0.5
  elif attackT in defenseT[0].immune:
    totalmulti *= 0
  else:
    totalmulti *= 1
    
  if len(defenseT) > 1:
   if attackT in defenseT[1].weak:
    totalmulti *= 2
   elif attackT in defenseT[1].resist:
    totalmulti *= 0.5
   elif attackT in defenseT[1].immune:
    totalmulti *= 0
   else:
    totalmulti *= 1
  return totalmulti

