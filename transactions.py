import otherHelpers
from replit import db

async def give(message, channelServer):
  if message.author.id == 211832708530307082:
    split_parts = message.content.split(' ')
    if len(split_parts) >= 3 and split_parts[3].isdecimal():
      split_parts[2] = split_parts[2].replace("<","")
      split_parts[2] = split_parts[2].replace(">","")
      split_parts[2] = split_parts[2].replace("!","")
      split_parts[2] = split_parts[2].replace("@","")
      searchedID = otherHelpers.get_spot(int(split_parts[2]))
      searchedDay = int(db[searchedID][2])
      searchedDoge = int(db[searchedID][3])
      Ticket = int(db[searchedID][4])
      searchedMoney = int(db[searchedID][1])
      searchedWins = db[searchedID][5]
      searchedSalys = db[searchedID][6]
      del db[searchedID]
      db[searchedID] = int(split_parts[2]), searchedMoney + int(split_parts[3]), searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
      await channelServer.send("<@%s> gavo " % int(split_parts[2]) + otherHelpers.kableliai(split_parts[3]) + " pinigų.")
  else:
    await channelServer.send("<@%s> Norėjo sugadinti ekonomiką." % message.author.id)

async def send(message, channelServer):
  split_parts = message.content.split(' ')
  if len(split_parts) >= 3 and split_parts[3].isdecimal():
    split_parts[2] = split_parts[2].replace("<","")
    split_parts[2] = split_parts[2].replace(">","")
    split_parts[2] = split_parts[2].replace("!","")
    split_parts[2] = split_parts[2].replace("@","")
    searchedAuthorID = otherHelpers.get_spot(message.author.id)
    searchedAuthorMoney = int(db[searchedAuthorID][1])
    searchedAuthorDay = int(db[searchedAuthorID][2])
    searchedAuthorDoge = int(db[searchedAuthorID][3])
    AuthorTicket = int(db[searchedAuthorID][4])
    searchedAuthorWins = db[searchedAuthorID][5]
    searchedAuthorSalys = db[searchedAuthorID][6]
    if db[searchedAuthorID][1] >= int(split_parts[3]) and int(split_parts[3]) > 0:
      searchedID = otherHelpers.get_spot(int(split_parts[2]))
      searchedDay = int(db[searchedID][2])
      searchedDoge = int(db[searchedID][3])
      Ticket = int(db[searchedID][4])
      searchedWins = db[searchedID][5]
      if int(message.author.id) == int(split_parts[2]):
        await channelServer.send("Negalima siųsti pinigų sau.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")
      else:
        searchedMoney = int(db[searchedID][1])
        searchedSalys = db[searchedID][6]
        del db[searchedID]
        db[searchedID] = int(split_parts[2]), searchedMoney + int(split_parts[3]), searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
        del db[searchedAuthorID]
        db[searchedAuthorID] = message.author.id, searchedAuthorMoney - int(split_parts[3]), searchedAuthorDay, searchedAuthorDoge, AuthorTicket, searchedAuthorWins, searchedAuthorSalys
       #print(db[searchedAuthorID])
        await channelServer.send("<@%s> išsiuntė" % message.author.id + " " + otherHelpers.kableliai(split_parts[3]) + " pinigų į <@%s> sąskaitą." % str(split_parts[2]))
    else:
      await channelServer.send("<@%s>, arba tau neužtenka pinigų, arba skaičius nėra teigiamas.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif" % message.author.id)
  else:
    await channelServer.send("Padėtas nereikalingas tarpas arba neteisingai panaudota komanda.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")