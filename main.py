import discord, os, cryptocompare, requests, random
from replit import db
from keep_alive import keep_alive
from datetime import datetime
import checksHelper, otherHelpers #helper functions
import taxes, others, transactions, playersEconomy, gambling, events #main bot functions

r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")
global skaiciusSt
skaiciusSt = 0
servers = [846826501865603092, 515932305689411594]
intents = discord.Intents.default()
#intents.message_content = True
client = discord.Client(intents=intents)
#client = discord.Bot(intents=intents)
DOGE = cryptocompare.get_price('DOGE', currency='EUR', full=False) # rad
DogeEur = DOGE["DOGE"]["EUR"]
db[9871] = -1
searchedID = None
searchedMoney = 0
newMoney = 0
now = datetime.now()
print("Current day: " + str(now.day))
# a database for the puzzle. Structure:
# isRunning: boolean, answer: int, lastPuzzle: int, correctAnswers (ids of accounts who answered correctly): Array
db['puzzle'] = False, 0, -1, []

@client.event
async def on_ready():
  skaiciusSt = 0
  #await events.puzzleStart(client)
  # searchedID = otherHelpers.get_spot(337336281782550530)
  # searchedDoge = int(db[searchedID][3])
  # Ticket = int(db[searchedID][4])
  # searchedDay = int(db[searchedID][2])
  # searchedSalys = db[searchedID][6]
  # searchedMoney = int(db[searchedID][1])
  # searchedWins = db[searchedID][5]
  # searchedWins["DIAMOND"] = 2
  # del db[searchedID]
  # db[searchedID] = 337336281782550530, searchedMoney, searchedDay, searchedDoge, Ticket, searchedWins, searchedSalys
  print("Bot is logged in as {0.user}".format(client))
  #otherHelpers.printOutAllDatabase()
  #otherHelpers.updatintDatabase()

