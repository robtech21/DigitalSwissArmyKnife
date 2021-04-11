#!/usr/bin/env python3

import os

# Anti-Windows Countermeasure ;)
if os.name == 'nt':
  print("We don't allow your kind here")
  exit(1)

# Import essential modules
import dsaklib
import dsaklib.appmodules.config as Config
from dsaklib import *
from dsaklib.appmodules.shortcode import *
from dsaklib.appmodules.config import *

# Add base commands
from dsaklib.cmdpkg.core.base import *

# Add any extra command sets here
from dsaklib.cmdpkg.musicplayer import *
from dsaklib.cmdpkg.multipkg import *

# Help command
def hlp(type=None,args=None):
  '''Displays Help'''
  if type == 'dsak':
    pnt('dsak')
  if type == 'py':
    if args == None:
      args == inpt('args>')
      if args == '':
        pnt('Opening the Python help menu')
        help()
      else:
        help(args)

# All of the magic begins here
if welcome_msg == True:
  slogan()
  pnt(color("Digital Swiss Army Knife",red))
  pnt(color("Welcome to the ",green)+color('Future\n',red))
  pnt(color('Version ',green)+color(Config.__Version__,red)+color('\nType hlp() ',red)+color('to get help with DSAK or Python',green))
code.interact(banner='', readfunc=None, local=locals(),exitmsg=color('Exit',green))
