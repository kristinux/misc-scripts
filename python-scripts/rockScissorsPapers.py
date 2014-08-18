#!/usr/bin/python

'''
  Rock, scissors, paper example in Python
  Author: ksilinja
'''

import random
from sys import exit

def choose():
  '''
    Return user choice.
  '''
  return raw_input('\nEnter your choice: ').lower()
  
def replay():
  '''
    Game replay selection. If false, system exit is
    called.
  '''
  r = raw_input("\nPlay again?(y/n) ")
  if r.lower() == 'y':
    return True
  elif r.lower() == 'n':
    exit()
  else:
    replay()

def computer():
  ''' 
    Random choice of a list element returned as computer
    choice.
  '''
  computerChoice = random.choice(['rock','paper','scissors'])
  print 'Computer choice:', computerChoice
  return computerChoice


def compare(uChoice, cChoice):
  '''
    Runs user input and computer choice comparison.
  '''

  if uChoice == cChoice:
    return "It's a tie!\n"
    
  elif uChoice == 'paper':
    if cChoice == 'scissors':
      return 'Scissors cut paper - SCISSORS win!'
    elif cChoice == 'rock':
      return 'Paper covers rock - PAPER wins!'

  elif uChoice == 'rock':
    if cChoice == 'paper':
      return 'Paper covers rock - PAPER wins!'
    elif cChoice == 'scissors':
      return 'Rock beats scissors - ROCK wins!'

  elif uChoice == 'scissors':
    if cChoice == 'paper':
      return 'Scissors cut paper - SCISSORS win!'
    elif cChoice == 'rock':
      return 'Rock beats scissors - ROCK wins!'
  else:
    print '\nWrong input! Choose from: rock, scissors or paper'
    if replay() == True:
        play(choose(), computer())

      
def play(userChoice, compChoice):
  '''
    Gameplay and replay launch.
  '''
  print compare(userChoice, compChoice)
  replay()
  

try:
  print "\nWelcome to Rock, Scissors, Paper classical game!"
  print "You will be playing against the computer.\n"
  
  while 1:
    play(choose(), computer())

except KeyboardInterrupt:
    print "\nCtrl+C caught. Exiting...\n"
    exit()
