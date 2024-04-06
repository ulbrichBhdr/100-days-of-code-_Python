# import random
# word_list = ["ardvark", "baboon", "camel"]

# chosen_word = []
# chosen_word = random.choice(word_list)
# print(chosen_word)


# user_guess = input("Guess a letter : ").lower()

# for char in chosen_word :
#   if user_guess == char in chosen_word :
#     print(True)
#   else :
#     print(False)
# ......................................................
# import random

# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# print(f'Pssst, the solution is {chosen_word}.')

# display = []
# word_length = len(chosen_word)

# for _ in range(word_length) :
#   display += "_"

# print(display)

# guess = input("Guess a letter: ").lower()

# for position in range(word_length) :
#   letter = chosen_word[position]
#   if letter == guess:
#     display[position] = letter
  
# print(display)
# .......................................................
# import random 

# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# word_length = len(word_list)
# display = []

# for _ in range(word_length) :
#   display += "_"

# ueser_guess = input("Guess a letter :").lower()

# for position in range(word_length) :
#     letter = chosen_word[position]
#     if letter == ueser_guess :
#        display[position] = letter

# print(display)
# ........................................................
# import random
# word_list = ["ardvark", "baboon", "camel"]

# chosen_word = []
# chosen_word = random.choice(word_list)
# print(chosen_word)


# user_guess = input("Guess a letter : ").lower()

# for char in chosen_word :
#   if user_guess == char in chosen_word :
#     print(True)
#   else :
#     print(False)
# ......................................................
# import random

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''','''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''','''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''','''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''','''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''']

# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# print(f'Pssst, the solution is {chosen_word}.')

# word_length = len(chosen_word)

# lives = 6

# display = []
# for _ in range(word_length) :
#   display += "_"

# print(display)



# while  lives > 0 :
#   guess = input("Guess a letter: ").lower()
  
#   for position in range(word_length) :
#     letter = chosen_word[position]
#     if letter == guess:
#       display[position] = letter
    
#   print(display)

#   if guess not in letter :
#     lives -= 1
#     print(stages[lives])
#     if lives == 0 :
#       print("You Lose!")
    
#     if "_" not in display :
      
#       print("You win.")
# .................................................................
import random 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(f'Pssst, the solution is {chosen_word}')

display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for position in range(word_length) :
    letter = chosen_word[position]

    if letter == guess:
        display[position] = letter

  if guess not in chosen_word:
      lives -= 1
      if lives == 0 :
         end_of_game = True
         print("You lose.")

  print(f"{' '.join(display)}")

  if "_" not in display:
     end_of_game = True
     print("You Win.")

  print(stages[lives]) 
