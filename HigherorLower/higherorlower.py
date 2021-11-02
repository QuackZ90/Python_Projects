import random
import art
from game_data import data
from replit import clear

new_game = "y"

def formatPrint(dic):
  return (f"Compare A: {dic['name']}, a {dic['description']} from {dic['country']}.") #with {dic['follower_count']} followers.")

def compare(a, b):
  """Takes in 2 dictionaries (a and b) with name, description, country and follower_count, request for player to choose the dictionary with the higher follower count. Return True if player makes the right guess, else return false."""

  print(f"Compare A: {formatPrint(a)}")

  print(art.vs)

  print(f"Against B: {formatPrint(b)}")

  answer = input("A or B, which one has more follower?").lower()

  if a["follower_count"] > b["follower_count"]:
    if answer == "a":
      return True
    else:
      return False
  else:
    if answer =="b":
      return True
    else:
      return False


def playGame():

  choice = data.copy()
  streak = 0

  choiceA = data.pop(random.randint(0,len(choice)-1))
  choiceB = data.pop(random.randint(0,len(choice)-1))

  print(art.logo)

  while compare(choiceA, choiceB):
    streak += 1
    clear()
    print(art.logo)
    if len(choice) == 0:
      print(f"Congratulations! You won the game with {streak} points. There are no more questions left at the moment. Do check back again for new updates")
    else:
      print(f"You are right! Current Score:{streak}")
    choiceA = choiceB
    choiceB = data.pop(random.randint(0,len(choice)-1))
  
  clear()
  print(art.logo)
  print(f"Opps, you picked the wrong choice. {choiceA['name']} has {choiceA['follower_count']} followers while {choiceB['name']} has {choiceB['follower_count']} followers. You score {streak} points.")


while new_game == 'y':
  
  playGame()

  new_game = input("Do you want to try again (Y/N)?").lower()
