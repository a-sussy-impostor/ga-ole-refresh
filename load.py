playerData = []
serverData = []
import save
# import requests

if __name__ == "__load__":
  try:
    playerData = save.load()
    notplayed = False
  except EOFError:
    logging.warning("No save file detected")
    notplayed = True
    save.save([])

