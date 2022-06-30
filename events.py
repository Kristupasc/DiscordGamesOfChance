
import bankHelper, otherHelpers
from replit import db
import random
import csv
import discord


SALYS = ['Norvegija', 'Švedija', 'Suomija', 'Danija', 'Estija', 'Latvija', 'Lietuva', 'Lenkija', 'Vokietija', 'Nyderlandai', 'Belgija', 'Liuksemburgas', 'Prancūzija', 'Ispanija', 'Portugalija', 'Italija', 'Čekija', 'Austrija', 'Slovakija', 'Vengrija', 'Slovėnija', 'Šveicarija', 'Kroatija', 'Graikija', 'Rumunija', 'Bulgarija', 'Kipras', 'Malta', 'Juodkalnija', 'Airija', 'Islandija']

async def eventStart(now, client, discord):
  bankHelper.pradetiBanka()
  otherHelpers.resetintPlayeriuTickets()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="0 pinigų prize pool"))
  pinigai = int(db["bankas"][0])
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(pinigai) + " pinigų prize pool"))

async def eventEnd(now, client, discord, channelServer):
  notificationServer = client.get_channel(983041377241821235)
  await channelServer.send("Eventas baigėsi! Laimėtojai:")
  await notificationServer.send("Eventas baigėsi! Laimėtojai:")
  ticketai = otherHelpers.ticketboard()
  if len(ticketai) >= 3:
    ranum = random.randint(0, len(ticketai) - 1)
    user = await  client.fetch_user(ticketai[ranum])
    suma = db["bankas"][0]
    sempro = int((suma * 60) / 100)
    await channelServer.send(str(user) + " 60% visos sumos! (" + str(sempro) + ")")
    await notificationServer.send(str(user) + " 60% visos sumos! (" + str(sempro) + ")")
    searchedID = otherHelpers.get_spot(ticketai[ranum])
    searchedMoney = int(db[searchedID][1])
    searchedDoge = int(db[searchedID][3])
    searchedDay = int(db[searchedID][2])
    searchedWins = db[searchedID][5]
    salys = db[searchedID][6]
    del db[searchedID]
    db[searchedID] = ticketai[ranum], searchedMoney + sempro, searchedDay, searchedDoge, 0, searchedWins, salys
    while True:
      ranum2 = random.randint(0, len(ticketai) - 1)
      if ranum != ranum2:
        break
    user = await client.fetch_user(ticketai[ranum2])
    trimpro = int((suma * 30) / 100)
    await channelServer.send(str(user) + " 30% visos sumos! (" + str(trimpro) + ")")
    await notificationServer.send(str(user) + " 30% visos sumos! (" + str(trimpro) + ")")
    searchedID = otherHelpers.get_spot(ticketai[ranum2])
    searchedMoney = int(db[searchedID][1])
    searchedDoge = int(db[searchedID][3])
    searchedDay = int(db[searchedID][2])
    searchedWins = db[searchedID][5]
    salys = db[searchedID][6]
    del db[searchedID]
    db[searchedID] = ticketai[ranum2], searchedMoney + trimpro, searchedDay, searchedDoge, 0, searchedWins, salys
    while True:
      ranum3 = random.randint(0, len(ticketai) - 1)
      if ranum != ranum3 and ranum2 != ranum3:
        break
    user = await client.fetch_user(ticketai[ranum3])
    despro = int((suma * 10) / 100)
    await channelServer.send(str(user) + " 10% visos sumos! (" + str(despro) + ")")
    await notificationServer.send(str(user) + " 10% visos sumos! (" + str(despro) + ")")
    searchedID = otherHelpers.get_spot(ticketai[ranum3])
    searchedMoney = int(db[searchedID][1])
    searchedDoge = int(db[searchedID][3])
    searchedDay = int(db[searchedID][2])
    searchedWins = db[searchedID][5]
    salys = db[searchedID][6]
    del db[searchedID]
    db[searchedID] = ticketai[ranum3], searchedMoney + despro, searchedDay, searchedDoge, 0, searchedWins, salys
  elif len(ticketai) == 2:
    ranum = random.randint(0, len(ticketai) - 1)
    user = await client.fetch_user(ticketai[ranum])
    suma = db["bankas"][0]
    sempro = int((suma * 60) / 100)
    await channelServer.send(str(user) + " 60% visos sumos! (" + str(sempro) + ")")
    await notificationServer.send(str(user) + " 60% visos sumos! (" + str(sempro) + ")")
    searchedID = otherHelpers.get_spot(ticketai[ranum])
    searchedMoney = int(db[searchedID][1])
    searchedDoge = int(db[searchedID][3])
    searchedDay = int(db[searchedID][2])
    searchedWins = db[searchedID][5]
    salys = db[searchedID][6]
    del db[searchedID]
    db[searchedID] = ticketai[ranum], searchedMoney + sempro, searchedDay, searchedDoge, 0, searchedWins, salys
    while True:
      ranum2 = random.randint(0, len(ticketai) - 1)
      if ranum != ranum2:
        break
    user = await client.fetch_user(ticketai[ranum2])
    trimpro = int((suma * 30) / 100)
    await channelServer.send(str(user) + " 30% visos sumos! (" + str(trimpro) + ")")
    await notificationServer.send(str(user) + " 30% visos sumos! (" + str(trimpro) + ")")
    searchedID = otherHelpers.get_spot(ticketai[ranum2])
    searchedMoney = int(db[searchedID][1])
    searchedDoge = int(db[searchedID][3])
    searchedDay = int(db[searchedID][2])
    searchedWins = db[searchedID][5]
    salys = db[searchedID][6]
    del db[searchedID]
    db[searchedID] = ticketai[ranum2], searchedMoney + trimpro, searchedDay, searchedDoge, 0, searchedWins, salys
  elif len(ticketai) == 1:
    user = await client.fetch_user(ticketai[0])
    suma = db["bankas"][0]
    sempro = int((suma * 60) / 100)
    await channelServer.send(str(user) + " 60% visos sumos! (" + str(sempro) + ")")
    await notificationServer.send(str(user) + " 60% visos sumos! (" + str(sempro) + ")")
    searchedID = otherHelpers.get_spot(ticketai[0])
    searchedMoney = int(db[searchedID][1])
    searchedDoge = int(db[searchedID][3])
    searchedDay = int(db[searchedID][2])
    searchedWins = db[searchedID][5]
    salys = db[searchedID][6]
    del db[searchedID]
    db[searchedID] = ticketai[0], searchedMoney + sempro, searchedDay, searchedDoge, 0, searchedWins, salys
  bankHelper.pabaigtBanka()

