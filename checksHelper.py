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
