'''INFO
Name:        term_mcpi
Description: Control MCPI through DSAK using the MCPI API (coming soon)
Author(s):   Robert Furr
Year:        2021
Extra:       Looking for devs to work on this :)

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

from dsaklib.appmodules.shortcode import *

from dsaklib.appmodules.mcpi import minecraft

def connect():
  global mc
  '''Connect to MCPI via the API'''
  print('Attempting to connect')
  mc = minecraft.Minecraft.create()
  print('Done')

if __name__ == '__main__':
  print('MCPI Terminal')
  connect()