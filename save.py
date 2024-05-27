import pickle
import json
from cryptography.fernet import Fernet
from os import environ
import logging

devmode = False

# Generate passkeys
if not 'savekey' in environ:
  key = Fernet.generate_key()
  environ['saveKey'] = key.decode()
else:
  key = environ['saveKey'].encode()


# Encrypt list
def encrypt(list):
  list_json = json.dumps(list)
  fernet = Fernet(key)
  return fernet.encrypt(list_json.encode())

# Decrypt list
def decrypt(json):
  fernet = Fernet(key)
  decrypted_json = fernet.decrypt(json).decode()
  return json.loads(decrypted_json)


def save(data):
  global devmode
  if not devmode:
    with open("savedata.pk","wb") as f:
      pickle.dump(encrypt(data))
  else:
    logging.info("Saving disabled due to developer mode ON")
  # del f,g

def load():
  with open("savedata.pk","rb") as f:
    return decrypt(pickle.load(f))
  # del f
