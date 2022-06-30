import gamesHelper, otherHelpers, bankHelper
import discord, random
from replit import db

async def slots(message, channelServer, client):
  multiplier = 1
  split_content = message.content.split(' ')
  if len(split_content) >= 3 and split_content[2].lower().startswith("high"):
    multiplier = 10
  searchedID = otherHelpers.get_spot(message.author.id)
  resultss = gamesHelper.game()
  results = list(resultss)
  searchedWins = db[searchedID][5]
  searchedMoney = int(db[searchedID][1])
  if results[0] > 2500 * multiplier and searchedMoney >= 500 * multiplier:
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
  searchedID = otherHelpers.get_spot(message.author.id)
  searchedDoge = int(db[searchedID][3])
  Ticket = int(db[searchedID][4])
  searchedDay = int(db[searchedID][2])
  if searchedMoney < 500 * multiplier:
    await channelServer.send("<@%s>, tau neužtenka pinigų.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif" % message.author.id)
  else:
    newMoney = searchedMoney - (500 * multiplier)
    newMoney += results[0] * multiplier
    if results[0] == 0 and db["bankas"][2] == True:
      bankHelper.pridetBankui(500 * multiplier, False, message)
      pinigai = int(db["bankas"][0])
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(otherHelpers.kableliai(pinigai)) + " pinigų prize pool"))
    searchedSalys = db[searchedID][6]
    del db[searchedID]
    db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
    if results[0] > 0:
      await channelServer.send(results[1] + "|" + results[2] + "|" + results[3] + "\n<@%s> laimėjo " % message.author.id + str(results[0] * multiplier) + " pinigų!\nIš viso turi " + otherHelpers.kableliai(newMoney) + " pinigų.")
    else:
      await channelServer.send(results[1] + "|" + results[2] + "|" + results[3] + "\n<@%s> pralaimėjo." % message.author.id + "\nIš viso turi " + otherHelpers.kableliai(newMoney) + " pinigų.")

async def coinflip(message, channelServer, split_parts, client):
  searchedID = otherHelpers.get_spot(message.author.id)
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
      zinute = "Padėjo " + otherHelpers.kableliai(str(split_parts[3])) + " pinigų.\n"
    if int(split_parts[3]) <= searchedMoney and int(split_parts[3]) > 0:
      if searchedID != None:
        searchedDay = int(db[searchedID][2])
        if gamesHelper.coinflip(split_parts[2], split_parts[3]) == True:
          newMoney = searchedMoney + int(split_parts[3])
          searchedSalys = db[searchedID][6]
          del db[searchedID]
          db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
          #paimtIsBanko(int(split_parts[3]))
          await channelServer.send("<@%s> " % message.author.id + zinute + "Laimėjo! \nIš viso turi pinigų: " + otherHelpers.kableliai(newMoney))
        else:
          newMoney = searchedMoney - int(split_parts[3])
          searchedSalys = db[searchedID][6]
          del db[searchedID]
          db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
          if db["bankas"][2] == True:
            bankHelper.pridetBankui(int(split_parts[3]), True, message)
            pinigai = int(db["bankas"][0])
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(otherHelpers.kableliai(pinigai)) + " pinigų prize pool"))
          await channelServer.send("<@%s> " % message.author.id + zinute + "Pralaimėjo. \nIš viso turi pinigų: " + otherHelpers.kableliai(newMoney))
    else:
      await channelServer.send("Arba pinigų suma viršija jūsų balansą, arba įvestas neigiamas skaičius.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")

async def multipleCoinflips(message, channelServer, client, split_parts):
  searchedID = otherHelpers.get_spot(message.author.id)
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
        flip = gamesHelper.multipleCoinflips(split_parts[2], int(split_parts[3]), int(split_parts[4]))
        newMoney = searchedMoney + flip[1]
        searchedSalys = db[searchedID][6]
        del db[searchedID]
        db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
        if flip[1] > 0:
          #paimtIsBanko(flip[1])
          await channelServer.send("<@%s> Laimėjo! \n" % message.author.id + "Moneta buvo mesta " + str(split_parts[4]) + " kartų(us).\n" + split_parts[2] + " iškrito " + str(flip[0]) + " kartų(us).\nDabar turi pinigų: " + otherHelpers.kableliai(newMoney))
        elif flip[1] < 0:
          if db["bankas"][2] == True:
            bankHelper.pridetBankui(flip[1] * -1, False, message)
            pinigai = int(db["bankas"][0])
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(otherHelpers.kableliai(pinigai)) + " pinigų prize pool"))
          await channelServer.send("<@%s> Pralaimėjo. \n" % message.author.id + "Moneta buvo mesta " + str(split_parts[4]) + " kartų(us).\n" + split_parts[2] + " iškrito " + str(flip[0]) + " kartų(us).\nDabar turi pinigų: " + otherHelpers.kableliai(newMoney))
        else:
          await channelServer.send("<@%s> Lygiosios. \n" % message.author.id + "Moneta buvo mesta " + str(split_parts[4]) + " kartų(us).\n" + split_parts[2] + " iškrito " + str(flip[0]) + " kartų(us).\nDabar turi pinigų: " + otherHelpers.kableliai(newMoney))
    else:
      await channelServer.send("Arba pinigų suma viršija jūsų balansą, arba įvestas neigiamas skaičius.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")

