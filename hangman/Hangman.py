alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import re

try_again = "yes"

def caesar(plain_text, shift_amount, shift_direction):
  cipher_text = ""

  for letter in plain_text:
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

  print(f"The {shift_direction}d text is {cipher_text}")


while try_again == "yes":

  direction =""
  text ="*"
  shift=""

  while direction != 'encode' and direction !='decode':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction !='decode':
      print("Please enter the correct action.")

  while re.search("[^A-Za-z]",text):
    text = input("Type your message:\n").lower()
    if re.search("[^A-Za-z]",text):
      print("Please only enter alphabets.")

  while not (type(shift) is int):
    try:
      shift = int(input("Type the shift number:\n"))
    except:
      print("Please enter a number.")
      continue

  caesar(text, shift, direction)

  try_again = input("Would you like to try again? (yes / no)")
