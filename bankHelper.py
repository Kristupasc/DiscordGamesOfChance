from replit import db
from datetime import datetime
import checksHelper, otherHelpers

def pridetBankui(bet, normalus, message):
  pinigai = db['bankas'][0]
  searchedID = otherHelpers.get_spot(message.author.id)
  diena = db['bankas'][1]
  isStarted = db['bankas'][2]
  isEnded = db['bankas'][3]
  if normalus and db[searchedID][1] * 0.1 <= bet:
    if bet >= 10000 and bet <= 1000000:
     bet = bet / 10000
     percent = (-0.0025 * (bet**2)) - (0.2 * bet) + 60
     bet = bet * 10000
     bet = (bet * percent) / 100
    elif bet < 10000 and bet != 500:
     bet = (bet * 60) / 100
    elif bet == 500:
     bet = (bet * 40) / 100
    else:
     bet = (bet * 25) / 100
    bet = (bet * 75) / 100
    pinigai += bet
    del db['bankas']
    db['bankas'] = pinigai, diena, isStarted, isEnded
  elif not normalus:
    if bet >= 10000 and bet <= 1000000:
     bet = bet / 10000
     percent = (-0.0025 * (bet**2)) - (0.2 * bet) + 60
     bet = bet * 10000
     bet = (bet * percent) / 100
    elif bet < 10000 and bet != 500:
     bet = (bet * 60) / 100
    elif bet == 500:
     bet = (bet * 40) / 100
    else:
     bet = (bet * 25) / 100
    bet = (bet * 35) / 100
    pinigai += bet
    del db['bankas']
    db['bankas'] = pinigai, diena, isStarted, isEnded

# def paimtIsBanko(bet):
#   print("keisk")
#   pinigai = db['bankas']
#   pinigai -= bet
#   del db['bankas']
#   db['bankas'] = pinigai

def pradetiBanka():
  diena = db['bankas'][1]
  del db['bankas']
  db['bankas'] = 0, diena, True, False

def pabaigtBanka():
  now = datetime.now()
  diena = now.day + 1
  if now.day + 1 > 31:
    diena = 1
  del db["bankas"]
  db["bankas"] = 0, diena, False, True
  for i in range(len(db.keys()) - 5):
    try:
      if db[i][4] == 1:
        dataID = db[i][0]
        searchedID = checksHelper.get_spot(dataID)
        searchedMoney = int(db[searchedID][1])
        searchedDoge = int(db[searchedID][3])
        searchedDay = int(db[searchedID][2])
        searchedWins = db[searchedID][5]
        del db[searchedID]
        db[searchedID] = dataID, searchedMoney, searchedDay, searchedDoge, 0, searchedWins
    except IndexError:
      continue
    except KeyError:
      continue

