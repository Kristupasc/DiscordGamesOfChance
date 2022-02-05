
import bankHelper, otherHelpers
from replit import db
import random

SALYS = ['Norvegija', 'Švedija', 'Suomija', 'Danija', 'Estija', 'Latvija', 'Lietuva', 'Lenkija', 'Vokietija', 'Nyderlandai', 'Belgija', 'Liuksemburgas', 'Prancūzija', 'Ispanija', 'Portugalija', 'Italija', 'Čekija', 'Austrija', 'Slovakija', 'Vengrija', 'Slovėnija', 'Šveicarija', 'Kroatija', 'Graikija', 'Rumunija', 'Bulgarija', 'Kipras', 'Malta', 'Juodkalnija', 'Airija', 'Islandija']

'''
async def eventStart(now, client, discord):
  bankHelper.pradetiBanka()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="0 pinigų prize pool"))
  pinigai = int(db["bankas"][0])
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(pinigai) + " pinigų prize pool"))

async def eventEnd(now, client, discord, channelServer):
  await channelServer.send("Eventas baigėsi! Laimėtojai:")
  ticketai = otherHelpers.ticketboard()
  if len(ticketai) >= 3:
    ranum = random.randint(0, len(ticketai) - 1)
    user = await  client.fetch_user(ticketai[ranum])
    suma = db["bankas"][0]
    sempro = int((suma * 60) / 100)
    await channelServer.send(str(user) + " 60% visos sumos! (" + str(sempro) + ")")
    searchedID = otherHelpers.get_spot(ticketai[ranum])
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
    searchedID = otherHelpers.get_spot(ticketai[ranum2])
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
    searchedID = otherHelpers.get_spot(ticketai[ranum3])
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
    searchedID = otherHelpers.get_spot(ticketai[ranum])
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
    searchedID = otherHelpers.get_spot(ticketai[ranum2])
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
    searchedID = otherHelpers.get_spot(ticketai[0])
    searchedMoney = int(db[searchedID][1])
    searchedDoge = int(db[searchedID][3])
    searchedDay = int(db[searchedID][2])
    searchedWins = db[searchedID][5]
    del db[searchedID]
    db[searchedID] = ticketai[0], searchedMoney + sempro, searchedDay, searchedDoge, 0, searchedWins
  bankHelper.pabaigtBanka()

async def event(channelServer):
  if db["bankas"][2] == False:
      await channelServer.send("Savaitinis event dar neprasidėjo. Jis prasidės " + str(db["bankas"][1]) + " dieną ir truks iki sekmadienio 12h. Rašyk !r event help dėl daugiau informacijos.")
  else:
    await channelServer.send("Savaitinis event jau prasidėjo. Jis truks iki šio sekmadienio 12h. Rašyk !r event help dėl daugiau informacijos.")

async def ticketBuy(channelServer, message):
  searchedID = otherHelpers.get_spot(message.author.id)
  searchedMoney = int(db[searchedID][1])
  searchedDoge = int(db[searchedID][3])
  searchedDay = int(db[searchedID][2])
  searchedWins = db[searchedID][5]
  if db[searchedID][4] > 1:
      del db[searchedID]
      db[searchedID] = message.author.id, searchedMoney, searchedDay, searchedDoge, 0, searchedWins
  if db[searchedID][4] == 0 and db[searchedID][1] >= 30000 and db["bankas"][2] == True:
    del db[searchedID]
    db[searchedID] = message.author.id, searchedMoney - 30000, searchedDay, searchedDoge, 1, searchedWins
    await channelServer.send("<@%s>, nusipirkai bilietą!" % message.author.id)
  elif db["bankas"][2] == False:
    await channelServer.send("Eventas dar neprasidėjo!")
  elif db[searchedID][4] == 1:
    await channelServer.send("<@%s>, tu jau turi nusipirkęs bilietą." % message.author.id)
  elif db[searchedID][1] < 30000:
    await channelServer.send("<@%s>, tau neužtenka pinigų." % message.author.id)

async def tickets(client, channelServer):
  zinute = ""
  ticketai = otherHelpers.ticketboard()
  for i in range(len(ticketai)):
    user = await client.fetch_user(ticketai[i])
    zinute += str(user.name) + "\n"
  if len(ticketai) == 0:
    await channelServer.send("Niekas dar neturi nusipirkę bilietų.")
  else:
    await channelServer.send(zinute)

'''
async def salysPradet(channelServer):
  otherHelpers.resetintPlayeriuSalis()
  saliuSarasas = []
  zinute = "Šios dienos šalys yra išrinktos:\n"
  for i in range(6):
    num = random.randint(0, len(SALYS)-1)
    while SALYS[num] in saliuSarasas:
      num = random.randint(0, len(SALYS)-1)
    saliuSarasas.append(SALYS[num])
    zinute += SALYS[num]
    zinute += '\n'
  db['dailySalys'] = saliuSarasas
  zinute += "Nuo dabar yra galima statyti pinigus ant šių šalių. ``Rašyk !r salys help`` norint sužinoti visas komandas."
  await channelServer.send(zinute)

