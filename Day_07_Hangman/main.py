import random
print("Welcome to the game Hangman!")
print("HINTS!!! Just think of a fruit")
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

word_list = [
    "apple",
    "banana",
    "orange",
    "grape",
    "mango",
    "pineapple",
    "watermelon",
    "strawberry",
    "blueberry",
    "kiwi",
    "papaya",
    "peach",
    "pear",
    "plum",
    "cherry",
    "coconut",
    "lemon",
    "lime",
    "guava",
    "avocado"]

secret_word=random.choice(word_list)


placeholder ="_"*len(secret_word)
print(placeholder)
game_over=False
guessed_letters=[]
no_of_lives=6
while not game_over:
    print(f"***********<???>/{no_of_lives} LIVES LEFT*************")
    guess= input("Guess a letter: ").lower()
    display=""
    if guess in guessed_letters:
        print(f"letter already guessed the letter{guess}")
    for letter in secret_word:
        if guess==letter:
            display+=letter
            guessed_letters.append(guess)
        elif letter in guessed_letters:
            display+=letter

        else:
            display+="_"
    print(display)
    if guess not in secret_word:
        print(f"Your letter {guess} is not in the fruit")
        no_of_lives-=1
        if no_of_lives==0:
            game_over=True
            print("You lost!")
            print(f"The friut was {secret_word}. ")

    if display==secret_word:
        game_over=True
        print("You win!")
    print(HANGMANPICS[no_of_lives])