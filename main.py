import discord
import os
from replit import db
import random
from keep_alive import keep_alive
from datetime import datetime
import cryptocompare
import requests


r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")

winai = {
    "CHERRIES" : 0,
    "SEVEN" : 0,
    "DIAMOND" : 0,
    "GRAPE" : 0,
    "WATERMELON" : 0,
    "BELL" : 0
}
client = discord.Client()
SLOTS = ["DIAMOND", "CHERRIES", "GRAPE", "WATERMELON", "BELL", "SEVEN"]
DOGE = cryptocompare.get_price('DOGE', currency='EUR', full=False) # rad
DogeEur = DOGE["DOGE"]["EUR"]
SAFE = cryptocompare.get_price('SAFEMOON', currency='EUR', full = False)
SafeEur = SAFE["SAFEMOON"]["EUR"]
print(DogeEur)
print('{:.8f}'.format(SafeEur))

db[9871] = -1
default_money = 400
searchedID = None
searchedMoney = 0
newMoney = 0
now = datetime.now()
print("Current day: " + str(now.day))


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

def pridetBankui(bet):
  pinigai = db['bankas'][0]
  diena = db['bankas'][1]
  isStarted = db['bankas'][2]
  isEnded = db['bankas'][3]
  #if bet >= 10000 and bet <= 1000000:
  #  bet = bet / 10000
  #  percent = (-0.0025 * (bet**2)) - (0.2 * bet) + 70
  #  bet = bet * 10000
  #  bet = (bet * percent) / 100
  #elif bet < 10000 and bet != 500:
  #  bet = (bet * 70) / 100
  #elif bet == 500:
  #  bet = (bet * 40) / 100
  #else:
  #  bet = (bet * 25) / 100
  bet = (bet * 25) / 100
  pinigai += bet
  del db['bankas']
  db['bankas'] = pinigai, diena, isStarted, isEnded

def paimtIsBanko(bet):
  print("keisk")
  #pinigai = db['bankas']
  #pinigai -= bet
  #del db['bankas']
  #db['bankas'] = pinigai

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
        searchedID = get_spot(dataID)
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


def coinflip(guess, bet):
  num = random.randint(1, 2)
  if num == 1 and guess == "herbas": 
    return True
  elif num == 2 and guess == "skaičius":
    return True
  elif num == 2 and guess == "skaicius":
    return True
  else:
    return False

def multipleCoinflips(guess, bet, times):
    correct = 0
    won = 0
    for i in range(times):
      num = random.randint(1,2)
      if num == 1 and guess == "herbas":
        correct += 1 
        won += bet
      elif num == 2 and guess == "skaičius":
        correct += 1 
        won += bet
      elif num == 2 and guess == "skaicius":
        correct += 1 
        won += bet
      else:
          won -= bet
    return correct, won

def roll():
    num = random.randint(0, 5)
    return SLOTS[num]

def check(slot1, slot2, slot3):
    money = 0
    if slot1 == slot2 and slot2 == slot3:
        if slot1 == "CHERRIES":
            money = 62500
        elif slot1 == "GRAPE":
            money = 125000
        elif slot1 == "WATERMELON":
            money = 175000
        elif slot1 == "BELL":
            money = 250000
        elif slot1 == "SEVEN":
            money = 650000
        elif slot1 == "DIAMOND":
            money = 1250000
    elif slot1 == "DIAMOND" or slot2 == "DIAMOND" or slot3 == "DIAMOND":
        if slot1 == slot2 and slot1 == "DIAMOND":
            money = 25000
        elif slot2 == slot3 and slot2 == "DIAMOND":
          money = 25000
        elif slot1 == slot3 and slot3 == "DIAMOND":
          money = 25000
        else:
          money = 7500
    return money

def game():
    slot1 = roll()
    slot2 = roll()
    slot3 = roll()
    decision = random.randint(1,5)
    if slot1 == slot2 and slot2 == slot3 and slot1 != "CHERRIES" and slot1 != "GRAPE":
        slot2 = roll()
    if slot1 == slot2 and slot2 == slot3 and slot1 != "CHERRIES":
        slot3 = roll()
    if slot1 == "DIAMOND" and decision > 2:
      slot1 = roll()
    if slot3 == "DIAMOND" and decision > 2:
      slot3 = roll()
    if slot2 == "DIAMOND" and decision > 2:
      slot2 = roll()
    if slot1 == slot2 and slot2 == slot3 and slot1 != "CHERRIES" and decision > 4:
      slot2 = roll()
    money = check(slot1, slot2, slot3)
    return money, slot1, slot2, slot3

def roulette(guess, bet):
  red =  {1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,38,40}
  black = {2,4,6,8,10,11,15,17,19,20,22,24,26,28,29,31,33,35,37,39}
  green = {0, 36}
  even = {2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,38,40} #as nzn ar cia exploitas
  odd = {1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39}
  roll = random.randint(0, 40)
  print(roll)
  if guess.lower() == "raudona" and roll in red:
    return True
  elif guess.lower() == "juoda" and roll in black:
    return True
  elif (guess.lower() == "žalia" or guess.lower() == "zalia") and roll in green:
    return True
  elif guess.lower() == "lyginis" and roll in even:
    return True
  elif guess.lower() == "nelyginis" and roll in odd:
    return True
  return False

def numberGuesser(number, bet, limit):
    rnum = random.randint(1,limit)
    if number == rnum:
        return bet * (limit - 1), rnum
    else:
        return bet * -1, rnum

def get_spot(id):
  for i in range(len(db.keys())):
    try:
      if id == db[i][0]:
        return i
    except KeyError:
      print(i)
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

def checkForCoinflip(message, split_parts):
  if len(split_parts) == 4:
    try:
      if split_parts[1].lower() == "coinflip" and split_parts[2].lower() == "herbas" or split_parts[2].lower() == "skaičius" or split_parts[2].lower() == "skaicius" and (split_parts[3].isdecimal() or split_parts[3] == "random"): 
        return True
    except IndexError:
      return False

def checkForMultipleCoinflips(message, split_parts):
  try:
    if split_parts[1].lower() == "coinflip" and split_parts[2].lower() == "herbas" or split_parts[2].lower() == "skaičius" or split_parts[2].lower() == "skaicius" and split_parts[3].isdecimal() and split_parts[4].isdecimal():
      return True
  except IndexError:
    return False

