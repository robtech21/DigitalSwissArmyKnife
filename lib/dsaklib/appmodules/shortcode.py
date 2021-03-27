'''A hub for values/imports/defs that tie most of DSAK together.
Made by Robert Furr
2021'''

import os
from dsaklib.appmodules.termcolor import colored
from os import system
from dsaklib.appmodules.config import *
from socket import gethostname
from getpass import getuser
global homeDir
pnt              = print
inpt             = input
hlp              = help
osName           = os.name
userName         = getuser()
hostName         = gethostname()
userName         = getuser()
homeDir          = '/home/'+str(userName)+"/"
color            = colored
green            = 'green'
blue             = 'blue'
yellow           = 'yellow'
red              = 'red'
cyan             = 'cyan'
promptState      = 'term'
colorPrompt      = True
doFunEmojis      = True
if colorPrompt == True:
  userPrompt  = color("[",yellow)+color(str(userName),blue)+color("@",green)+color(str(hostName),blue)+color("|",yellow)+color("(",green)+color(promptState,blue)+color(")",green)+color("]",yellow)+color("$ ",cyan)
if colorPrompt == False:
  userPrompt  = "["+str(userName)+"@"+str(hostName)+"|("+str(promptState)+")"+"]$ "
if osName == 'posix': 
  import readline
def clear():
  '''Clear screen function'''
  system('clear')
#Legacy components from prior projects
def updatePrompt():
  '''Legacy component, do not use'''
  global userPrompt
  userPrompt = color("[",yellow)+color(str(userName),blue)+color("@",green)+color(str(hostName),blue)+color("|",yellow)+color("]",yellow)+color("$ ",cyan)
def changePrompt(state):
  '''Legacy component, do not use'''
  global userPrompt,promptState
  '''Legacy component, do not use'''
  promptState = state
  updatePrompt()
def userInput(promptstate):
  '''Legacy component, do not use'''
  changePrompt(promptstate)
  result = input(str(userPrompt))
  return result
import dsaklib.appmodules.codemodified as code

def coming_soon():
  '''Simple message'''
  print('Coming soon')
#pnt("Detected OS: %s"%osName)
#system('clear')