from prerun import *
sys("pip3 install pickle")
from base import *

testing = Disk("Pikachu","Electric",25,[35,55,40,50,50,90],["Thunderbolt","Electric",90,"S",None,None],2,1500)
testing2 = Disk("Charmander","Fire",25,[35,55,40,50,50,90],["Flamethrower","Fire",90,"S",None,None],2,1500)

print(testing.name)
print(sBright + "Hello World")
print(testing.Attack(testing2))
print(cRed + "hi")
print(cCyan + "hello")
