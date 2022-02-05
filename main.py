import discord, os, cryptocompare, requests
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

client = discord.Client()
DOGE = cryptocompare.get_price('DOGE', currency='EUR', full=False) # rad
DogeEur = DOGE["DOGE"]["EUR"]
db[9871] = -1
searchedID = None
searchedMoney = 0
newMoney = 0
now = datetime.now()
print("Current day: " + str(now.day))


@client.event
async def on_ready():
  print("Bot is logged in as {0.user}".format(client))
  
  #db[0] = 211832708530307082, 309000, 8, 0, 0, {'CHERRIES': 79, 'SEVEN': 17, 'DIAMOND': 0, 'GRAPE': 75, 'WATERMELON': 14, 'BELL': 15}, {'Norvegija': 0, 'Švedija': 0, 'Suomija': 0, 'Danija': 0, 'Estija': 0, 'Latvija': 0, 'Lietuva': 0, 'Lenkija': 100000, 'Vokietija': 0, 'Nyderlandai': 0, 'Belgija': 0, 'Liuksemburgas': 250000, 'Prancūzija': 0, 'Ispanija': 0, 'Portugalija': 0, 'Italija': 0, 'Čekija': 100000, 'Austrija': 0, 'Slovakija': 0, 'Vengrija': 0, 'Slovėnija': 0, 'Šveicarija': 0, 'Kroatija': 0, 'Graikija': 0, 'Rumunija': 0, 'Bulgarija': 0, 'Kipras': 0, 'Malta': 0, 'Juodkalnija': 0, 'Airija': 0, 'Islandija': 0}
  #otherHelpers.printOutAllDatabase()
  #otherHelpers.updatintDatabase()

@client.event
async def on_message(message):
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

  #if now.weekday() == 0 and db["bankas"][2] == False:
    #await events.eventStart(now, client, discord)

  #if now.weekday() == 6 and db["bankas"][2] == True and message.author.id == 699945002406510692:
    #await events.eventEnd(now, client, discord, channelServer)
  
  if client.user.mentioned_in(message) and str(message.channel.id) == str(channelServer.id):
    await message.reply("Kas yra")

  elif message.content.lower().startswith("!r slots help") and str(message.channel.id) == str(channelServer.id):
    await others.slotsHelp(channelServer)

  elif message.content.lower().startswith("!r slots check") and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.slotsCheck(message, channelServer)

  elif message.content.lower().startswith("!r slots leaderboard") and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.slotsLeaderboard(message, channelServer, now, client)

  elif message.content.lower().startswith("!r slots") and str(message.channel.id) == str(channelServer.id):
    await gambling.slots(message, channelServer, client)
    
  elif message.content.lower().startswith("!r addme") and str(message.channel.id) == str(channelServer.id):
    if otherHelpers.addme(message) == False:
      await channelServer.send("<@%s> jau yra pridėtas. " % message.author.id)
    else:
      await channelServer.send("<@%s> pridėtas. " % message.author.id + " Pradiniai pinigai: 400")

  elif message.content.lower().startswith("!r taisykles") and str(message.channel.id) == str(channelServer.id):
    await message.delete()

  elif message.content.lower().startswith("liaudies priesas") and str(message.channel.id) == str(channelServer.id):
    await message.delete()

  elif message.content.lower().startswith("!r lmao") and str(message.channel.id) == str(channelServer.id):
    await channelServer.send("lmao")

  elif message.content.lower().startswith("agrastas") and str(message.channel.id) == str(channelServer.id):
    await channelServer.send("norėtum")

  elif message.content.lower().startswith("!r patchnotes") and str(message.channel.id) == str(channelServer.id):
    await others.patchNotes(channelServer, client)

  elif message.content.lower().startswith("!r help") and str(message.channel.id) == str(channelServer.id):
    await others.help(channelServer)

  elif (message.content.lower().startswith("!r šalys help") or message.content.lower().startswith("!r salys help"))and str(message.channel.id) == str(channelServer.id):
    await events.salysHelp(channelServer)

  elif (message.content.lower().startswith("!r mano šalys") or message.content.lower().startswith("!r mano salys"))and str(message.channel.id) == str(channelServer.id):
    if (now.weekday() == 0 or now.weekday() == 2 or now.weekday() == 5) and db['dailySalys'] != []:
      await events.salysPatikrintiStatymus(message, channelServer)
    else:
      await channelServer.send("Šiandien ant šalių statyti negalima. Statymai veikia tik pirmadieniais, trečiadieniais ir šeštadieniais.")

  elif (message.content.lower().startswith("!r šalys statyti") or message.content.lower().startswith("!r salys statyti"))and str(message.channel.id) == str(channelServer.id):
    if (now.weekday() == 0 or now.weekday() == 2 or now.weekday() == 5) and db['dailySalys'] != []:
      await events.salysStatyt(message, channelServer)
    else:
      await channelServer.send("Šiandien ant šalių statyti negalima. Statymai veikia tik pirmadieniais, trečiadieniais ir šeštadieniais.")

  elif (message.content.lower().startswith("!r šalys") or message.content.lower().startswith("!r salys"))and str(message.channel.id) == str(channelServer.id):
    if (now.weekday() == 0 or now.weekday() == 2 or now.weekday() == 5) and db['dailySalys'] != []:
      await events.paroSalis(channelServer)
    else:
      await channelServer.send("Šiandien ant šalių statyti negalima. Statymai veikia tik pirmadieniais, trečiadieniais ir šeštadieniais.")

  #elif message.content.lower().startswith("!r event") and str(message.channel.id) == str(channelServer.id):
    #await events.event(channelServer)

  #elif message.content.lower().startswith("!r ticket buy") and str(message.channel.id) == str(channelServer.id):
    #await events.ticketBuy(channelServer, message)
    
  elif message.content.lower().startswith("!r give") and str(message.channel.id) == str(channelServer.id):
    await transactions.give(message, channelServer)

  #elif message.content.lower().startswith("!r tickets") and str(message.channel.id) == str(channelServer.id):
    #await events.tickets(client, channelServer)

  elif message.content.lower().startswith("!r balance") and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.balance(message, channelServer)

  elif message.content.lower().startswith("!r kainos"):
    await playersEconomy.kainos(channelServer, message)

  elif message.content.lower().startswith("!r praradau") and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.praradau(channelServer, message)

  elif message.content.lower().startswith("!r leaderboard") and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.leaderboard(channelServer, client, now)

  elif (message.content.lower().startswith("!r daily") or message.content.lower().startswith("!к вфшдн") or message.content.lower().startswith("!г суточный")) and str(message.channel.id) == str(channelServer.id):
    await playersEconomy.daily(message, channelServer)
       
  elif message.content.lower().startswith("!r send") and str(message.channel.id) == str(channelServer.id):
    await transactions.send(message, channelServer)

  elif message.content.lower().startswith("!r") or message.content.lower().startswith("ąr"):
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
        await channelServer.send("Nesupratau komandos. Parašykite !r help, kad sužinoti visas komandas.\nhttps://media.giphy.com/media/f9qYBByA7FXePMu2Km/giphy.gif")

keep_alive()
client.run(os.getenv('TOKEN??'))
cryptocompare.cryptocompare._set_api_key_parameter(os.getenv('TOKEN2'))