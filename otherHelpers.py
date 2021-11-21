import cryptocompare
from replit import db


default_money = 400
winai = {
    "CHERRIES" : 0,
    "SEVEN" : 0,
    "DIAMOND" : 0,
    "GRAPE" : 0,
    "WATERMELON" : 0,
    "BELL" : 0
}

def updatintDatabase():
  for i in range(len(db.keys())):
    try:
      if len(db[i]) != 7:
        id = db[i][0]
        money = db[i][1]
        day = db[i][2]
        try:
          doge = db[i][3]
        except IndexError:
          doge = 0
        try:
          ticket = db[i][4]
        except IndexError:
          ticket = 0
        try:
          wins = db[i][5]
        except IndexError:
          wins = winai
        salys = {'Norvegija': 0, 'Švedija': 0, 'Suomija': 0, 'Danija': 0, 'Estija': 0, 'Latvija': 0, 'Lietuva': 0, 'Lenkija': 0, 'Vokietija': 0, 'Nyderlandai': 0, 'Belgija': 0, 'Liuksemburgas': 0, 'Prancūzija': 0, 'Ispanija': 0, 'Portugalija': 0, 'Italija': 0, 'Čekija': 0, 'Austrija': 0, 'Slovakija': 0, 'Vengrija': 0, 'Slovėnija': 0, 'Šveicarija': 0, 'Kroatija': 0, 'Graikija': 0, 'Rumunija': 0, 'Bulgarija': 0, 'Kipras': 0, 'Malta': 0, 'Juodkalnija': 0, 'Airija': 0, 'Islandija': 0}
        del db[i]
        db[i] = id, money, day, doge, ticket, wins, salys
        print("completed.")
    except KeyError:
      continue
  return None

def resetintPlayeriuSalis():
  for i in range(len(db.keys())):
    try:
      if len(db[i]) == 7:
        id = db[i][0]
        money = db[i][1]
        day = db[i][2]
        doge = db[i][3]
        ticket = db[i][4]
        wins = db[i][5]
        salys = {'Norvegija': 0, 'Švedija': 0, 'Suomija': 0, 'Danija': 0, 'Estija': 0, 'Latvija': 0, 'Lietuva': 0, 'Lenkija': 0, 'Vokietija': 0, 'Nyderlandai': 0, 'Belgija': 0, 'Liuksemburgas': 0, 'Prancūzija': 0, 'Ispanija': 0, 'Portugalija': 0, 'Italija': 0, 'Čekija': 0, 'Austrija': 0, 'Slovakija': 0, 'Vengrija': 0, 'Slovėnija': 0, 'Šveicarija': 0, 'Kroatija': 0, 'Graikija': 0, 'Rumunija': 0, 'Bulgarija': 0, 'Kipras': 0, 'Malta': 0, 'Juodkalnija': 0, 'Airija': 0, 'Islandija': 0}
        del db[i]
        db[i] = id, money, day, doge, ticket, wins, salys
        print("completed.")
      else:
        updatintDatabase()
    except KeyError:
      continue
  return None

def printOutAllDatabase():
  for i in range(len(db.keys())):
    try:
      print(db[i])
    except KeyError:
      continue
  return None

def getDogePrice(): # reik pakeist nes trugdo
  DOGE = cryptocompare.get_price('DOGE', currency='EUR', full=False)
  DogeEur = DOGE["DOGE"]["EUR"]
  return DogeEur

def getSafePrice():
  SAFE = cryptocompare.get_price('SAFEMOON', currency='EUR', full = False)
  SafeEur = SAFE["SAFEMOON"]["EUR"]
  return SafeEur

def kableliai(suma):
  sumastr = ""
  suma = str(suma)
  padetas = 0
  if len(suma) >= 4:
    for i in reversed(range(len(suma))):
      if padetas == 3:
        sumastr = ''.join((suma[i], "," + sumastr))
        padetas = 1
      else:
        padetas += 1
        sumastr = ''.join((suma[i], sumastr))
  if sumastr == "":
    sumastr = str(suma)
  return sumastr
  
def get_spot(id):
  for i in range(len(db.keys())):
    try:
      if id == db[i][0]:
        return i
    except KeyError:
      continue
  return None

def addme(message):
  if db.keys() == None or db[0] == None:
    db[0] = message.author.id, default_money, 0, 0, 0, winai
  else:
    for i in range(len(db.keys())-5):
      if message.author.id == db[i][0]:
        return False
    db[len(db.keys())-5] = message.author.id, default_money, 0, 0, 0, winai

def turtingumoInspekcija():
  turtingi = []
  for i in range(len(db.keys())):
    try:
      if db[i][1] > 1000000:
        turtingi.append(db[i][0])
    except IndexError:
      continue
    except KeyError:
      continue
  return turtingi

def bomzuInspekcija():
  bomzai = []
  playeriai = [211832708530307082, 475075704992563200, 315411412455260161, 469084309228093440, 313727222953279488, 337336281782550530, 204496800919453697, 554273438022500353] # beveik isitikines kad kazka pamirsau
  for i in range(len(db.keys())):
    try:
      if db[i][1] < 500000 and db[i][0] in playeriai:
        bomzai.append(db[i][0])
    except IndexError:
      continue
    except KeyError:
      continue
  return bomzai

def leaderboard():
  pinigai = [[]]
  for i in range(len(db.keys())):
    try:
      pinigai.append([db[i][1], db[i][0]])
    except IndexError:
      continue
    except KeyError:
      continue
  pinigai.sort(reverse=True)
  return pinigai

def ticketboard():
  ticketai = []
  for i in range(len(db.keys())):
    try:
      if db[i][4] == 1:
        ticketai.append(db[i][0])
    except IndexError:
      continue
    except KeyError:
      continue
  return ticketai

def slotsboard():
  trump = ["CHERRIES", "GRAPE", "WATERMELON", "BELL", "SEVEN", "DIAMOND"]
  top = {
    "CHERRIES" : 0,
    "GRAPE" : 0,
    "WATERMELON" : 0,
    "BELL" : 0,
    "SEVEN" : 0,
    "DIAMOND" : 0
  }
  ids = {
    "CHERRIES" : 0,
    "GRAPE" : 0,
    "WATERMELON" : 0,
    "BELL" : 0,
    "SEVEN" : 0,
    "DIAMOND" : 0
  }
  for i in range(len(db.keys())):
    try:
      for j in range(6):
        if db[i][5][trump[j]] > top[trump[j]]:
          top[trump[j]] = db[i][5][trump[j]]
          ids[trump[j]] = db[i][0]
    except IndexError:
      continue
    except KeyError:
      continue
  return top, ids

def update(message, searchedID):
  searchedMoney = int(db[searchedID][1])
  searchedDay = int(db[searchedID][2])
  searchedDoge = int(db[searchedID][3])
  Ticket = int(db[searchedID][4])
  del db[searchedID]
  db[searchedID] = message.author.id, searchedMoney + 1, searchedDay, searchedDoge, Ticket, winai # neprimetu kaip tas +1 atsirado bet palieku
  print("ADDED!!!!!")