async def event(channelServer):
  if db["bankas"][2] == False:
      await channelServer.send("Savaitinis event dar neprasidėjo. Jis prasidės " + str(db["bankas"][1]) + " dieną ir truks iki sekmadienio 12h. Rašyk !r event help dėl daugiau informacijos.")
  else:
    await channelServer.send("Savaitinis event jau prasidėjo. Jis truks iki šio sekmadienio 12h. Rašyk !r event help dėl daugiau informacijos.")

async def eventPool(channelServer):
  if db["bankas"][2] == True:
    await channelServer.send("Prize poole yra " + str(int(db["bankas"][0])) + " pinigų. Pinigai, patenkantys į prize poola yra nustatomi pagal šią funkciją:\n``f(x)= -0.0025x^2 -0.2x +60``\nx = (statoma suma / 10000). Ši funkcija veikia tik tada, kai pralaimėtų pinigų suma yra tarp 10,000 ir 1,000,000 pinigų. Jeigu pinigų suma yra mažesnė negu 10,000, tada yra taikoma 70% taisyklė. Jeigu pinigų suma didesnė už 1 milijoną, taikoma 25% taisyklė. Šie procentai gali keistis savaites eigoje dėl galimos sistemos balansavimo.")
  else:
    await channelServer.send("Eventas dar neprasidėjo.")

async def ticketBuy(channelServer, message):
  searchedID = otherHelpers.get_spot(message.author.id)
  searchedMoney = int(db[searchedID][1])
  searchedDoge = int(db[searchedID][3])
  searchedDay = int(db[searchedID][2])
  searchedWins = db[searchedID][5]
  try:
    salys = db[searchedID][6]
  except:
    salys = SALYS
  if db[searchedID][4] > 1:
      del db[searchedID]
      db[searchedID] = message.author.id, searchedMoney, searchedDay, searchedDoge, 0, searchedWins, salys
  if db[searchedID][4] == 0 and db[searchedID][1] >= 50000 and db["bankas"][2] == True:
    del db[searchedID]
    db[searchedID] = message.author.id, searchedMoney - 50000, searchedDay, searchedDoge, 1, searchedWins, salys
    await channelServer.send("<@%s>, nusipirkai bilietą!" % message.author.id)
  elif db["bankas"][2] == False:
    await channelServer.send("Eventas dar neprasidėjo!")
  elif db[searchedID][4] == 1:
    await channelServer.send("<@%s>, tu jau turi nusipirkęs bilietą." % message.author.id)
  elif db[searchedID][1] < 50000:
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

# not working with python :(
async def puzzleStart(client):
  channelServer = client.get_channel(971787066839027763)
  lastPuzzle = db["puzzle"][2]
  print("last puzzle id was: " + str(lastPuzzle))
  with open('goc_puzzles.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
          if lastPuzzle == int(row[0])-1:
            print("Today's puzzle image is: " + row[1] + ".png")
            await channelServer.send("<redacted>")
            #await channelServer.send("A new puzzle has been started!\nReact to the correct answer by the end of the day to win `10000 money`!\n``Participants with multiple reactions automatically get disqualified.``")
            message = await channelServer.send(file=discord.File('puzzles/' + row[1] + '.png'))
            # await message.add_reaction('🇦')
            # await message.add_reaction('🇧')
            # await message.add_reaction('🇨')
            # await message.add_reaction('🇩')
            del db['puzzle']
            db['puzzle'] = True, int(row[2]), int(row[0]), []
            # view = discord_ui.View()
            # item = discord.ui.Button(style=discord.ButtonStyle.blurple, label="🇦")
            # view.add_item(item=item)
            # item = discord.ui.Button(style=discord.ButtonStyle.blurple, label="🇧")
            # view.add_item(item=item)
            # item = discord.ui.Button(style=discord.ButtonStyle.blurple, label="🇨")
            # view.add_item(item=item)
            # item = discord.ui.Button(style=discord.ButtonStyle.blurple, label="🇩")
            # view.add_item(item=item)
            # await channelServer.send("", view=view)
            break
          line_count += 1

async def puzzleEnd(client):
  channelServer = client.get_channel(971787066839027763)
  message = ''
  if db['puzzle'][1] == 0:
    message = "The answer was: 🇦!"
  if db['puzzle'][1] == 1:
    message = "The answer was: 🇧!"
  if db['puzzle'][1] == 2:
    message = "The answer was: 🇨!"
  if db['puzzle'][1] == 3:
    message = "The answer was: 🇩!"
  message += "\nThe winners are:\n"
  # now we need to find the winners