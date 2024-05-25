import pickle

def save(data):
  with open("savedata.pk","wb") as f:
    pickle.dump(data)
  # del f,g

def load():
  with open("savedata.pk","rb") as f:
    return pickle.load(f.read())
  # del f
