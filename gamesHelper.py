import random
import checksHelper

SLOTS = ["DIAMOND", "CHERRIES", "GRAPE", "WATERMELON", "BELL", "SEVEN"]

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
    money = checksHelper.check(slot1, slot2, slot3)
    return money, slot1, slot2, slot3

def roulette(guess, bet):
  red =  {1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,38,40}
  black = {2,4,6,8,10,11,15,17,19,20,22,24,26,28,29,31,33,35,37,39}
  green = {0, 36}
  even = {2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,38,40} #as nzn ar cia exploitas
  odd = {1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39}
  roll = random.randint(0, 40)
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
