# This is an enjoyable Python project idea to emulate the word-guessing game,
# Hangman. We’ve used a predefined list of words for the guessing aspect,
# but feel free to improve this by using a third-party dictionary API.
# This Python project uses loops, functions, and string formatting to print the hangman’s progress.
# It also lets you experiment with the standard library's random, time, and os modules.
# Specifically, we’ve used the random module to select the word to guess,
# the os module to clear the screen, and the time module’s
# .sleep() function to introduce pauses to enhance the game flow.
#
# Это приятная идея проекта на Python, имитирующая игру в угадывание слов Hangman.
# Мы использовали заранее определенный список слов для аспекта угадывания,
# но не стесняйтесь улучшать его, используя сторонний словарь API.
# Этот проект на Python использует циклы, функции и форматирование строк для печати прогресса палача.
# Это также позволяет вам экспериментировать с модулями стандартной библиотеки random, time и os.
# В частности, мы использовали модуль random для выбора слова для угадывания,
# модуль os для очистки экрана и функцию
# .sleep() временного модуля для введения пауз для улучшения игрового процесса.

'''
Hangman Game
-------------------------------------------------------------
'''


import random
import time
import os


def play_again():
  question = 'Do You want to play again? y = yes, n = no \n'
  play_game = input(question)
  while play_game.lower() not in ['y', 'n']:
      play_game = input(question)

  if play_game.lower() == 'y':
      return True
  else:
      return False


def hangman(word):
  display = '_' * len(word)
  count = 0
  limit = 5
  letters = list(word)
  guessed = []
  while count < limit:
      guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
      while len(guess) == 0 or len(guess) > 1:
          print('Invalid input. Enter a single letter\n')
          guess = input(
              f'Hangman Word: {display} Enter your guess: \n').strip()

      if guess in guessed:
          print('Oops! You already tried that guess, try again!\n')
          continue

      if guess in letters:
          letters.remove(guess)
          index = word.find(guess)
          display = display[:index] + guess + display[index + 1:]

      else:
          guessed.append(guess)
          count += 1
          if count == 1:
              time.sleep(1)
              print('   _____ \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - count} guesses remaining\n')

          elif count == 2:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - count} guesses remaining\n')

          elif count == 3:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - count} guesses remaining\n')

          elif count == 4:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - count} guesses remaining\n')

          elif count == 5:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |    /|\ \n'
                    '  |    / \ \n'
                    '__|__\n')
              print('Wrong guess. You\'ve been hanged!!!\n')
              print(f'The word was: {word}')

      if display == word:
          print(f'Congrats! You have guessed the word \'{word}\' correctly!')
          break


def play_hangman():
   print('\nWelcome to Hangman\n')
   name = input('Enter your name: ')
   print(f'Hello {name}! Best of Luck!')
   time.sleep(1)
   print('The game is about to start!\nLet\'s play Hangman!')
   time.sleep(1)
   os.system('cls' if os.name == 'nt' else 'clear')

   words_to_guess = [
       'january', 'border', 'image', 'film', 'promise', 'kids',
       'lungs', 'doll', 'rhyme', 'damage', 'plants', 'hello', 'world'
   ]
   play = True
   while play:
       word = random.choice(words_to_guess)
       hangman(word)
       play = play_again()

   print('Thanks For Playing! We expect you back again!')
   exit()


if __name__ == '__main__':
  play_hangman()


