# Hangman Game
# A simple word guessing game using strings, lists, and functions

# TODO: Import the random module to select random words


word_list = [
    "python",
    "hangman",
    "computer",
    "programming",
    "keyboard",
    "elephant",
    "calendar",
    "sunshine",
    "mountain",
    "basketball",
    "orchestra",
    "universe",
    "chemistry",
    "adventure"
]
import random
random.choice(word_list) 

# TODO: Create a function to select a random word that:
# - Takes no parameters
# - Uses random.choice to select a random word from your word list
# - Returns the selected word in lowercase

def get_random_word():
  selected_word = random.choice(word_list)
  return selected_word
# Testing the function
print(get_random_word())

# TODO: Create a function to initialize the game state that:
# - Takes parameter: word (str)
# - Creates and returns a dictionary with these keys:
#   - "word": the word to guess
#   - "guessed_letters": an empty list to track guessed letters
#   - "word_completion": a string of underscores representing unguessed letters (e.g., "_ _ _ _")
#   - "tries_remaining": number of incorrect guesses allowed (start with 6)

def initialize_game_state(word):
   game_state= { 
        "word": word,
        "guessed_letters": [],
        "word_completion": "_ " * len(word),
        "tries_remaining": 6
      }
   return game_state

# TODO: Create a function to display the game state that:
# - Takes parameter: game_state (dict)
# - Prints the current hangman state based on tries_remaining
#   (You can use ASCII art for different hangman states)
# - Prints the current word completion (with spaces between letters)
# - Prints the letters that have been guessed so far
# - Prints the number of tries remaining
# ASCII art for hangman states
HANGMAN_STAGES = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========='''
]


def display_game_state(game_state):
   tries_remaining = game_state["tries_remaining"]
   print(HANGMAN_STAGES[tries_remaining])
   print("Word to guess: " + " ".join(game_state["word_completion"]))
   print("Guessed letters: " + " ,".join(game_state["guessed_letters"]))
   print(f"Tries remaining: {game_state['tries_remaining']}")


# TODO: Create a function to get a valid letter guess that:
# - Takes parameter: game_state (dict)
# - Asks the user to guess a letter
# - Validates that the input is:
#   - A single character
#   - A letter (not a number or symbol)
#   - Not already guessed
# - Returns the valid guessed letter in lowercase
# - Keeps asking until a valid letter is entered

def get_valid_letter_guess(game_state):
   while True:
      guess= input("Guess a letter:").lower()
      if len(guess) !=1:
         print("Please enter a letter.")
         continue 
      if not guess.isalpha():
         print("Please enter a letter.")
         continue
      if guess in game_state["guessed_letters"]:
         print("You have already guessed that letter. Try again.")
         continue
      return guess 

# TODO: Create a function to update the game state that:
# - Takes parameters: game_state (dict) and guessed_letter (str)
# - Adds the guessed letter to the guessed_letters list
# - Checks if the guessed letter is in the word
# - If it is, updates the word_completion to reveal the letter
# - If it's not, decreases the tries_remaining
# - Returns True if the guess was correct, False otherwise

def update_game_state(game_state, guessed_letter):
   game_state["guessed_letters"].append(guessed_letter)

   if guessed_letter in game_state["word"]: 
      word_completion_list = list(game_state["word_completion"])
      for index, letter in enumerate(game_state["word"]):
         if letter == guessed_letter:
            word_completion_list[index] = guessed_letter
            game_state["word_completion"] = ''.join(word_completion_list)
            return True 
   else:
      game_state["tries_remaining"] -= 1
      return False     

# TODO: Create a function to check if the game is over that:
# - Takes parameter: game_state (dict)
# - Returns True if the word is completely guessed or no tries remain
# - Returns False otherwise

def is_game_over(game_state):
   if '_' not in game_state["word_completion"]:
      return True
   if game_state["tries_remaining"] <= 0:
      return True
   return False 

# TODO: Create a function to check if the player won that:
# - Takes parameter: game_state (dict)
# - Returns True if the word_completion matches the word (no more underscores)
# - Returns False otherwise

def is_player_won(game_state): 
   if '_' not in game_state["word_completion"]:
      return True
   else:
      return False 

# TODO: Create the main game function that:
# - Takes no parameters
# - Selects a random word
# - Initializes the game state
# - Displays welcome message and initial game state
# - Loops until the game is over:
#   - Gets a valid letter guess
#   - Updates the game state with the guess
#   - Displays the updated game state
# - When game ends, displays win or lose message
# - Reveals the word if the player lost
# - Asks if the player wants to play again

def play_hangman():
   selected_word = get_random_word()
   game_state = initialize_game_state(selected_word)
   print("Welcome to Hangman!")
   display_game_state(game_state)
   while not is_game_over(game_state):
       guessed_letter = get_valid_letter_guess(game_state)
       update_game_state(game_state, guessed_letter)
       display_game_state(game_state)
   
   if is_player_won(game_state):
      print("Congratulations, you won!")
   else: 
      print(f"Sorry, you lost. The word was{game_state['word']}.")  

   play_again = input("Do you want to play again? (yes/no):").lower()
   if play_again == "yes" :
      play_hangman()
   else:
      print("Thanks for playing!")        

# TODO: Create the main program that:
# - Prints a welcome message
# - Calls the main game function
# - Handles play again logic

       
if __name__ == "__main__":
   print("Welcome to Hangman!")

   play_hangman()          