@client.event
async def on_message(message):
  global skaiciusSt
  now = datetime.now()
  channelServer = client.get_channel(825306731814846465)
  if message.author == client.user:
    return
  if now.weekday() == 1 and message.author.id == 699945002406510692:
    await taxes.taxes(channelServer, client, now, message)

  if (now.weekday() == 0 or now.weekday() == 2 or now.weekday() == 5) and db['dailySalys'] == [] and message.author.id == 699945002406510692 and now.hour == 8:
    await events.salysPradet(channelServer)

  if (now.weekday() == 0 or now.weekday() == 2 or now.weekday() == 5) and db['dailySalys'] != [] and message.author.id == 699945002406510692 and now.hour == 20:
    await events.salysBaigt(client, channelServer)

  if message.author.id == 173107123490783232 and skaiciusSt == 0:
    await message.reply("pisk nx stalinas")
    skaiciusSt = 1
  
  if now.weekday() == 0 and db["bankas"][2] == False:
    await events.eventStart(now, client, discord)

  if now.weekday() == 6 and db["bankas"][2] == True and message.author.id == 699945002406510692:
    await events.eventEnd(now, client, discord, channelServer)

  if message.author.id == 211832708530307082 and message.content.lower().startswith("!r override salys pradet") and str(message.channel.id) == str(channelServer.id):
    await message.delete()
    if db['dailySalys'] == []:
      await events.salysPradet(channelServer)

  if message.author.id == 211832708530307082 and message.content.lower().startswith("!r override salys baigt") and str(message.channel.id) == str(channelServer.id):
    await message.delete()
    if db['dailySalys'] != []:
      await events.salysBaigt(client, channelServer)

    
  # if message.author.id == 699945002406510692 and db["puzzle"][0] == False:
  #   await events.puzzleStart(client)
  
  if client.user.mentioned_in(message) and str(message.channel.id) == str(channelServer.id):
    r = random.randint(0, 1)
    if r == 0:
      await message.reply("Kas yra")
    elif r == 1:
      await message.reply("Ok")

  if message.content.lower().startswith("!r slots help") and str(message.channel.id) == str(channelServer.id):
    await others.slotsHelp(channelServer)

  elif message.content.lower().startswith("!r slots check") and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.slotsCheck(message, channelServer)

  elif message.content.lower().startswith("!r duoti") and str(message.channel.id) == str(channelServer.id):
    await transactions.duoti(message, channelServer, client)

  elif message.content.lower().startswith("!r slots leaderboard") and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.slotsLeaderboard(message, channelServer, now, client)

  elif message.content.lower().startswith("!r slots") and str(message.channel.id) == str(channelServer.id):
    await gambling.slots(message, channelServer, client)
    
  elif message.content.lower().startswith("!r addme") and str(message.channel.id) == str(channelServer.id):
    if otherHelpers.addme(message) == False:
      await channelServer.send("<@%s> jau yra prid??tas. " % message.author.id)
    else:
      await channelServer.send("<@%s> prid??tas. " % message.author.id + " Pradiniai pinigai: 400")

  elif message.content.lower().startswith("!r taisykles") and str(message.channel.id) == str(channelServer.id):
    await message.delete()

  elif message.content.lower().startswith("liaudies priesas") and str(message.channel.id) == str(channelServer.id):
    await message.delete()

  elif message.content.lower().startswith("!r lmao") and str(message.channel.id) == str(channelServer.id):
    await channelServer.send("lmao")

  elif message.content.lower().startswith("agrastas") and str(message.channel.id) == str(channelServer.id):
    await channelServer.send("nor??tum")

  elif message.content.lower().startswith("!r help") and str(message.channel.id) == str(channelServer.id):
    await others.help(channelServer)

  elif (message.content.lower().startswith("!r ??alys help") or message.content.lower().startswith("!r salys help"))and str(message.channel.id) == str(channelServer.id):
    await events.salysHelp(channelServer)

  elif (message.content.lower().startswith("!r mano ??alys") or message.content.lower().startswith("!r mano salys"))and str(message.channel.id) == str(channelServer.id):
    if (now.weekday() == 0 or now.weekday() == 2 or now.weekday() == 5) and db['dailySalys'] != []:
      await events.salysPatikrintiStatymus(message, channelServer)
    else:
      await channelServer.send("??iandien ant ??ali?? statyti negalima. Statymai veikia tik pirmadieniais, tre??iadieniais ir ??e??tadieniais.")

  elif (message.content.lower().startswith("!r ??alys statyti") or message.content.lower().startswith("!r salys statyti"))and str(message.channel.id) == str(channelServer.id):
    if (now.weekday() == 0 or now.weekday() == 2 or now.weekday() == 5) and db['dailySalys'] != []:
      await events.salysStatyt(message, channelServer)
    else:
      await channelServer.send("??iandien ant ??ali?? statyti negalima. Statymai veikia tik pirmadieniais, tre??iadieniais ir ??e??tadieniais.")

  elif (message.content.lower().startswith("!r ??alys") or message.content.lower().startswith("!r salys"))and str(message.channel.id) == str(channelServer.id):
    if (now.weekday() == 0 or now.weekday() == 2 or now.weekday() == 5) and db['dailySalys'] != []:
      await events.paroSalis(channelServer)
    else:
      await channelServer.send("??iandien ant ??ali?? statyti negalima. Statymai veikia tik pirmadieniais, tre??iadieniais ir ??e??tadieniais.")

  elif message.content.lower().startswith("!r event pool") and str(message.channel.id) == str(channelServer.id):
    await events.eventPool(channelServer)
  
  elif message.content.lower().startswith("!r event help") and str(message.channel.id) == str(channelServer.id):
    await others.eventHelp(channelServer)
  
  elif message.content.lower().startswith("!r event") and str(message.channel.id) == str(channelServer.id):
    await events.event(channelServer)

  elif message.content.lower().startswith("!r ticket buy") and str(message.channel.id) == str(channelServer.id):
    await events.ticketBuy(channelServer, message)
    
  elif message.content.lower().startswith("!r give") and str(message.channel.id) == str(channelServer.id):
    await transactions.give(message, channelServer)

  elif message.content.lower().startswith("!r tickets") and str(message.channel.id) == str(channelServer.id):
    await events.tickets(client, channelServer)

  elif message.content.lower().startswith("!r balance") and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.balance(message, channelServer)

  elif message.content.lower().startswith("!r kainos"):
    await playersEconomy.kainos(channelServer, message)

  elif message.content.lower().startswith("!r praradau") and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.praradau(channelServer, message)

  elif message.content.lower().startswith("!r leaderboard") and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.leaderboard(channelServer, client, now)

  elif (message.content.lower().startswith("!r daily") or message.content.lower().startswith("!?? ??????????") or message.content.lower().startswith("!?? ????????????????")) and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.daily(message, channelServer)
       
  elif message.content.lower().startswith("!r send") and str(message.channel.id) == str(channelServer.id):
    await transactions.send(message, channelServer)

  elif message.content.lower().startswith("!r") or message.content.lower().startswith("??r"):
    if str(message.channel.id) == str(channelServer.id):
      split_parts = message.content.split(' ')
      if checksHelper.checkForCoinflip(message, split_parts):
        await gambling.coinflip(message, channelServer, split_parts, client)

      elif checksHelper.checkForMultipleCoinflips(message, split_parts):
        await gambling.multipleCoinflips(message, channelServer, client, split_parts)

      elif checksHelper.checkForRoulette(message, split_parts):
        await gambling.roulette(channelServer, client, message, split_parts)

      elif checksHelper.checkForNumber(message, split_parts):
       await gambling.number(channelServer, client, message, split_parts)

      elif checksHelper.checkForDoge(message, split_parts):
        await gambling.doge(message, split_parts, channelServer, client)

      else:
        await channelServer.send("Nesupratau komandos. Para??ykite !r help, kad su??inoti visas komandas.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")


#@client.slash_command(description="Monetos metimas")
#async def coinflip(
    #ctx: discord.ApplicationContext,
    #pasirinkimas: Option(str, choices=["herbas", "skai??ius"]),
    #suma: Option(str, "statoma suma") 
#):
  #await ctx.respond("dar neveikia lol")

keep_alive()
client.run(os.getenv('TOKEN??'))
cryptocompare.cryptocompare._set_api_key_parameter(os.getenv('TOKEN2'))