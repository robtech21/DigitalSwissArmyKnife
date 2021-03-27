'''INFO
Name:         git
Description:  Execute certain Git functions
Author(s):    Robert Furr
Year:         2021

Extra:        Requesting for someone with more experience in using git via terminal to write more code for this
Goals:        To make using git through the command line much easier

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

from os import system
from dsaklib.appmodules.shortcode import *

def gitman():
  choice = inpt(color('''Options:

1. Git Every Day
2. Git Tutorial

> ''',green))

def Git(args):
  '''A blank slate git command'''
  system('git '+args)

def clone(repo,args=None):
  '''Clones a git repo of your choice'''
  print('Attempting to clone repo '+repo)
  if args == None:
    system('git clone '+repo)
  else:
    system()