def checkForRoulette(message, split_parts):
  try:
    if split_parts[1].lower() == "roulette":
      if split_parts[2].lower() == "lyginis" or split_parts[2].lower() == "nelyginis" or split_parts[2].lower() == "raudona" or split_parts[2].lower() == "juoda" or split_parts[2].lower() == "zalia" or split_parts[2].lower() == "žalia":
        if split_parts[3].isdecimal(): 
          return True
  except IndexError:
    return False

def checkForNumber(message, split_parts):
  try:
    if split_parts[1].lower() == "numeris" and split_parts[2].isdecimal() and split_parts[3].isdecimal() and split_parts[4].isdecimal():
      if int(split_parts[4]) % 2 == 0:
        return True
      else:
        return False
  except IndexError:
    return False

def checkForDoge(message, split_parts):
  if len(split_parts) == 4:
    try:
      if split_parts[1].lower() == "doge" and split_parts[2].lower() == "buy" or split_parts[2].lower() == "sell" and split_parts[3].isdecimal(): 
        return True
    except IndexError:
      return False

def checkForSafe(message, split_parts):
  if len(split_parts) == 4:
    try:
      if split_parts[1].lower() == "safemoon" and split_parts[2].lower() == "buy" or split_parts[2].lower() == "sell" and split_parts[3].isdecimal(): 
        return True
    except IndexError:
      return False

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

