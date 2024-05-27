import pickle
import logging

def save(key,data):
  with open("savedata.pk","rb") as f:
    g = pickle.load(f)
  g[key] = data
  with open("savedata.pk","wb") as f:
    pickle.dump(g)
  # del f,g

def load(key):
  with open("savedata.pk","rb") as f:
    pickle.load(f)
  # del f
  try:
    return pickle[key]
  except:
    return
