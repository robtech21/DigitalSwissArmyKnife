'''INFO
Name:        musicplayer
Description: Plays music or audio so your sessions won't be as boring :)
Author(s):   Robert Furr
Year:        2021
Extra:       You'll need to have VLC installed to be able to use this

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

import subprocess,os,dsaklib.appmodules.termcolor
from os import system
from dsaklib.appmodules.termcolor import colored
color = colored

class music:
  '''The main music class'''
  def play(dir,silent=True):
    '''Plays music out of the directory of your choice'''
    if silent == True:
      # Kills running VLC processes so audio doesn't overlap
      system('killall vlc&>/dev/null')
      dir = os.path.abspath(dir)
      print(color('⎹  🎝  ⎸Attempting to play music out of directory ','green')+color(dir,'red'))
      system("cvlc '"+dir+"'&>/dev/null&")
    else:
      system('killall vlc')

  def stop(silent=True):
    '''Kills the vlc process to stop the music'''
    if silent == True:
      system('killall vlc&>/dev/null')
    else:
      system('killall vlc')