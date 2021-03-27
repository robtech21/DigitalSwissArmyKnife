'''INFO
Name:        webutil
Description: Web utilities
Author(s):   Robert Furr
Year:        2021

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

from os import system

def wget(args):
  '''Runs the wget command'''
  system('wget '+args)

def w3m(args):
  '''Runs w3m'''
  system('w3m '+args)