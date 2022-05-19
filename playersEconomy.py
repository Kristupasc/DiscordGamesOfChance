import otherHelpers
from replit import db
import random
from datetime import datetime

async def balance(message, channelServer):
  searchedID = otherHelpers.get_spot(message.author.id)
  searchedMoney = int(db[searchedID][1])
  searchedDoge = int(db[searchedID][3])
  await channelServer.send("<@%s>, tu turi:\n" % message.author.id + otherHelpers.kableliai(searchedMoney) + " pinigų.\n" + str(searchedDoge) + " DOGE.\n")

async def kainos(channelServer, message):
  DogeEur = otherHelpers.getDogePrice()
  searchedID = otherHelpers.get_spot(message.author.id)
  searchedDoge = int(db[searchedID][3])
  await channelServer.send("DOGE yra vertas " + str(DogeEur) + " EUR.\n<@%s>, tavo DOGE balansas yra vertas " % message.author.id + str(int(DogeEur * searchedDoge)) + " eur.\n")

async def praradau(channelServer, message):
  searchedID = otherHelpers.get_spot(message.author.id)
  searchedMoney = int(db[searchedID][1])
  searchedDoge = int(db[searchedID][3])
  searchedDay = int(db[searchedID][2])
  searchedWins = db[searchedID][5]
  searchedSalys = db[searchedID][6]
  Ticket = int(db[searchedID][4])
  if int(db[searchedID][1]) <= 0:
    del db[searchedID]
    db[searchedID] = message.author.id, searchedMoney + 10, searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
    await channelServer.send("<@%s>, gavai 10 pinigų." % message.author.id)
  else:
    await channelServer.send("Tau dar liko pinigų.")

async def leaderboard(channelServer, client, now):
  if db[9871] != now.minute:
    db[9871] = now.minute
    top = otherHelpers.leaderboard()
    zmogus1 = await client.fetch_user(top[0][1])
    zmogus2 = await client.fetch_user(top[1][1])
    zmogus3 = await client.fetch_user(top[2][1])
    zmogus4 = await client.fetch_user(top[3][1])
    zmogus5 = await client.fetch_user(top[4][1])
    await channelServer.send("1. " + str(zmogus1.name) + ": " + otherHelpers.kableliai(int(top[0][0])) + "\n2. " + str(zmogus2.name) + ": " + otherHelpers.kableliai(int(top[1][0])) + "\n3. " + str(zmogus3.name) + ": " + otherHelpers.kableliai(int(top[2][0])) + "\n4. " + str(zmogus4.name) + ": " + otherHelpers.kableliai(int(top[3][0])) + "\n5. " + str(zmogus5.name) + ": " + otherHelpers.kableliai(int(top[4][0])))
  else:
    await channelServer.send("Jau ši komanda buvo parašyta visai neseniai. Pabandyk vėliau!")

async def daily(message, channelServer):
  now = datetime.now()
  searchedID = otherHelpers. get_spot(message.author.id)
  searchedDoge = int(db[searchedID][3])
  Ticket = int(db[searchedID][4])
  searchedWins = db[searchedID][5]
  if db[searchedID][2] != now.day and db[searchedID][2] != now.day + 1:
    searchedMoney = int(db[searchedID][1])
    num = random.randint(1, 101)
    money = 5000
    if num >= 1 and num <= 30:
        money = 5000
    elif num >= 31 and num <= 61:
        money = 5000
    elif num >= 62 and num <= 66:
        money = 1000
    elif num >= 67 and num <= 81:
        money = 8000
    elif num >= 82 and num <= 95:
        money = 10000
    elif num >= 96 and num <= 101:
        money = 50000
    searchedSalys = db[searchedID][6]
    if now.weekday() == 4:
      money = money * 10
    del db[searchedID]
    db[searchedID] = message.author.id, searchedMoney + money, now.day, searchedDoge, Ticket, searchedWins, searchedSalys
    if db["bankas"][2] == True and db[searchedID][4] != 1:
      await channelServer.send("<@%s> priėmė savo dieninį bonusą" % message.author.id + " (" + str(money) + " pinigų).\n" +"Visa pinigų suma: " + otherHelpers.kableliai(searchedMoney + money) + "\nAr jau nusipirkai evento bilietą? Rašyk !r event dėl informacijos.")
    else:
      await channelServer.send("<@%s> priėmė savo dieninį bonusą" % message.author.id + " (" + str(money) + " pinigų).\n" +"Visa pinigų suma: " + otherHelpers.kableliai(searchedMoney + money))
  elif db[searchedID][2] == now.day and now.hour >= 22:
    searchedMoney = int(db[searchedID][1])
    num = random.randint(1, 101)
    money = 5000
    if num >= 1 and num <= 30:
        money = 5000
    elif num >= 31 and num <= 61:
        money = 5000
    elif num >= 62 and num <= 66:
        money = 1000
    elif num >= 67 and num <= 81:
        money = 8000
    elif num >= 82 and num <= 95:
        money = 10000
    elif num >= 96 and num <= 101:
        money = 50000
    if now.weekday() == 3:
      money = money * 10
    searchedSalys = db[searchedID][6]
    del db[searchedID]
    db[searchedID] = message.author.id, searchedMoney + money, now.day + 1, searchedDoge, Ticket, searchedWins, searchedSalys
    if db["bankas"][2] == True and db[searchedID][4] != 1:
      await channelServer.send("<@%s> priėmė savo dieninį bonusą" % message.author.id + " (" + str(money) + " pinigų).\n" +"Visa pinigų suma: " + otherHelpers.kableliai(searchedMoney + money) + "\nAr jau nusipirkai evento bilietą? Rašyk !r event dėl informacijos.")
    else:
      await channelServer.send("<@%s> priėmė savo dieninį bonusą" % message.author.id + " (" + str(money) + " pinigų).\n" +"Visa pinigų suma: " + otherHelpers.kableliai(searchedMoney + money))
  else:
    await channelServer.send("<@%s>, tavo dieninis bonusas jau buvo aktyvuotas.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif" % message.author.id)

async def slotsCheck(message, channelServer):
  searchedID = otherHelpers.get_spot(message.author.id)
  await channelServer.send(":cherries: : " + str(db[searchedID][5]["CHERRIES"]) + "\n:grapes: : " + str(db[searchedID][5]["GRAPE"]) + "\n:watermelon: : " + str(db[searchedID][5]["WATERMELON"]) + "\n:bell: : " + str(db[searchedID][5]["BELL"]) + "\n<:7nr:860229154363539466> : " + str(db[searchedID][5]["SEVEN"]) + "\n<:diamond1:860229741861011466>  : " + str(db[searchedID][5]["DIAMOND"]))

async def slotsLeaderboard(message, channelServer, now, client):
  trump = ["CHERRIES", "GRAPE", "WATERMELON", "BELL", "SEVEN", "DIAMOND"]
  if db[9871] != now.minute:
    db[9871] = now.minute
    top, ids = otherHelpers.slotsboard()
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