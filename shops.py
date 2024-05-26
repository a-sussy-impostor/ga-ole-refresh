from prerun import *

def shop(pokedollar):
  print("~ Shop ~")
  print("Welcome to the shop! You can buy poke balls and held items (coming soon). You can also play the lottery.")
  print("===== Poke Balls =====")
  print(f"1. {cOrange}Broken Ball{rReset} - An old ball that doesn't seem to work. (FREE)")
  print(f"2. {sDim}Rusted Ball{rReset} - A ball that has lower catch chance and bad aesthetics. Tbh, who uses this? (₽40)")
  print(f"3. {cRed}Poke Ball{rReset} - The single most common ball you'll see. (₽200)")
  print(f"4. {cBlue}Great Ball{rReset} - Works better than a poke ball. That's all. (₽400)")
  print(f"5. {cYellow}Ultra Ball{rReset} - Much better than a poke ball. Even capable of catching rare pokemon. (₽700)")
  print(f"6. {cPurple}Master Ball{rReset} - The most high-tech ball ever. Can catch any pokemon without fail. (₽19999)")
  print(f"7. {cCyan}Quick Ball{rReset} - A high-tech poke ball. Catches better when thrown at the start of a battle. (₽1500)")
  print(f"8. {cBlue}{sDim}Dusk Ball{rReset} - A pokeball that gains power from the moon. Better use it at night. (₽1000)")
  print(f"9. {cRed}{sDim}Fast Ball{rReset} - Less impactful but easier to use Quick Ball. Recommended to throw within 3 turns of a battle. (₽1200)")
  print(f"10. {cOrange}{sDim}Level Ball{rReset} - A rare poke ball that works well on weak pokemon. (₽1000)")
  print(f"11. {cRed}Premier{rReset} Ball - A ball that is made for people to flex. (₽500)")
  print(f"12. {cOrange}Repeat {cYellow}Ball - (No actual effect yet.) (₽1000)")
  print(f"13. Timer {cRed}Ball{rReset} - A ball that charges overtime. Works better the longer the battle. (₽1200)")
  print(f"14. {cGreen}Nest Ball{rReset} - A ball that works better on pokemon with low energy. (₽1000)")
  print(f"15. {cRed}Luxury {cYellow}Ball{rReset} - This ball is expensive. Maybe because myths say it makes your pokemon luckier. (₽1999)")
  print(f"16. {cPink}Dream Ball{rReset} - This ball collects energy from people's dreams. Works much better at midnight. (₽1200)")
  print(f"17. {cBlue}Beast {cYellow}Ball{rResst} - This ball is designed to catch ultra beasts by The Aether Foundation and doesn't get affected by ultra beast's aura. It doesn't work too well on other pokemon tho. (₽2000)")
  print(f"18. {cLime}Strange Ball{rReset} - This suspiciously just randomly appeared in this shop and somehow always successfully catches any pokemon, no matter it's a Caterpie or Rayquaza, half of the time. (₽7777)")
  print(f"19. {cBlue}Net {cLime}Ball{rReset} - This ball works well on bugs and oceanic creatures, and also specifically one legendary. (₽1300)")
  print()
  print("| Held Items |")
  print("Coming Soon")
  print()
  print("$ Lottery $")
  print("Coming very soon")
  _vinput = False
  while _vinput == False:
    buying = input("What would you like to buy? Enter number: ")
    if int(buying) in range(1,20):
      _vinput = True
    else:
      print("Invalid input. Try again.")
  del _vinput
  try:
    quan = int(input("How many? "))
    if quan < 1:
      print("Are you buying or not?")
      return [None]
  except TypeError:
    print("Invalid number. Buying 1 of the specified item.")
    quan = 1
  match int(buying):
    case 1:
      print(f"You got {quan} {cOrange}Broken Ball{rReset}(s)! Yay??")
      return ['brokenball',quan,0]
    case 2 if pokedollar >= 50*quan:
      print(f"You bought {quan} {sDim}Rusted Ball{rReset}(s) for ₽{50*quan}!")
      return ['rustedball',quan,-50*quan]
    case 3 if pokedollar >= 200*quan:
      print(f"You bought {quan} {cRed}Poke Ball{rReset}(s) for ₽{200*quan}!")
      return ['pokeball',quan,-200*quan]
    case 4 if pokedollar >= 400*quan:
      print(f"You bought {quan} {cBlue}Great Ball{rReset}(s) for ₽{400*quan}!")
      return ['greatball',quan,-400*quan]
    case 5 if pokedollar >= 700*quan:
      print(f"You bought {quan} {cYellow}Ultra Ball{rReset}(s) for ₽{700*quan}!")
      return ['ultraball',quan,-700*quan]
    case 6 if pokedollar >= 19999*quan:
      print(f"You bought {quan} {cPurple}Master Ball{rReset}(s) for ₽{19999*quan}!")
      return ['masterball',quan,-19999*quan]
    case 7 if pokedollar >= 1500*quan:
      print(f"You bought {quan} {sDim}Rusted Ball{rReset}(s) for ₽{1500*quan}!")
      return ['quickball',quan,-1500*quan]
    case 8 if pokedollar >= 1000*quan:
      print(f"You bought {quan} {cBlue}{sDim}Rusted Ball{rReset}(s) for ₽{1000*quan}!")
      return ['duskball',quan,-1000*quan]
    case 9 if pokedollar >= 1200*quan:
      print(f"You bought {quan} {cRed}{sDim}Rusted Ball{rReset}(s) for ₽{1200*quan}!")
      return ['fastball',quan,-1200*quan]
    case 10 if pokedollar >= 1000*quan:
      print(f"You bought {quan} {cOrange}{sDim}Level Ball{rReset}(s) for ₽{1000*quan}!")
      return ['levelball',quan,-1000*quan]
    case 11 if pokedollar >= 500*quan:
      print(f"You bought {quan} {cRed}Premier{rReset} Ball (s) for ₽{500*quan}! Rich people be like: ")
      return ['premierball',quan,-500*quan]
    case 12 if pokedollar >= 1000*quan:
      print(f"You bought {quan} {sDim}Repeat Ball{rReset}(s) for ₽{1000*quan}! Are you stupid?") #delete stupid later
      return ['repeatball',quan,-1000*quan]
    case 13 if pokedollar >= 1200*quan:
      print(f"You bought {quan} Timer{cRed} Ball{rReset}(s) for ₽{1200*quan}!")
      return ['timerball',quan,-1200*quan]
    case 14 if pokedollar >= 1000*quan:
      print(f"You bought {quan} {cGreen}Nest Ball{rReset}(s) for ₽{1000*quan}!")
      return ['nestball',quan,-1000*quan]
    case 15 if pokedollar >= 1999*quan:
      print(f"You bought {quan} {cRed}Luxury{cYellow} Ball{rReset}(s) for ₽{1999*quan}!")
      return ['luxuryball',quan,-1999*quan]
    case 16 if pokedollar >= 1200*quan:
      print(f"You bought {quan} {cPink}Dream Ball{rReset}(s) for ₽{1200*quan}!")
      return ['rustedball',quan,-1200*quan]
    case 17 if pokedollar >= 2000*quan:
      print(f"You bought {quan} {cBlue}Beast {cYellow}Ball{rReset}(s) for ₽{2000*quan}! By the way ultra beasts aren't in the game yet.") #edit later
      return ['rustedball',quan,-2000*quan]
    case 18 if pokedollar >= 7777*quan:
      print(f"You bought {quan} {cLime}Strange Ball{rReset}(s) for ₽{7777*quan}! Strange.")
      return ['rustedball',quan,-7777*quan]
    case 19 if pokedollar >= 1300*quan:
      print(f"You bought {quan} {cBlue}Net{cCyan} Ball{rReset}(s) for ₽{1300*quan}!")
      return ['rustedball',quan,-1300*quan]
    case _:
      print("Not enough money lol")
      return [None]
