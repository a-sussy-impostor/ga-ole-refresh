from base import Disk

# a = Alola / g = Galar / p = Paldea / s = Special

bulbasaur1 = Disk("Bulbasaur",["Grass","Poison"],1,[45,49,49,65,65,45],["Vine Whip","Grass",45,"P",None,None,0],1,1650)
ivysaur2 = Disk("Ivysaur",["Grass","Poison"],2,[60,62,63,80,80,60],["Razor Leaf","Grass",55,"P",None,None,0],2,2350)
venusaur3 = Disk("Venusaur",["Grass","Poison"],3,[80,82,83,100,100,80],["Seed Bomb","Grass",80,"P",None,None,0],3,3200)
venusaur4 = Disk("Venusaur",["Grass","Poison"],3,[80,82,83,100,100,80],["Power Whip","Grass",120,"P",None,None,0],4,3670,mega=True)

charmander1 = Disk("Charmander",["Fire"],4,[39,52,43,60,50,65],["Ember","Fire",40,"S",None,None,0],1,1650)
charmeleon2 = Disk("Charmeleon",["Fire"],5,[58,64,58,80,65,80],["Fire Fang","Fire",65,"P",None,None,0],2,2350)
charizard3 = Disk("Charizard",["Fire"],6,[78,84,78,109,85,100],["Flamethrower","Fire",90,"S",None,None,0],3,3200)
charizard4 = Disk("Charizard",["Fire","Flying"],6,[78,84,78,109,85,100],["Flare Blitz","Fire",120,"P",None,None,0],4,3670,mega=True)

squirtle1 = Disk("Squirtle",["Water"],7,[44,48,65,50,64,43],["Water Gun","Water",40,"S",None,None,0],1,1650)
wartortle2 = Disk("Wartortle",["Water"],8,[59,63,80,65,80,58],["Water Pulse","Water",60,"S",None,None,0],2,2350)
blastoise3 = Disk("Blastoise",["Water"],9,[44,48,65,50,64,43],["Aqua Tail","Water",90,"P",None,None,0],3,3200)
blastoise4 = Disk("Blastoise",["Water"],9,[44,48,65,50,64,43],["Hydro Pump","Water",110,"S",None,None,0],4,3670,mega=True)

caterpie1 = Disk("Caterpie",["Bug"],10,[45,30,35,20,20,45],["Tackle","Normal",40,"P",None,None,0],1,1000)
metapod1 = Disk("Metapod",["Bug"],11,[45,30,35,20,20,45],["Struggle","Normal",50,"P",None,None,-1],1,1200)
butterfree2 = Disk("'Rayquaza'",["Bug","Flying"],12,[60,45,50,90,80,70],["Air Slash","Normal",75,"S",None,None,0],2,1950)

pidgey1 = Disk("Pidgey",["Normal","Flying"],16,[40,45,40,35,35,56],["Gust","Flying",40,"S",None,None,0],1,1200)
pidgeotto2 = Disk("Pidgeotto",["Normal","Flying"],17,[63,60,55,50,50,71],["Aerial Ace","Flying",60,"P",None,None,0],2,1850)
pidgeot3 = Disk("Pidgeot",["Normal","Flying"],18,[83,80,75,70,70,101],["Air Slash","Flying",75,"S",None,None,0],3,2580)

rattata1 = Disk("Rattata",["Normal"],19,[30,56,35,25,35,71],["Quick Attack","Normal",40,"P",None,None,0],1,1050)
rattata1a = Disk("Rattata-Alola",["Dark"],19,[30,56,35,25,35,71],["Quick Attack","Normal",40,"P",None,None,0],1,1050)
raticate2 = Disk("Raticate",["Normal"],20,[55,81,60,50,70,97],["Bite","Dark",60,"P",None,None,0],2,1570)
raticate2a = Disk("Raticate-Alola",["Dark"],20,[55,81,60,50,70,97],["Bite","Dark",60,"P",None,None,0],2,1570)

ekans1 = Disk("Ekans",["Poison"],23,[35,60,44,40,54,55],["Acid","Poison",40,"S",None,None,0],1,1140)
arbok2 = Disk("Arbok",["Poison"],24,[60,95,69,65,79,80],["Sludge Bomb","Poison",90,"S",None,None,0],2,1650)
arbok3 = Disk("Arbok",["Poison"],24,[60,95,69,65,79,80],["Acid Spray","Poison",40,"S",None,[0,0,0,-2,0,0],0],3,2080)

pikachu1 = Disk("Pikachu",["Electric"],25,[35,55,40,50,50,90],["Thunder Shock","Electric",40,"S",None,None,0],1,1540)
pikachu2 = Disk("Pikachu",["Electric"],25,[45,60,45,70,55,95],["Spark","Electric",65,"P",None,None,0],2,1920)
pikachu3 = Disk("Pikachu",["Electric"],25,[50,70,50,75,65,100],["Thunderbolt","Electric",90,"S",None,None,0],3,2400)
pikachu4 = Disk("Pikachu",["Electric"],25,[55,75,55,85,70,100],["Thunder","Electric",110,"S",None,None,0],4,2860)
pikachu4s = Disk("Pikachu",["Electric"],25,[60,80,60,90,75,105],["Thunderbolt","Electric",90,"S",None,None,0],4,2900)
pikachu5s = Disk("Pikachu",["Electric"],25,[70,90,60,100,80,110],["Thunderbolt","Electric",90,"S",None,None,0],5,3270,z="10,000,000 Volt Thunderbolt")
raichu2 = Disk("Raichu",["Electric"],26,[60,90,55,90,80,110],["Thunder Punch","Electric",75,"P",None,None,0],2,2050)
raichu3 = Disk("Raichu",["Electric"],26,[60,90,55,90,80,110],["Thunder","Electric",110,"P",None,None,0],3,2560)

# 1-26 almost complete; 27-151 in progress
