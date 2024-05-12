from os import system as sys
sys("pip3 install colorama")

from base import *
from colorama import Fore as fore
testing = Disk("Pikachu","Electric",25,[35,55,40,50,50,90],["Thunderbolt","Electric",90,"S",None,None],2,1500)
testing2 = Disk("Charmander","Fire",25,[35,55,40,50,50,90],["Flamethrower","Fire",90,"S",None,None],2,1500)

print(testing.name)
print("Hello World")
print(testing.Attack(testing2))
