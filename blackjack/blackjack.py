import random
from art import logo
import time

class Deck():
  
  cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  suits = ["♢", "♣", "♡", "♠",  ]

  def __init__(self):
    """Initiate a new deck of 52 cards"""
    self.deck = []
    for suit in self.suits:
      for card in self.cards:
        self.deck.append(card+" "+suit)


  def __repr__(self):
    return str(self.deck)


class Hand():

  def __init__(self, currdeck):
    """Initiate a new hand by drawing 2 cards from the currdeck, then update the value of the hand"""
    self.hand=[]
    self.draw(currdeck)
    self.draw(currdeck)
    self.value=self.checkValue()
  
  def __repr__(self):
    return str(self.hand)

  def __lt__(self, other):
    return self.value < other.value

  def __eq__(self, other):
    return self.value == other.value

  def draw (self, currdeck):
    """Draw a card from currdeck to the player's hand and update the value of the hand"""
    card = currdeck.deck.pop(random.randint(0,len(currdeck.deck)-1))
    self.hand.append(card)
    self.value = self.checkValue()
    return card

  def checkValue(self):
    """Calculate and return the value of the cards in the hand.
    Number cards has the value of its number.
    Picture cards has a value of 10.
    Ace has a value of 11 if the total value is less than 21, otherwise, it has a value of 1"""
    value = 0
    numA = 0

    for card in self.hand:
      try:
        value += int(card[0:2])
      except:
        if card[0] == "K" or card[0] == "Q" or card[0]=="J":
          value += 10
        elif card[0] =="A":
          value += 11
          numA += 1
    
    for _ in range(numA):
      if value > 21:
        value -= 10


    return (value)

print(logo)
new_game = input("Welcome to the game of Black Jack. Would you like to start a new game? (Y/N)").lower()

while new_game == "y":
  current_deck = Deck()
  print("Dealer is distributing the cards", end="")
  time.sleep(1)
  for i in range(5):
    print(".", end="")
    time.sleep(1)
  print(".")
  player_hand = Hand(current_deck)
  print(f"You drew: {player_hand}. Hand's value: {player_hand.value}")
  ai_hand = Hand(current_deck)
  print(f"Computer drew: {ai_hand.hand[0]}.")

  if player_hand.value == 21:
    """Check for blackjack"""
    print(f"Computer's hand: {ai_hand}.")
    if ai_hand.value == 21:
      print("Both hand drew a blackjack. It is a draw")
      new_game=input("Would you like to play again?(Y/N)").lower()
      continue
    else:
      print("You drew a blackblack. You won!")
      new_game=input("Would you like to play again?(Y/N)").lower()
      continue

  elif ai_hand.value ==21:
    print(f"Computer's hand: {ai_hand}.")
    print("Computer drew a backjack. You lost")
    new_game=input("Would you like to play again?(Y/N)").lower()
    continue

  new_card = input("Would you like to draw another card?(Y/N)").lower()

  while new_card =="y" and player_hand.value < 21:
    """player gets to decide whether to draw a card as long as the value of card in hand is less then 21"""
    card_drawn = player_hand.draw(current_deck)
    print(f"You drew: {card_drawn}")
    print(f"Your current hand:{player_hand}. Hand's value: {player_hand.value}")

    if player_hand.value > 21:
      continue

    new_card = input("Would you like to draw another card?(Y/N)").lower()

  while (ai_hand.value < 16 or (ai_hand < player_hand and player_hand.value <= 21)):
    """computer draws a card as long as the value of card in hand is less then 16, or if the value of card in hand is less than player's when player's card is not more than 21"""
    print("Computer is deciding on it's next move", end="")
    time.sleep(1)
    for i in range(5):
      print(".", end="")
      time.sleep(1)
    print(".")
    card_drawn = ai_hand.draw(current_deck)
    print("Computer drew a card.")
  
  """Computer show hand"""
  print(f"Computer's hand:{ai_hand}. Hand's value: {ai_hand.value}")

  if player_hand.value > 21 and ai_hand.value > 21:
    print("Both player and computer go burst. It is a tie.")

  elif player_hand.value > 21:
    print(f"You ({player_hand.value}) went burst. You lost.")

  elif ai_hand.value > 21:
    print(f"Computer ({ai_hand.value}) went burst. You won!")

  elif player_hand > ai_hand:
    print (f"Your hand ({player_hand.value}) has a higher value than the computer's hand ({ai_hand.value}). You won.")

  elif player_hand < ai_hand:
    print (f"Your hand ({player_hand.value}) has a lower value than the computer's hand ({ai_hand.value}). You lose.")

  elif player_hand == ai_hand:
    print (f"Both hands have a value of {player_hand.value} , {ai_hand.value}. It is a draw.")
  
  new_game=input("Would you like to play again?(Y/N)").lower()
