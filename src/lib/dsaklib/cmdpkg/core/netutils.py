'''INFO
Name:        netutils
Description: Networking commands for DSAK (core)
Author(s):   Robert Furr
Year:        2021

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

from dsaklib.appmodules.shortcode import *

def ssh(args=None):
  '''Runs ssh'''
  if args == None:
    system('ssh')
  else:
    if doFunEmojis is True:
      pnt(color('⎹  ‼  ⎸Note: Press CTRL+D to close connection',green))
      pnt(color('⎹  🖧  ⎸Attemping to run ssh with arguments ',green)+color(str(args),red))
    system('ssh '+args)
#‼
def ping(args=None):
  '''Pings a specified address'''
  if args == None:
    system('ping')
  else:
    if doFunEmojis is True:
      pnt(color('⎹  🖧  ⎸Attempting to ping address ',green)+color(args,red))
    system('ping '+args)

def pingtest():
  '''Tests ping command by pinging 127.0.0.1'''
  ping('127.0.0.1')

def wget(args):
  '''Runs the wget command'''
  system('wget '+args)