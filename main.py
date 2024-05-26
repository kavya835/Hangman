#Import modules.
import random
import os

clear = lambda: os.system('clear')
import time
#___________________________________________________________

#Word Dictionary
w_1 = ("toronto", "This is one of the most populous cities in Canada.")
w_2 = (
    "tokyo",
    "This city is one of the world's largest metropolitan areas. It is home to the largest 'tower' in the world which stands at 634m."
)
w_3 = ("paris", "This city is one of the fashion captials of the world.")
w_4 = (
    "london",
    "The famous Tower Bridge is one of the many landmarks found in this city.")
w_5 = (
    "rome",
    "This capital city is widely known for its culture and historical architecture that dates back to 509 BC."
)
w_6 = (
    "bangkok",
    "This Thai city is home to the Grand Palace and is home to various temples and shrines."
)
w_7 = (
    "chicago",
    "This city is nicknamed the 'Windy City' and is located near Lake Michigan."
)
w_8 = (
    "montreal",
    "This French-speaking city has hosted a variety of events including the 1976 Summer Olympics."
)
w_9 = (
    "athens",
    "This is Europe's oldest capital city and home to famous architectural buildings like the Acropolis."
)
w_10 = (
    "beijing",
    "This is one of the oldest cities in the world and is home to the world’s largest imperial garden as well as one of the seven wonders of the world."
)
w_11 = (
    "seoul",
    "This capital city is home to Lotte World, one of the world's largest indoor theme parks, and various cultural and artistic attractions."
)
w_12 = (
    "amsterdam",
    "This is a European city built on poles and is well-known for its canals and narrow houses."
)
w_13 = (
    "delhi",
    "One of the famous landmarks of this city is the Red Fort which was built back in 1648."
)
w_14 = (
    "sydney",
    "This city is famous for its sail-shaped opera house and is known as the Harbour City."
)
w_15 = (
    "cairo",
    "This Egyptian city is home to one of the wonders of the world, as well as artifacts from the ancient world."
)
w_16 = (
    "lisbon",
    "This capital city is home to St. George's Castle, as well as the National Tile museum."
)

#This is the list of words.
word_list = [
    w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8, w_9, w_10, w_11, w_12, w_13, w_14,
    w_15, w_16
]

#Hangman structure and art.
stickman_art = [
    " |----\n |\n |\n |\n---", " |----\n |   O\n | \n | \n---",
    " |----\n |   O\n |   |\n |\n---", " |----\n |   O\n |  \|\n |\n---",
    " |----\n |   O\n |  \|/\n |\n---", " |----\n |   O\n |  \|/\n |  /\n---",
    " |----\n |   O\n |  \|/\n |  / \\\n---"
]


def welcome():
  import welcome_art
  #Print the welcome statement.
  print("\nWelcome to Hangman with Cities Around the World!\n")

  #Print the instructions.
  instructions()

  #Ask for user name.
  user_name = input("\n\nPlease enter a user name: ")
  print("\nStarting Hangman with Cities Around the World for " + user_name +
        ", good luck!\n")


def instructions():
  #Print the instructions.
  print(
      "There are 5 rounds in this game. You will win after you have finished all 5 rounds."
  )
  print("Each round will consist of a word from our dictionary.")
  print(
      "For every incorrect letter, a stroke will be added to the stickman. If the entire stickman is hung, you will have exhausted your guesses and it's game over."
  )
  print("If you guess correctly, you'll move onto the next round.")
  print("Once you complete all 5 rounds, you'll be declared a winner.")


def new_round(num):
  #Select a random number and set it as the index of the element in 'word_list'.
  word_num = random.randint(1, len(word_list))
  word_string = word_list[word_num - 1][0]
  word_hint = word_list[word_num - 1][1]

  #Remove the word from the 'word_list' so that it doesn't repeat.
  word_list.pop(word_num - 1)

  #Create an empty string and list, to keep track of the dashes and the incorrect letters.
  dash_string = ("")
  incorrect_letters_str = ("")
  incorrect_letters = list(incorrect_letters_str)

  #Create the dashes, based on the number of letters in the word.
  for each in word_string:
    dash_string += ("-")

  #Wait 1 second before starting a new round.
  time.sleep(1)

  while (True):
    #Print the "Staring round" statement with 'num' changing each time.
    print("\nStarting round", num, "...\n")

    #Print the hint, the 'stickman_art', the user's guesses and the incorrect letters.
    print(word_hint)
    print(stickman_art[len(incorrect_letters)])
    print("Your guesses so far: " + dash_string)
    print("Incorrect letters: " + incorrect_letters_str)

    #___________________________________________________________
    #If the user guesses all the letters, print the corresponding statement and break the 'while' loop.
    if word_string == dash_string:
      print("\nYAY! You guessed the city!\n")
      return "Next Round"

    #If the number of incorrect guesses is equal to 6, print the corresponding statement and break the loop.
    if len(incorrect_letters) == 6:
      print(
          "\nOOPS! You have exhausted your chances. Game over, better luck next time!\n"
      )
      return "Game Over"
    #___________________________________________________________

    #Ask the user to guess a letter.
    user_guess = input("\nGuess a letter: ").lower()

    #Iterate throught the loop to see if the user's guess is present in the word.
    for i in range(len(word_string)):
      if word_string[i] == user_guess:
        #If it is, convert the string of dashes into a list so that it is mutable.
        dash_list = list(dash_string)
        #Set the 'delimiter' to an empty string so that when changing the list back into a string, the letters don't have any space in between them.
        delimiter = ""

        #Change the dash into the user's letter.
        dash_list[i] = user_guess

        #Join all the element in 'dash_list' into a string.
        dash_string = delimiter.join(dash_list)

    #If the user's guess is not in the word, add their guess to the list of incorrect letters.
    if user_guess not in word_string:
      incorrect_letters.append(user_guess)

      #Join all the elements in 'incorrect_letters' into a string.
      delimiter_incorrect = " "
      incorrect_letters_str = delimiter_incorrect.join(incorrect_letters)

    #Clear the console.
    clear()


def five_rounds():
  for i in range(5):
    #Call the 'new_round(num)' function.
    result = new_round(i + 1)
    result

    #If the 'new_round(num)' function returns "Game Over", end the game.
    if result == "Game Over":
      return "end"


def congratulations():
  #Call the 'five_rounds()' function.
  final_result = five_rounds()
  final_result

  #If the user finishes all five rounds [If the 'five_rounds()' function doesn't return "end"], print the congratulations statement.
  if final_result != "end":
    print("\nCongratulations! You won all five rounds!")


#Call the functions
welcome()
congratulations()