@client.event
async def on_ready():
  print("Bot is logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  now = datetime.now()
  channelServer = client.get_channel(825306731814846465)
  if message.author == client.user:
    return
  searchedID = get_spot(message.author.id)
  if now.weekday() == 1 and message.author.id == 699945002406510692:
    zinute = "Laikas surinkti rytinius mokesčius!\nMokesčiai buvo surinkti iš:\n"
    turtingi = turtingumoInspekcija()
    vargsai = bomzuInspekcija()
    mokestis = 0
    if len(turtingi) > 0 and len(vargsai) > 0:
      for i in range(len(turtingi)): # atimam 
        searchedID = get_spot(turtingi[i])
        searchedMoney = int(db[searchedID][1])
        Ticket = int(db[searchedID][4])
        searchedDay = int(db[searchedID][2])
        searchedDoge = int(db[searchedID][3])
        searchedWins = db[searchedID][5]
        newMoney = 0
        if searchedMoney < 15000000:
          mokestis += (searchedMoney * 5) / 100
          newMoney = searchedMoney - mokestis
        else:
          mokestis += (searchedMoney * 10) / 100
          newMoney = searchedMoney - mokestis
        del db[searchedID]
        db[searchedID] = turtingi[i], int(newMoney), searchedDay, searchedDoge, Ticket, searchedWins
        user = await client.fetch_user(turtingi[i])
        zinute += user.name + "\n"
      zinute += "Surinkti pinigai yra atiduodami šiem žmonėm:\n"
      for i in range(len(vargsai)): # atiduodam
        searchedID = get_spot(vargsai[i])
        searchedMoney = int(db[searchedID][1])
        Ticket = int(db[searchedID][4])
        searchedDay = int(db[searchedID][2])
        searchedDoge = int(db[searchedID][3])
        searchedWins = db[searchedID][5]
        newMoney = int(searchedMoney + (mokestis / len(vargsai)))
        del db[searchedID]
        db[searchedID] = vargsai[i], int(newMoney), searchedDay, searchedDoge, Ticket, searchedWins
        user = await client.fetch_user(vargsai[i])
        zinute += user.name + "\n"
      await channelServer.send(zinute)
      
  '''if now.weekday() == 0 and db["bankas"][2] == False:
    pradetiBanka()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="0 pinigų prize pool"))
  pinigai = int(db["bankas"][0])
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(pinigai) + " pinigų prize pool"))
  if now.weekday() == 6 and db["bankas"][2] == True and message.author.id == 699945002406510692:
    await channelServer.send("Eventas baigėsi! Laimėtojai:")
    ticketai = ticketboard()
    if len(ticketai) >= 3:
      ranum = random.randint(0, len(ticketai) - 1)
      user = await client.fetch_user(ticketai[ranum])
      suma = db["bankas"][0]
      sempro = int((suma * 60) / 100)
      await channelServer.send(str(user) + " 60% visos sumos! (" + str(sempro) + ")")
      searchedID = get_spot(ticketai[ranum])
      searchedMoney = int(db[searchedID][1])
      searchedDoge = int(db[searchedID][3])
      searchedDay = int(db[searchedID][2])
      searchedWins = db[searchedID][5]
      del db[searchedID]
      db[searchedID] = ticketai[ranum], searchedMoney + sempro, searchedDay, searchedDoge, 0, searchedWins
      while True:
        ranum2 = random.randint(0, len(ticketai) - 1)
        if ranum != ranum2:
          break
      user = await client.fetch_user(ticketai[ranum2])
      trimpro = int((suma * 30) / 100)
      await channelServer.send(str(user) + " 30% visos sumos! (" + str(trimpro) + ")")
      searchedID = get_spot(ticketai[ranum2])
      searchedMoney = int(db[searchedID][1])
      searchedDoge = int(db[searchedID][3])
      searchedDay = int(db[searchedID][2])
      searchedWins = db[searchedID][5]
      del db[searchedID]
      db[searchedID] = ticketai[ranum2], searchedMoney + trimpro, searchedDay, searchedDoge, 0, searchedWins
      while True:
        ranum3 = random.randint(0, len(ticketai) - 1)
        if ranum != ranum3 and ranum2 != ranum3:
          break
      user = await client.fetch_user(ticketai[ranum3])
      despro = int((suma * 10) / 100)
      await channelServer.send(str(user) + " 10% visos sumos! (" + str(despro) + ")")
      searchedID = get_spot(ticketai[ranum3])
      searchedMoney = int(db[searchedID][1])
      searchedDoge = int(db[searchedID][3])
      searchedDay = int(db[searchedID][2])
      searchedWins = db[searchedID][5]
      del db[searchedID]
      db[searchedID] = ticketai[ranum3], searchedMoney + despro, searchedDay, searchedDoge, 0, searchedWins
    elif len(ticketai) == 2:
      ranum = random.randint(0, len(ticketai) - 1)
      user = await client.fetch_user(ticketai[ranum])
      suma = db["bankas"][0]
      sempro = int((suma * 60) / 100)
      await channelServer.send(str(user) + " 60% visos sumos! (" + str(sempro) + ")")
      searchedID = get_spot(ticketai[ranum])
      searchedMoney = int(db[searchedID][1])
      searchedDoge = int(db[searchedID][3])
      searchedDay = int(db[searchedID][2])
      searchedWins = db[searchedID][5]
      del db[searchedID]
      db[searchedID] = ticketai[ranum], searchedMoney + sempro, searchedDay, searchedDoge, 0, searchedWins
      while True:
        ranum2 = random.randint(0, len(ticketai) - 1)
        if ranum != ranum2:
          break
      user = await client.fetch_user(ticketai[ranum2])
      trimpro = int((suma * 30) / 100)
      await channelServer.send(str(user) + " 30% visos sumos! (" + str(trimpro) + ")")
      searchedID = get_spot(ticketai[ranum2])
      searchedMoney = int(db[searchedID][1])
      searchedDoge = int(db[searchedID][3])
      searchedDay = int(db[searchedID][2])
      searchedWins = db[searchedID][5]
      del db[searchedID]
      db[searchedID] = ticketai[ranum2], searchedMoney + trimpro, searchedDay, searchedDoge, 0, searchedWins
    elif len(ticketai) == 1:
      user = await client.fetch_user(ticketai[0])
      suma = db["bankas"][0]
      sempro = int((suma * 60) / 100)
      await channelServer.send(str(user) + " 60% visos sumos! (" + str(sempro) + ")")
      searchedID = get_spot(ticketai[0])
      searchedMoney = int(db[searchedID][1])
      searchedDoge = int(db[searchedID][3])
      searchedDay = int(db[searchedID][2])
      searchedWins = db[searchedID][5]
      del db[searchedID]
      db[searchedID] = ticketai[0], searchedMoney + sempro, searchedDay, searchedDoge, 0, searchedWins
    pabaigtBanka()
  '''
  if client.user.mentioned_in(message) and str(message.channel.id) == str(channelServer.id):
    await message.reply("Kas yra")

  #istrint 449, 450 eilutes ir 452 eilutej elif pakeist i if
  elif message.content.lower().startswith("!r addme") and str(message.channel.id) == str(channelServer.id):
    if addme(message) == False:
      await channelServer.send("<@%s> jau yra pridėtas. " % message.author.id)
    else:
      await channelServer.send("<@%s> pridėtas. " % message.author.id + " Pradiniai pinigai: 400")
  #elif len(db[searchedID]) == 5:
    #update(message, searchedID)
  #elif message.content.lower().startswith("!r event pool") and str(message.channel.id) == str(channelServer.id):
    #await channelServer.send("Prize poole yra " + str(int(db["bankas"][0])) + " pinigų.") #Pinigai, patenkantys į prize poola yra nustatomi pagal šią funkciją:\n```f(x)= -0.0025x^2 -0.2x +70```x = (statoma suma / 10000). Ši funkcija veikia tik tada, kai pralaimėtų pinigų suma yra tarp 10,000 ir 1,000,000 pinigų.\nJeigu pinigų suma yra mažesnė negu 10,000, tada yra taikoma 70% taisyklė. Jeigu pinigų suma didesnė už 1 milijoną, taikoma 25% taisyklė.\nŠie procentai gali keistis savaites eigoje dėl galimos sistemos balansavimo.")
  #elif message.content.lower().startswith("!r event help") and str(message.channel.id) == str(channelServer.id):
    #await channelServer.send('```Šis eventas padės žmonėms susigrąžinti prarastus pinigus! Visą savaitę 25% prarastų pinigų eis į prize poolą (jeigu nori sužinoti tikslius procentus, rašyk !r event pool). Savaitės gale (sekmadienį) bus išrinkti trys žmonės, kurie gaus dalį šios sumos (60%, 30%, 10%). Norint dalyvauti šiame evente, reikia nusipirkti bilietą (bilietas galioja tik tą savaitę. Jo kaina - 30000 pinigų). Bilietą reikia pirkti rašant !r ticket buy. Taip pat parašydamas !r tickets gali sužinoti kokie žmonės yra nusipirkę po bilietą.```')

  elif message.content.lower().startswith("!r taisykles") and str(message.channel.id) == str(channelServer.id):
    await message.delete()

  elif message.content.lower().startswith("liaudies priesas") and str(message.channel.id) == str(channelServer.id):
    await message.delete()

  elif message.content.lower().startswith("!r lmao") and str(message.channel.id) == str(channelServer.id):
    await channelServer.send("lmao")

  elif message.content.lower().startswith("agrastas") and str(message.channel.id) == str(channelServer.id):
    await channelServer.send("norėtum")

  elif message.content.lower().startswith("!r patchnotes") and str(message.channel.id) == str(channelServer.id):
    seniausiNotes = '08/29/2021 patch notes:\n1. Pasikeitė !r daily galimybių lentelė:\n```30% - 1000\n5% - 1500\n30% - 2000\n15% - 3000\n14% - 4000\n6% - 30000```\n2. !r daily taip pat galima parašyti rašant: !к вфшдн arba !г суточный.\n3. !r praradau duoda 10 pinigų.\n4. Panaikinta event poolo funkcija. Nuo šiol visada į poola eina 25% pralaimėtos sumos.\n5. Botas nebėra case sensitive.\n6. Ticketo kaina dabar 30000 pinigų.\ncoming soon:\n1. nauji, brangesni slotai.\n\n\n'
    antriNotes = '09/03/2021\n```1. pasikeitė slots taisyklės. Odds išliko tie patys, tačiau kainos pasikeitė. !r slots help suteiks daugiau informacijos.\n2. Šios savaitės event kol kas bus paskutinis. Eventas bus sugrąžintas po *kelių* savaičių su naujomis taisyklėmis.\n3. pridėta balsavimo funkcija. !r balsuoti help dėl detalesnės informacijos.```\n\n\n'
    NaujausiNotes = '09/25/2021\n1. Pridėta komanda !r coinflip skaicius/herbas random (bet koks skaicius iš tavo pinigų kiekio(atsargiai)).\n2. Mokesčių sistema. Kiekviena antradienį yra surenkami 5% pinigų iš kiek vieno žmogaus, kuris turi daugiau negu 1 mil. pinigų, bet ne daugiau kaip 15mil. Tie kurie turi daugiau negu 15 mil, turi mokėti 10%. Ta pinigų suma keliauja i fondą ir yra išskirstoma žmonėms kurie nėra labai turtingi.\n3. Pridėta !r patchnotes komanda, kuri rodo tris naujausius patch notes.'
    await channelServer.send(seniausiNotes + antriNotes + NaujausiNotes)

  elif message.content.lower().startswith("!r help") and str(message.channel.id) == str(channelServer.id):
    await channelServer.send('```Pirmas kartas žaidžiant? Parašyk !r addme. \nNori žaisti monetų metimą? Parašyk !r coinflip "herbas/skaičius" "pinigų suma/random"(be kabučių).\nNori žaisti ruletę? Rašyk !r roulette "juoda/raudona/lyginis/nelyginis/žalia" "suma"(be kabučių)\nNori sužinoti kiek liko pinigų? Parašyk !r balance.\nNori gauti dieninį bonusą? Rašyk !r daily.\nPraradai visus pinigus? Rašyk !r praradau.\nNori pervesti kažkam pinigų? Rašyk !r send @žmogus suma.\nNori sužinoti, kokie yra 5 turtingiausi žmonės? Rašyk !r leaderboard\nNori mesti daugiau monetų vienu metu? Rašyk !r coinflip "herbas/skaičius" "pinigų suma" "monetų skaičius" (be kabučių) (monetų limitas yra 150)\nNori spėti numerį pasirinktame intervale? Rašyk !r numeris "spėjamas numeris" "statoma suma" "iki kokio skaičiaus yra intervalas (turi būti lyginis skaičius, mažesnis už 100)" (be kabučių).\nNori pirkti/parduoti DOGE kriptovaliutą? Rašyk !r doge buy/sell(minimalus pirkimo kiekis yra 500) kiekis (rekomenduojama pirkti dideliais kiekiais, nes balansas yra suapvalinamas).\nNori sužinoti kiek yra vertas DOGE? Rašyk !r kainos.\nNori išbandyti savo sėkmę lošimų automatuose? Rašyk !r slots.\nNori sužinoti lošimo bei laimėjimo sumas? Parašyk !r slots help\nNori sužinoti, kas daugiausiai laimėjo lošimo automatuose? Rašyk !r slots leaderboard\nNori sužinoti savo slot laimėjimus? Rašyk !r slots check\nNori dalyvauti savaitiniame evente? Rašyk !r event.```')

  #elif message.content.lower().startswith("!r event") and str(message.channel.id) == str(channelServer.id):
    #if db["bankas"][2] == False:
      #await channelServer.send("Savaitinis event dar neprasidėjo. Jis prasidės " + str(db["bankas"][1]) + " dieną ir truks iki sekmadienio 12h. Rašyk !r event help dėl daugiau informacijos.")
    #else:
      #await channelServer.send("Savaitinis event jau prasidėjo. Jis truks iki šio sekmadienio 12h. Rašyk !r event help dėl daugiau informacijos.")

  #elif message.content.lower().startswith("!r ticket buy") and str(message.channel.id) == str(channelServer.id):
    '''if db[searchedID][4] > 1:
      searchedMoney = int(db[searchedID][1])
      searchedDoge = int(db[searchedID][3])
      searchedDay = int(db[searchedID][2])
      searchedWins = db[searchedID][5]
      del db[searchedID]
      db[searchedID] = message.author.id, searchedMoney, searchedDay, searchedDoge, 0, searchedWins
    if db[searchedID][4] == 0 and db[searchedID][1] >= 30000 and db["bankas"][2] == True:
      searchedMoney = int(db[searchedID][1])
      searchedDoge = int(db[searchedID][3])
      searchedDay = int(db[searchedID][2])
      searchedWins = db[searchedID][5]
      del db[searchedID]
      db[searchedID] = message.author.id, searchedMoney - 30000, searchedDay, searchedDoge, 1, searchedWins
      await channelServer.send("<@%s>, nusipirkai bilietą!" % message.author.id)
    elif db["bankas"][2] == False:
      await channelServer.send("Eventas dar neprasidėjo!")
    elif db[searchedID][4] == 1:
      await channelServer.send("<@%s>, tu jau turi nusipirkęs bilietą." % message.author.id)
    elif db[searchedID][1] < 30000:
      await channelServer.send("<@%s>, tau neužtenka pinigų." % message.author.id)'''
  elif message.content.lower().startswith("!r give") and str(message.channel.id) == str(channelServer.id):
    if message.author.id == 211832708530307082:
      split_parts = message.content.split(' ')
      if len(split_parts) >= 3 and split_parts[3].isdecimal():
        split_parts[2] = split_parts[2].replace("<","")
        split_parts[2] = split_parts[2].replace(">","")
        split_parts[2] = split_parts[2].replace("!","")
        split_parts[2] = split_parts[2].replace("@","")
        searchedID = get_spot(int(split_parts[2]))
        searchedDay = int(db[searchedID][2])
        searchedDoge = int(db[searchedID][3])
        Ticket = int(db[searchedID][4])
        searchedMoney = int(db[searchedID][1])
        searchedWins = db[searchedID][5]
        del db[searchedID]
        db[searchedID] = int(split_parts[2]), searchedMoney + int(split_parts[3]), searchedDay, searchedDoge, Ticket, searchedWins
        await channelServer.send("<@%s> gavo " % message.author.id + kableliai(split_parts[2] + split_parts[3]) + " pinigų.")
    else:
      await channelServer.send("<@%s> Norėjo sugadinti ekonomiką." % message.author.id)

  #elif message.content.lower().startswith("!r tickets") and str(message.channel.id) == str(channelServer.id):
    '''zinute = ""
    ticketai = ticketboard()
    for i in range(len(ticketai)):
      user = await client.fetch_user(ticketai[i])
      zinute += str(user.name) + "\n"
    if len(ticketai) == 0:
      await channelServer.send("Niekas dar neturi nusipirkę bilietų.")
    else:
      await channelServer.send(zinute)
'''
  elif message.content.lower().startswith("!r balance") and str(message.channel.id) == str(channelServer.id):
    searchedID = get_spot(message.author.id)
    searchedMoney = int(db[searchedID][1])
    searchedDoge = int(db[searchedID][3])
    await channelServer.send("<@%s>, tu turi:\n" % message.author.id + kableliai(searchedMoney) + " pinigų.\n" + str(searchedDoge) + " DOGE.\n")

  elif message.content.lower().startswith("!r kainos"):
    DogeEur = getDogePrice()
    searchedID = get_spot(message.author.id)
    searchedDoge = int(db[searchedID][3])
    await channelServer.send("DOGE yra vertas " + str(DogeEur) + " EUR.\n<@%s>, tavo DOGE balansas yra vertas " % message.author.id + str(int(DogeEur * searchedDoge)) + " eur.\n")


  #elif message.content.startswith("!r bankas")and str(message.channel.id) == str(channelServer.id):
    #bankoPinigai = db['bankas']
    #await channelServer.send("Bankas turi %s " % str(bankoPinigai) + "pinigų.")

  elif message.content.lower().startswith("!r praradau") and str(message.channel.id) == str(channelServer.id):
    searchedID = get_spot(message.author.id)
    searchedMoney = int(db[searchedID][1])
    searchedDoge = int(db[searchedID][3])
    searchedDay = int(db[searchedID][2])
    searchedWins = db[searchedID][5]
    Ticket = int(db[searchedID][4])
    if int(db[searchedID][1]) <= 0:
      del db[searchedID]
      db[searchedID] = message.author.id, searchedMoney + 10, searchedDay, searchedDoge, Ticket, searchedWins
      await channelServer.send("<@%s>, gavai 10 pinigų." % message.author.id)
    else:
      await channelServer.send("Tau dar liko pinigų.")

  elif message.content.lower().startswith("!r leaderboard") and str(message.channel.id) == str(channelServer.id):
    if db[9871] != now.minute:
      db[9871] = now.minute
      top = leaderboard()
      zmogus1 = await client.fetch_user(top[0][1])
      zmogus2 = await client.fetch_user(top[1][1])
      zmogus3 = await client.fetch_user(top[2][1])
      zmogus4 = await client.fetch_user(top[3][1])
      zmogus5 = await client.fetch_user(top[4][1])
      await channelServer.send("1. " + str(zmogus1.name) + ": " + kableliai(int(top[0][0])) + "\n2. " + str(zmogus2.name) + ": " + kableliai(int(top[1][0])) + "\n3. " + str(zmogus3.name) + ": " + kableliai(int(top[2][0])) + "\n4. " + str(zmogus4.name) + ": " + kableliai(int(top[3][0])) + "\n5. " + str(zmogus5.name) + ": " + kableliai(int(top[4][0])))
    else:
      await channelServer.send("Jau ši komanda buvo parašyta visai neseniai. Pabandyk vėliau!")

  elif (message.content.lower().startswith("!r daily") or message.content.lower().startswith("!к вфшдн") or message.content.lower().startswith("!г суточный")) and str(message.channel.id) == str(channelServer.id):
    now = datetime.now()
    searchedID = get_spot(message.author.id)
    searchedDoge = int(db[searchedID][3])
    Ticket = int(db[searchedID][4])
    searchedWins = db[searchedID][5]
    if db[searchedID][2] != now.day and db[searchedID][2] != now.day + 1:
      searchedMoney = int(db[searchedID][1])
      num = random.randint(1, 101)
      money = 1000
      if num >= 1 and num <= 30:
          money = 1000
      elif num >= 31 and num <= 61:
          money = 2000
      elif num >= 62 and num <= 66:
          money = 1500
      elif num >= 67 and num <= 81:
          money = 3000
      elif num >= 82 and num <= 95:
          money = 4000
      elif num >= 96 and num <= 101:
          money = 30000
      del db[searchedID]
      db[searchedID] = message.author.id, searchedMoney + money, now.day, searchedDoge, Ticket, searchedWins
      await channelServer.send("<@%s> priėmė savo dieninį bonusą" % message.author.id + " (" + str(money) + " pinigų).\n" +"Visa pinigų suma: " + kableliai(searchedMoney + money))
    elif db[searchedID][2] == now.day and now.hour >= 21:
      searchedMoney = int(db[searchedID][1])
      num = random.randint(1, 101)
      money = 1000
      if num >= 1 and num <= 30:
          money = 1000
      elif num >= 31 and num <= 61:
          money = 2000
      elif num >= 62 and num <= 66:
          money = 1500
      elif num >= 67 and num <= 81:
          money = 3000
      elif num >= 82 and num <= 95:
          money = 4000
      elif num >= 96 and num <= 101:
          money = 30000
      del db[searchedID]
      db[searchedID] = message.author.id, searchedMoney + money, now.day + 1, searchedDoge, Ticket, searchedWins
      await channelServer.send("<@%s> priėmė savo dieninį bonusą" % message.author.id + " (" + str(money) + " pinigų).\n" +"Visa pinigų suma: " + str(searchedMoney + money))
    else:
      await channelServer.send("<@%s>, tavo dieninis bonusas jau buvo aktyvuotas.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif" % message.author.id)
       
  elif message.content.lower().startswith("!r send") and str(message.channel.id) == str(channelServer.id):
    split_parts = message.content.split(' ')
    if len(split_parts) >= 3 and split_parts[3].isdecimal():
      split_parts[2] = split_parts[2].replace("<","")
      split_parts[2] = split_parts[2].replace(">","")
      split_parts[2] = split_parts[2].replace("!","")
      split_parts[2] = split_parts[2].replace("@","")
      searchedAuthorID = get_spot(message.author.id)
      searchedAuthorMoney = int(db[searchedAuthorID][1])
      searchedAuthorDay = int(db[searchedAuthorID][2])
      searchedAuthorDoge = int(db[searchedAuthorID][3])
      searchedAuthorSafe = int(db[searchedAuthorID][4])
      searchedAuthorWins = db[searchedAuthorID][5]
      if db[searchedAuthorID][1] >= int(split_parts[3]) and int(split_parts[3]) > 0:
        searchedID = get_spot(int(split_parts[2]))
        searchedDay = int(db[searchedID][2])
        searchedDoge = int(db[searchedID][3])
        Ticket = int(db[searchedID][4])
        searchedWins = db[searchedID][5]
        if int(message.author.id) == int(split_parts[2]):
          await channelServer.send("Negalima siųsti pinigų sau.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")
        else:
          searchedMoney = int(db[searchedID][1])
          del db[searchedID]
          db[searchedID] = int(split_parts[2]), searchedMoney + int(split_parts[3]), searchedDay, searchedDoge, Ticket, searchedWins
          del db[searchedAuthorID]
          db[searchedAuthorID] = message.author.id, searchedAuthorMoney - int(split_parts[3]), searchedAuthorDay, searchedAuthorDoge, searchedAuthorSafe, searchedAuthorWins
          await channelServer.send("<@%s> išsiuntė" % message.author.id + " " + kableliai(split_parts[3]) + " pinigų į <@%s> sąskaitą." % str(split_parts[2]))
      else:
        await channelServer.send("<@%s>, arba tau neužtenka pinigų, arba skaičius nėra teigiamas.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif" % message.author.id)
    else:
      await channelServer.send("Padėtas nereikalingas tarpas arba neteisingai panaudota komanda.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")
  elif message.content.lower().startswith("!r slots help"):
    await channelServer.send("Sukimo kaina: 5000 pinigų.\n<:diamond1:860229741861011466> -- --: 7500 pinigų.\n<:diamond1:860229741861011466> <:diamond1:860229741861011466> --: 25000 pinigų.\n<:diamond1:860229741861011466> <:diamond1:860229741861011466> <:diamond1:860229741861011466>: 1250000 pinigų.\n:cherries: :cherries:  :cherries: : 62500 pinigų.\n:grapes:  :grapes:  :grapes: : 125000 pinigų.\n:watermelon: :watermelon: :watermelon:: 175000 pinigų.\n:bell: :bell: :bell:: 250000 pinigų.\n<:7nr:860229154363539466> <:7nr:860229154363539466> <:7nr:860229154363539466>: 650000 pinigų.\n")

  #elif message.content.lower().startswith("!r balsuoti help") and str(message.channel.id) == str(channelServer.id):
    #await channelServer.send("```Balsavimas padės nuspręsti ar verta visiškai anuliuoti šį botą ir pradėti viską nuo pradžių.\nJeigu bus balsuota už, tada visų pinigai dings ir visi pradės su 10000 pinigų iš naujo (Tie kurie prieš resetą turėjo virš 1 mil, gaus papildomai 50k). Daily išliks tokie kokie dabar yra, bus naujas ir geresnis eventas. \nJeigu bus balsuota prieš, eventas bus išjungtas ilgesniam laikui, tačiau visų pinigai išliks.\nNorint balsuoti už šį sprendimą, reikia rašyti !r balsuoti už.\nNorint balsuoti prieš šį sprendimą, reikia rašyti !r balsuoti prieš.\nNorint panaikinti savo sprendimą, reikia rašyti !r balsuoti panaikinti.\nNorint patikrinti kiek balsų yra iš viso, reikia rašyti !r balsai.\nBalsavimas truks iki rugsėjo 10 dienos. Resetas bus įvykdytas rugsėjo 13 dieną. Slots leaderboardas išliks.Slotų kainos sumažės\nBalsavimas su alt accountais yra griežtai draudžiamas.\nJeigu lygiosios, bus 50/50 roll.```")
  
  #elif (message.content.lower().startswith("!r balsuoti uz") or message.content.lower().startswith("!r balsuoti už")) and str(message.channel.id) == str(channelServer.id):
    '''listasuz = db[9998]
    listaspries = db[9999]
    isTrue = False
    for i in listasuz:
      if message.author.id == i:
        await channelServer.send("<@%s>, tu jau esi prabalsavęs." % message.author.id)
        isTrue = True
    for i in listaspries:
      if message.author.id == i:
        await channelServer.send("<@%s>, tu jau esi prabalsavęs." % message.author.id)
        isTrue = True
    if isTrue == False:
      listasuz.append(message.author.id)
      await channelServer.send("<@%s>, sėkmingai prabalsavo!" % message.author.id)
      del db[9998]
      db[9998] = listasuz
    print(listasuz)
    isTrue = False'''

  #elif (message.content.lower().startswith("!r balsuoti pries") or message.content.lower().startswith("!r balsuoti prieš")) and str(message.channel.id) == str(channelServer.id):
    '''listasuz = db[9998]
    listaspries = db[9999]
    isTrue = False
    for i in listasuz:
      if message.author.id == i:
        await channelServer.send("<@%s>, tu jau esi prabalsavęs." % message.author.id)
        isTrue = True
    for i in listaspries:
      if message.author.id == i:
        await channelServer.send("<@%s>, tu jau esi prabalsavęs." % message.author.id)
        isTrue = True
    if isTrue == False:
      listaspries.append(message.author.id)
      await channelServer.send("<@%s>, sėkmingai prabalsavo!" % message.author.id)
      del db[9999]
      db[9999] = listaspries
    print(listaspries)
    isTrue = False'''

  #elif message.content.lower().startswith("!r balsuoti panaikinti") and str(message.channel.id) == str(channelServer.id):
    '''listasuz = db[9998]
    listaspries = db[9999]
    isTrue = False
    for i in listasuz:
      if message.author.id == i:
        isTrue = True
        listasuz.remove(message.author.id)
        del db[9998]
        db[9998] = listasuz
    for i in listaspries:
      if message.author.id == i:
        isTrue = True
        listaspries.remove(message.author.id)
        del db[9999]
        db[9999] = listaspries
    if isTrue == True:
      await channelServer.send("<@%s>, balsas sėkmingai panaikintas!" % message.author.id)
    else:
      await channelServer.send("<@%s>, tu nesi prabalsavęs." % message.author.id)
    isTrue = False'''
  
  #elif message.content.lower().startswith("!r balsai") and str(message.channel.id) == str(channelServer.id):
    #await channelServer.send("Balsai už: " + str(len(db[9998])) + "\nBalsai prieš: " + str(len(db[9999])))

  elif message.content.lower().startswith("!r slots check") and str(message.channel.id) == str(channelServer.id):
    trump = ["CHERRIES", "GRAPE", "WATERMELON", "BELL", "SEVEN", "DIAMOND"]
    searchedID = get_spot(message.author.id)
    await channelServer.send(":cherries: : " + str(db[searchedID][5]["CHERRIES"]) + "\n:grapes: : " + str(db[searchedID][5]["GRAPE"]) + "\n:watermelon: : " + str(db[searchedID][5]["WATERMELON"]) + "\n:bell: : " + str(db[searchedID][5]["BELL"]) + "\n<:7nr:860229154363539466> : " + str(db[searchedID][5]["SEVEN"]) + "\n<:diamond1:860229741861011466>  : " + str(db[searchedID][5]["DIAMOND"]))

  elif message.content.lower().startswith("!r slots leaderboard") and str(message.channel.id) == str(channelServer.id):
    trump = ["CHERRIES", "GRAPE", "WATERMELON", "BELL", "SEVEN", "DIAMOND"]
    if db[9871] != now.minute:
      db[9871] = now.minute
      top, ids = slotsboard()
      zinute = ":cherries: : "
      if len(str(ids[trump[0]])) == 18:
        zmogus1 = await client.fetch_user(ids[trump[0]])
        zinute = zinute + str(zmogus1.name) + " (" + str(top[trump[0]]) + ")\n"
      else:
        zinute = zinute + " Nėra laimėtojų\n"
      zinute = zinute + ":grapes: : "
      if len(str(ids[trump[1]])) == 18:
        zmogus2 = await client.fetch_user(ids[trump[1]])
        zinute = zinute + str(zmogus2.name) + " (" + str(top[trump[1]]) + ")\n"
      else:
        zinute = zinute + " Nėra laimėtojų\n"
      zinute = zinute + ":watermelon: : "
      if len(str(ids[trump[2]])) == 18:
        zmogus3 = await client.fetch_user(ids[trump[2]])
        zinute = zinute + str(zmogus3.name) + " (" + str(top[trump[2]]) + ")\n"
      else:
        zinute = zinute + " Nėra laimėtojų\n"
      zinute = zinute + ":bell: : "
      if len(str(ids[trump[3]])) == 18:
        zmogus4 = await client.fetch_user(ids[trump[3]])
        zinute = zinute + str(zmogus4.name) + " (" + str(top[trump[3]]) + ")\n"
      else:
        zinute = zinute + " Nėra laimėtojų\n"
      zinute = zinute + "<:7nr:860229154363539466> : "
      if len(str(ids[trump[4]])) == 18:
        zmogus5 = await client.fetch_user(ids[trump[4]])
        zinute = zinute + str(zmogus5.name) + " (" + str(top[trump[4]]) + ")\n"
      else:
        zinute = zinute + " Nėra laimėtojų\n"
      zinute = zinute + "<:diamond1:860229741861011466> : "
      if len(str(ids[trump[5]])) == 18:
        zmogus6 = await client.fetch_user(ids[trump[5]])
        zinute = zinute + str(zmogus6.name) + " (" + str(top[trump[5]]) + ")\n"
      else:
        zinute = zinute + " Nėra laimėtojų\n"
      await channelServer.send(zinute)
    else:
      await channelServer.send("Jau ši komanda buvo parašyta visai neseniai. Pabandyk vėliau!")

  elif message.content.lower().startswith("!r slots") and str(message.channel.id) == str(channelServer.id):
    resultss = game()
    results = list(resultss)
    searchedWins = db[searchedID][5]
    searchedMoney = int(db[searchedID][1])
    if results[0] > 25000 and searchedMoney >= 5000:
        searchedWins[results[1]] += 1
    for i in range(3):
      if results[i + 1] == "CHERRIES":
        results[i + 1] = ":cherries:"
      elif results[i + 1] == "GRAPE":
        results[i + 1] = ":grapes:"
      elif results[i + 1] == "WATERMELON":
        results[i + 1] = ":watermelon:"
      elif results[i + 1] == "BELL":
        results[i + 1] = ":bell:"
      elif results[i + 1] == "SEVEN":
        results[i + 1] = "<:7nr:860229154363539466>"
      elif results[i + 1] == "DIAMOND":
        results[i + 1] = "<:diamond1:860229741861011466>"
    searchedID = get_spot(message.author.id)
    searchedDoge = int(db[searchedID][3])
    Ticket = int(db[searchedID][4])
    searchedDay = int(db[searchedID][2])
    if searchedMoney < 5000:
      await channelServer.send("<@%s>, tau neužtenka pinigų.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif" % message.author.id)
    else:
      newMoney = searchedMoney - 5000
      newMoney += results[0]
      if results[0] == 0 and db["bankas"][2] == True:
        pridetBankui(5000)
        pinigai = int(db["bankas"][0])
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(pinigai) + " pinigų prize pool"))
      del db[searchedID]
      db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins
      if results[0] > 0:
        await channelServer.send(results[1] + "|" + results[2] + "|" + results[3] + "\n<@%s> laimėjo " % message.author.id + str(results[0]) + " pinigų!\nIš viso turi " + kableliai(newMoney) + " pinigų.")
      else:
        await channelServer.send(results[1] + "|" + results[2] + "|" + results[3] + "\n<@%s> pralaimėjo." % message.author.id + "\nIš viso turi " + kableliai(newMoney) + " pinigų.")
    

  elif message.content.lower().startswith("!r") or message.content.lower().startswith("ąr"):
    if str(message.channel.id) == str(channelServer.id):
      split_parts = message.content.split(' ')
      if checkForCoinflip(message, split_parts):
        searchedID = get_spot(message.author.id)
        if searchedID == None:
          await channelServer.send("<@%s>, žaidi pirmą kartą? Parašyk !r addme." % message.author.id)
        else:
          searchedMoney = int(db[searchedID][1])
          searchedDoge = int(db[searchedID][3])
          Ticket = int(db[searchedID][4])
          searchedWins = db[searchedID][5]
          zinute = ""
          if split_parts[3] == "random":
            split_parts[3] = random.randint(1, searchedMoney)
            zinute = "Padėjo " + kableliai(str(split_parts[3])) + " pinigų.\n"
          if int(split_parts[3]) <= searchedMoney and int(split_parts[3]) > 0:
            if searchedID != None:
              searchedDay = int(db[searchedID][2])
              if coinflip(split_parts[2], split_parts[3]) == True:
                newMoney = searchedMoney + int(split_parts[3])
                del db[searchedID]
                db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins
                #paimtIsBanko(int(split_parts[3]))
                await channelServer.send("<@%s> " % message.author.id + zinute + "Laimėjo! \nIš viso turi pinigų: " + kableliai(newMoney))
              else:
                newMoney = searchedMoney - int(split_parts[3])
                del db[searchedID]
                db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins
                if db["bankas"][2] == True:
                  pridetBankui(int(split_parts[3]))
                  pinigai = int(db["bankas"][0])
                  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(pinigai) + " pinigų prize pool"))
                await channelServer.send("<@%s> " % message.author.id + zinute + "Pralaimėjo. \nIš viso turi pinigų: " + kableliai(newMoney))
          else:
            await channelServer.send("Arba pinigų suma viršija jūsų balansą, arba įvestas neigiamas skaičius.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")
      elif checkForMultipleCoinflips(message, split_parts):
        searchedID = get_spot(message.author.id)
        if searchedID == None:
          await channelServer.send("<@%s>, žaidi pirmą kartą? Parašyk !r addme." % message.author.id)
        else:
          searchedMoney = int(db[searchedID][1])
          searchedDoge = int(db[searchedID][3])
          Ticket = int(db[searchedID][4])
          searchedWins = db[searchedID][5]
          if int(split_parts[3]) * int(split_parts[4]) <= searchedMoney and int(split_parts[3]) > 0 and int(split_parts[4]) > 1 and int(split_parts[4]) <= 150:
            if searchedID != None:
              searchedDay = int(db[searchedID][2])
              flip = multipleCoinflips(split_parts[2], int(split_parts[3]), int(split_parts[4]))
              newMoney = searchedMoney + flip[1]
              del db[searchedID]
              db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins
              if flip[1] > 0:
                #paimtIsBanko(flip[1])
                await channelServer.send("<@%s> Laimėjo! \n" % message.author.id + "Moneta buvo mesta " + str(split_parts[4]) + " kartų(us).\n" + split_parts[2] + " iškrito " + str(flip[0]) + " kartų(us).\nDabar turi pinigų: " + kableliai(newMoney))
              elif flip[1] < 0:
                if db["bankas"][2] == True:
                  pridetBankui(flip[1] * -1)
                  pinigai = int(db["bankas"][0])
                  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(pinigai) + " pinigų prize pool"))
                await channelServer.send("<@%s> Pralaimėjo. \n" % message.author.id + "Moneta buvo mesta " + str(split_parts[4]) + " kartų(us).\n" + split_parts[2] + " iškrito " + str(flip[0]) + " kartų(us).\nDabar turi pinigų: " + kableliai(newMoney))
              else:
                await channelServer.send("<@%s> Lygiosios. \n" % message.author.id + "Moneta buvo mesta " + str(split_parts[4]) + " kartų(us).\n" + split_parts[2] + " iškrito " + str(flip[0]) + " kartų(us).\nDabar turi pinigų: " + kableliai(newMoney))
          else:
            await channelServer.send("Arba pinigų suma viršija jūsų balansą, arba įvestas neigiamas skaičius.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")
      elif checkForRoulette(message, split_parts):
        searchedID = get_spot(message.author.id)
        if searchedID == None:
          await channelServer.send("<@%s>, žaidi pirmą kartą? Parašyk !r addme." % message.author.id)   
        else:
          searchedMoney = int(db[searchedID][1])
          searchedDoge = int(db[searchedID][3])
          Ticket = int(db[searchedID][4])
          searchedWins = db[searchedID][5]
          if int(split_parts[3]) <= searchedMoney and int(split_parts[3]) > 0:
            if searchedID != None:
              searchedDay = int(db[searchedID][2])
              if roulette(split_parts[2], split_parts[3]) == True:
                if split_parts[2].lower() == "zalia" or split_parts[2].lower() == "žalia":
                  newMoney = searchedMoney + (int(split_parts[3]) * 15)
                else:
                  newMoney = searchedMoney + int(split_parts[3])
                del db[searchedID]
                db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins
                #paimtIsBanko(int(split_parts[3]))
                await channelServer.send("<@%s> Laimėjo! \nIš viso turi pinigų: " % message.author.id + kableliai(newMoney))
              else:
                newMoney = searchedMoney - int(split_parts[3])
                del db[searchedID]
                db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins
                if db["bankas"][2] == True:
                  pridetBankui(int(split_parts[3]))
                  pinigai = int(db["bankas"][0])
                  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(pinigai) + " pinigų prize pool"))
                await channelServer.send("<@%s> Pralaimėjo. \nIš viso turi pinigų: " % message.author.id + kableliai(newMoney))
          else:
            await channelServer.send("Arba pinigų suma viršija jūsų balansą, arba įvestas neigiamas skaičius.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")
      elif checkForNumber(message, split_parts):
        searchedID = get_spot(message.author.id)
        if searchedID == None:
          await channelServer.send("<@%s>, žaidi pirmą kartą? Parašyk !r addme." % message.author.id)   
        else:
          searchedMoney = int(db[searchedID][1])
          if int(split_parts[3]) <= searchedMoney and int(split_parts[3]) > 0 and int(split_parts[2]) <= int(split_parts[4]) and int(split_parts[2]) > 0 and int(split_parts[4]) > 0 and int(split_parts[4]) < 100:
            if searchedID != None:
              searchedDay = int(db[searchedID][2])
              searchedDoge = int(db[searchedID][3])
              Ticket = int(db[searchedID][4])
              searchedWins = db[searchedID][5]
              prize = numberGuesser(int(split_parts[2]), int(split_parts[3]), int(split_parts[4]))
              newMoney = searchedMoney + prize[0]
              if prize[0] > 0:
                del db[searchedID]
                db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins
                #paimtIsBanko(prize[0])
                await channelServer.send("<@%s> Laimėjo!\nIš viso turi pinigų: " % message.author.id + kableliai(newMoney))
              else:
                del db[searchedID]
                db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins
                if db["bankas"][2] == True:
                  pridetBankui(prize[0] * -1)
                  pinigai = int(db["bankas"][0])
                  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(pinigai) + " pinigų prize pool"))
                await channelServer.send("<@%s> Pralaimėjo.\nSkaičius buvo: " % message.author.id + str(prize[1]) + ".\nIš viso turi pinigų: " + kableliai(newMoney))
      elif checkForDoge(message, split_parts):
        searchedID = get_spot(message.author.id)
        searchedDoge = int(db[searchedID][3])
        Ticket = int(db[searchedID][4])
        searchedWins = db[searchedID][5]
        if searchedID == None:
          await channelServer.send("<@%s>, žaidi pirmą kartą? Parašyk !r addme." % message.author.id)   
        else:
          searchedMoney = int(db[searchedID][1])
          print(searchedDoge)
          DogeEur = getDogePrice()
          if split_parts[2] == 'buy':
            if int(split_parts[3]) * DogeEur <= searchedMoney and int(split_parts[3]) > 0 and int(split_parts[3]) >= 500:
              if searchedID != None:
                searchedDay = int(db[searchedID][2])
                newMoney = searchedMoney - (int(split_parts[3]) * DogeEur)
                del db[searchedID]
                db[searchedID] = message.author.id, int(newMoney), searchedDay, searchedDoge + int(split_parts[3]), Ticket, searchedWins
                await channelServer.send("<@%s> Nusipirko " % message.author.id + str(split_parts[3]) + " DOGE!\nIš viso turi " + str(searchedDoge + int(split_parts[3])) + " DOGE.")
          elif split_parts[2] == 'sell' and searchedDoge > 0:
            if int(split_parts[3]) <= searchedDoge and int(split_parts[3]) > 0:
              if searchedID != None:
                searchedDay = int(db[searchedID][2])
                newMoney = searchedMoney + int((int(split_parts[3]) * DogeEur))
                del db[searchedID]
                db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge - int(split_parts[3]), Ticket, searchedWins
                await channelServer.send("<@%s> Pardavė " % message.author.id + str(split_parts[3]) + " DOGE!\nIš viso turi " + str(searchedDoge - int(split_parts[3])) + " DOGE.")
            else:
              await channelServer.send("Pinigų suma viršija jūsų balansą.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")
      else:
        await channelServer.send("Nesupratau komandos. Parašykite !r help, kad sužinoti visas komandas.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")

keep_alive()
client.run(os.getenv('TOKEN??'))
cryptocompare.cryptocompare._set_api_key_parameter(os.getenv('TOKEN2'))