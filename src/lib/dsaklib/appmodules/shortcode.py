'''
A hub for values/imports/defs that tie most of DSAK together.
Made by Robert Furr
2021'''

import os,subprocess
from dsaklib.appmodules.termcolor import colored
from os import system
from dsaklib.appmodules.config import *
from socket import gethostname
from getpass import getuser
global homedir

pnt               = print
inpt              = input
pyhlp             = help
osName            = os.name
userName          = getuser()
hostName          = gethostname()
userName          = getuser()
homedir           = '/home/'+str(userName)
downloadsdir      = homedir+"/Downloads"
picturesdir       = homedir+"/Pictures"
documentsdir      = homedir+"/Documents"
musicdir          = homedir+"/Music"
videosdir         = homedir+"/Videos"
docsdir           = documentsdir
vidsdir           = videosdir
picsdir           = picturesdir
color             = colored
sp                = subprocess
green             = 'green'
blue              = 'blue'
yellow            = 'yellow'
red               = 'red'
cyan              = 'cyan'
promptState       = 'term'
curdir            = os.path.abspath('./')
pardir            = os.path.abspath('../')
colorPrompt       = True
doFunEmojis       = True

# This is down here because it needs to have colors defined
import dsaklib.appmodules.codemodified as code

def clear():
  '''Clear screen function'''
  system('clear')

def coming_soon():
  '''Simple message'''
  print('Coming soon')
#pnt("Detected OS: %s"%osName)
#system('clear')