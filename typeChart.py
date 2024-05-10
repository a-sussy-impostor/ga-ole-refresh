class Type():
  def __init__(self, weak, resist, immune):
    self.weak = weak
    self.resist = resist
    self.immune = immune
    del weak, resist, immune

tNormal = Type([tFighting],[],[tGhost])
tFighting = Type([tFlying,tPsychic,tFairy],[tBug,tRock,tDark],[])
tFlying = Type([tElectric,tIce,tRock],[tBug,tGrass,tFighting],[])

def match(type1,type2):
  # dummy
  return 1