async def salysStatyt(message, channelServer):
  split_parts = message.content.split(' ')
  if split_parts[3] in db['dailySalys']:
    i = otherHelpers.get_spot(message.author.id)
    id = db[i][0]
    money = db[i][1]
    if split_parts[4].isdecimal() and money >= int(split_parts[4]) and int(split_parts[4]) > 0:
      day = db[i][2]
      doge = db[i][3]
      ticket = db[i][4]
      wins = db[i][5]
      salys = db[i][6]
      for j in salys:
        if salys[j] != 0 and j != split_parts[3]:
          await channelServer.send("<@%s>, tu jau esi pastatęs ant šalies." % message.author.id)
          return
      salys[split_parts[3]] += int(split_parts[4])
      del db[i]
      db[i] = id, money - int(split_parts[4]), day, doge, ticket, wins, salys
      await channelServer.send("<@%s> pastatė " % message.author.id + str(split_parts[4]) + " pinigų ant šalies: '" + str(split_parts[3]) + "'")
    else:
      await channelServer.send("Statoma suma turi būti teigiamas skaičius.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")
  else:
    await channelServer.send("Šalis nėra sąraše.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")

async def salysPatikrintiStatymus(message, channelServer):
  zinute = ''
  i = otherHelpers.get_spot(message.author.id)
  salys = db[i][6]
  for i in salys:
    if salys[i] != 0:
      zinute += str(i) + ": " + str(salys[i]) + " pinigų.\n"
  if zinute == '':
    await channelServer.send("<@%s>, šiandien nesi pastatęs ant jokių šalių."% message.author.id)
  else:
    await channelServer.send("<@%s>, štai tavo šalis, ant kurios esi pastatęs: \n"% message.author.id + zinute)

async def paroSalis(channelServer):
  zinute = "šios savaitės šalys: \n"
  for i in range(6):
    zinute += db['dailySalys'][i]
    zinute += '\n'
  await channelServer.send(zinute)

async def salysBaigt(client, channelServer):
  zinute = ""
  winner = random.randint(0, 5)
  saliesPav = db['dailySalys'][winner]
  await channelServer.send("Laikas išrinkti laimingą šalį!\nŠi šalis buvo: ``" + saliesPav + "``\nŠios dienos laimėtojai:")
  for i in range(len(db.keys())):
    try:
      if len(db[i]) >= 7:
        if db[i][6][saliesPav] > 0:
          user = await client.fetch_user(db[i][0])
          zinute += user.name + ": " + str(db[i][6][saliesPav]*5) + " pinigų.\n"
          id = db[i][0]
          money = db[i][1] + int(db[i][6][saliesPav]*5)
          day = db[i][2]
          doge = db[i][3]
          ticket = db[i][4]
          wins = db[i][5]
          salys = {'Norvegija': 0, 'Švedija': 0, 'Suomija': 0, 'Danija': 0, 'Estija': 0, 'Latvija': 0, 'Lietuva': 0, 'Lenkija': 0, 'Vokietija': 0, 'Nyderlandai': 0, 'Belgija': 0, 'Liuksemburgas': 0, 'Prancūzija': 0, 'Ispanija': 0, 'Portugalija': 0, 'Italija': 0, 'Čekija': 0, 'Austrija': 0, 'Slovakija': 0, 'Vengrija': 0, 'Slovėnija': 0, 'Šveicarija': 0, 'Kroatija': 0, 'Graikija': 0, 'Rumunija': 0, 'Bulgarija': 0, 'Kipras': 0, 'Malta': 0, 'Juodkalnija': 0, 'Airija': 0, 'Islandija': 0}
          del db[i]
          db[i] = id, money, day, doge, ticket, wins, salys
    except KeyError:
      continue
  db['dailySalys'] = []
  if zinute == "":
    await channelServer.send("Niekas <:pepesadhugs:888107003271061555>")
  else:
    await channelServer.send(zinute)

async def salysHelp(channelServer):
  await channelServer.send("Kiekvieną pirmadieni, trečiadienį bei šeštadienį bus galimybė statyti ant išrinktų šalių. Dienos pradžioje bus išrenkamos šešios Europos šalys ant kurių tą dieną bus galima statyti pinigus. Dienos gale bus išrenkama viena šalis iš šešių. Jeigu dalyvis buvo pastatęs pinigus ant tos šalies, jis atgaus ``pastatytą sumą * 5``\nKomandų sąrašas:\n``!r šalys`` parodys šešias tos dienos šalis.\n``!r mano šalys`` parodys ant kokių šalių esi pastatęs šiandien.\n``!r šalys statyti [šalies_pavadinimas] [suma]`` pastatys paskirtą sumą ant tos šalies.")
