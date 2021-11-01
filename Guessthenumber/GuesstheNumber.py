from logo import logo
import random
import time

EASY = 10
HARD = 5


def chooseLevel ():

  difficulty = input("Please choose your desired level of difficulty (EASY / HARD)").lower()
  if difficulty == 'easy':
    return EASY
  elif difficulty == 'hard':
    return HARD
  else:
      print("Invalid input. Please Try again.")
      return 0


def loadingFunc(myFunc):
  def wrapper(*args, **kwargs):
    value = myFunc(*args, **kwargs)
    for _ in range (5):
      time.sleep(1)
      print(".",end="")
    time.sleep(1)
    print (".")
    return value
  return wrapper


@loadingFunc
def generateRandomNumber(a,b):
  print(f"Generating a random number between {a} and {b}", end="")
  return random.randint(1,100)


def checkAnswer (guess, answer, tries):
  print (f"You guessed {guess}.")
  time.sleep(1)
  if guess == answer:
    print (f"The mystery number is {answer}.")
    time.sleep(1)
    print (f"Congratulations, you won in {tries} tries!")
    return True
  elif guess > answer:
    print("The number is too large.")
    time.sleep(1)
    return False
  elif guess < answer:
    print ("The number is too small.")
    time.sleep(2)
    return False

def playGame():
  print(logo)
  print("Welcome to Guess the Number.")

  level = 0
  while level == 0:
    level = chooseLevel()

  answer = generateRandomNumber(1,100)
  print(f"Hint, the answer is {answer}")

  for i in range(1, level+1):
    guess = ""

    while guess == "":
      try:
        guess = int(input("Please enter your guess between 1 and 100, inclusive: "))
      except:
        print("Please enter only numbers. ")
    
    if checkAnswer(guess, answer, i):
      return
    elif i == level:
      print("You ran out of number of tries. You loose.")
      return
    else:
        print (f"You have {level - i} tries left.")

  
new_game = "y"

while new_game =="y":

  playGame()

  new_game = input("Would you like to try again? (Y/N)").lower()

print("Thank you for playing. We hope to see you soon!")
