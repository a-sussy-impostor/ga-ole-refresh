from prerun import *
from os import getenv

if os.getenv("GITHUB_ACTIONS") == "true":
  print("Running on github actions")
  sys("pip3 install pickle")
  sys("pip install logging")

import logging
from base import *

logging.basicConfig(level=logging.INFO, filename="latest.log", filemode="w", format="%(asctime)s [%(levelname)s]: %(message)s")

testing = Disk("Pikachu","Electric",25,[35,55,40,50,50,90],["Thunderbolt","Electric",90,"S",None,None],2,1500)
testing2 = Disk("Charmander","Fire",25,[35,55,40,50,50,90],["Flamethrower","Fire",90,"S",None,None],2,1500)

logging.info(testing.name)
logging.info(sBright + "Hello World")
logging.info(testing.Attack(testing2))
logging.warning(cRed + "hi")
logging.warning(cCyan + "hello")
