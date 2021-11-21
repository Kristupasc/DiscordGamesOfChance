import otherHelpers
from replit import db

async def taxes(channelServer, client, now, message):
  zinute = "Laikas surinkti rytinius mokesčius!\nMokesčiai buvo surinkti iš:\n"
  turtingi = otherHelpers.turtingumoInspekcija()
  vargsai = otherHelpers.bomzuInspekcija()
  mokestis = 0
  if len(turtingi) > 0 and len(vargsai) > 0:
    for i in range(len(turtingi)): # atimam 
      searchedID = otherHelpers.get_spot(turtingi[i])
      searchedMoney = int(db[searchedID][1])
      Ticket = int(db[searchedID][4])
      searchedDay = int(db[searchedID][2])
      searchedDoge = int(db[searchedID][3])
      searchedWins = db[searchedID][5]
      searchedSalys = db[searchedID][6]
      newMoney = 0
      if searchedMoney < 15000000:
        mokestis += (searchedMoney * 5) / 100
        newMoney = searchedMoney - mokestis
      else:
        mokestis += (searchedMoney * 10) / 100
        newMoney = searchedMoney - mokestis
      del db[searchedID]
      db[searchedID] = turtingi[i], int(newMoney), searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
      user = await client.fetch_user(turtingi[i])
      zinute += user.name + "\n"
    zinute += "Surinkti pinigai yra atiduodami šiem žmonėm:\n"
    for i in range(len(vargsai)): # atiduodam
      searchedID = otherHelpers.get_spot(vargsai[i])
      searchedMoney = int(db[searchedID][1])
      searchedSalys = db[searchedID][6]
      Ticket = int(db[searchedID][4])
      searchedDay = int(db[searchedID][2])
      searchedDoge = int(db[searchedID][3])
      searchedWins = db[searchedID][5]
      newMoney = int(searchedMoney + (mokestis / len(vargsai)))
      del db[searchedID]
      db[searchedID] = vargsai[i], int(newMoney), searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
      user = await client.fetch_user(vargsai[i])
      zinute += user.name + "\n"
    await channelServer.send(zinute)
        