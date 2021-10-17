alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#import re
#import replit
import art

try_again = "yes"

def caesar(plain_text, shift_amount, shift_direction):
  cipher_text = ""

  for letter in plain_text:

    if letter in alphabet:
      position = alphabet.index(letter)

      if shift_direction == "encode":
        new_position = (position + shift_amount) % 26

      elif shift_direction == "decode":
        new_position = position - shift_amount
        while new_position < 0:
          new_position += 26
      else:
        print("Error, please try again.")
        break
      
      cipher_text += alphabet[new_position]
    else:
      cipher_text += letter

  print(f"The {shift_direction}d text is {cipher_text}")

print(art.logo)

while try_again == "yes":

  direction =""
  text ="*"
  shift=""

  while direction != 'encode' and direction !='decode':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction !='decode':
      print("Please enter the correct action.")

  text = input("Type your message:\n").lower()

  while not (type(shift) is int):
    try:
      shift = int(input("Type the shift number:\n"))
    except:
      print("Please enter a number.")
      continue

  caesar(text, shift, direction)

  try_again = input("Would you like to try again? (yes / no)")
  #replit.clear()

print("Logging off...")