async def roulette(channelServer, client, message, split_parts):
  searchedID = otherHelpers.get_spot(message.author.id)
  if searchedID == None:
    await channelServer.send("<@%s>, žaidi pirmą kartą? Parašyk !r addme." % message.author.id)   
  else:
    searchedMoney = int(db[searchedID][1])
    searchedDoge = int(db[searchedID][3])
    Ticket = int(db[searchedID][4])
    searchedWins = db[searchedID][5]
    searchedSalys = db[searchedID][6]
    if int(split_parts[3]) <= searchedMoney and int(split_parts[3]) > 0:
      if searchedID != None:
        searchedDay = int(db[searchedID][2])
        if gamesHelper.roulette(split_parts[2], split_parts[3]) == True:
          if split_parts[2].lower() == "zalia" or split_parts[2].lower() == "žalia":
            newMoney = searchedMoney + (int(split_parts[3]) * 15)
          else:
            newMoney = searchedMoney + int(split_parts[3])
          del db[searchedID]
          db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
          #paimtIsBanko(int(split_parts[3]))
          await channelServer.send("<@%s> Laimėjo! \nIš viso turi pinigų: " % message.author.id + otherHelpers.kableliai(newMoney))
        else:
          newMoney = searchedMoney - int(split_parts[3])
          searchedSalys = db[searchedID][6]
          del db[searchedID]
          db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
          if db["bankas"][2] == True:
            bankHelper.pridetBankui(int(split_parts[3]), True, message)
            pinigai = int(db["bankas"][0])
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(otherHelpers.kableliai(pinigai)) + " pinigų prize pool"))
          await channelServer.send("<@%s> Pralaimėjo. \nIš viso turi pinigų: " % message.author.id + otherHelpers.kableliai(newMoney))
    else:
      await channelServer.send("Arba pinigų suma viršija jūsų balansą, arba įvestas neigiamas skaičius.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")

async def number(channelServer, client, message, split_parts):
  searchedID = otherHelpers.get_spot(message.author.id)
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
        prize = gamesHelper.numberGuesser(int(split_parts[2]), int(split_parts[3]), int(split_parts[4]))
        newMoney = searchedMoney + prize[0]
        searchedSalys = db[searchedID][6]
        if prize[0] > 0:
          del db[searchedID]
          db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
          #paimtIsBanko(prize[0])
          await channelServer.send("<@%s> Laimėjo!\nIš viso turi pinigų: " % message.author.id + otherHelpers.kableliai(newMoney))
        else:
          del db[searchedID]
          db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
          if db["bankas"][2] == True:
            if int(split_parts[4]) >= 16:
              bankHelper.pridetBankui(prize[0] * -1, False, message)
              pinigai = int(db["bankas"][0])
              await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(otherHelpers.kableliai(pinigai)) + " pinigų prize pool"))
            else:
              bankHelper.pridetBankui(prize[0] * -1, True, message)
              pinigai = int(db["bankas"][0])
              await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(otherHelpers.kableliai(pinigai)) + " pinigų prize pool"))
          await channelServer.send("<@%s> Pralaimėjo.\nSkaičius buvo: " % message.author.id + str(prize[1]) + ".\nIš viso turi pinigų: " + otherHelpers.kableliai(newMoney))

async def doge(message, split_parts, channelServer, client):
  searchedID = otherHelpers.get_spot(message.author.id)
  searchedDoge = int(db[searchedID][3])
  Ticket = int(db[searchedID][4])
  searchedWins = db[searchedID][5]
  if searchedID == None:
    await channelServer.send("<@%s>, žaidi pirmą kartą? Parašyk !r addme." % message.author.id)   
  else:
    searchedMoney = int(db[searchedID][1])
    searchedSalys = db[searchedID][6]
    print(searchedDoge)
    DogeEur = otherHelpers.getDogePrice()
    if split_parts[2] == 'buy':
      if int(split_parts[3]) * DogeEur <= searchedMoney and int(split_parts[3]) > 0 and int(split_parts[3]) >= 500:
        if searchedID != None:
          searchedDay = int(db[searchedID][2])
          newMoney = searchedMoney - (int(split_parts[3]) * DogeEur)
          del db[searchedID]
          db[searchedID] = message.author.id, int(newMoney), searchedDay, searchedDoge + int(split_parts[3]), Ticket, searchedWins, searchedSalys
          await channelServer.send("<@%s> Nusipirko " % message.author.id + str(split_parts[3]) + " DOGE!\nIš viso turi " + str(searchedDoge + int(split_parts[3])) + " DOGE.")
    elif split_parts[2] == 'sell' and searchedDoge > 0:
      if int(split_parts[3]) <= searchedDoge and int(split_parts[3]) > 0:
        if searchedID != None:
          searchedSalys = db[searchedID][6]
          searchedDay = int(db[searchedID][2])
          newMoney = searchedMoney + int((int(split_parts[3]) * DogeEur))
          del db[searchedID]
          db[searchedID] = message.author.id, newMoney, searchedDay, searchedDoge - int(split_parts[3]), Ticket, searchedWins, searchedSalys
          await channelServer.send("<@%s> Pardavė " % message.author.id + str(split_parts[3]) + " DOGE!\nIš viso turi " + str(searchedDoge - int(split_parts[3])) + " DOGE.")
      else:
        await channelServer.send("Pinigų suma viršija jūsų balansą.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")