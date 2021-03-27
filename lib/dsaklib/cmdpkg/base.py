'''INFO
Name:        base
Description: A set of base commands that are imported by default in DSAK
Author(s):   Robert Furr
Year:        2021

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''


from dsaklib.appmodules.shortcode import osName, os, system, pnt, color, homeDir, doFunEmojis, red, green, yellow, blue, cyan
from dsaklib.appmodules.config import *
import subprocess

def clr():
  '''Command for clearing the screen'''
  if osName == 'nt':
    system('cls')
  if osName == 'posix':
    system('clear')
clear = clr
cls   = clr

def ls(args=None,noargs=False):
  '''Command for listing files, doing color is enabled by default.'''
  if args == None:
    system('ls --color=auto')
  #disables the use of the --color=auto tag
  elif noargs == True:
    if agrs == None:
      system('ls')
    else:
      system('ls '+args)
  else:
    system('ls --color=auto '+args)

dir = ls

hlp_py = help


def hlp_man(manpage):
  '''Allows you to get help from a manpage of your choice'''
  system('man '+manpage)

def oscmd(command):
  '''Run a command through the OS using os.system()'''
  system(command)


def cd(directory=None):
  '''Allows you to change your directory'''
  #os.path
  curdir = os.path.abspath('./')
  pardir = os.path.abspath('../')
  if directory == None:
    directory = input('Directory?\n> ')
  if directory == '~':
    directory = homeDir
  if directory == '../':
    directory = pardir
  if directory == './':
    directory = curdir
  if doFunEmojis == True:
    pnt(color('|🗁  Attempting to switch to directory ',green)+color(directory,red))
  
  os.chdir(directory)
  if doFunEmojis == True:
      pnt(color('|🗁  Done',green))

def uname(args=None):
  '''Runs uname'''
  if args == None:
    if doFunEmojis == True:
      pnt(color('🖳 Uname info:',yellow))
    system('uname')
  else:
    system('uname '+args)

def cat(args,sudo=False):
  '''Runs cat'''
  if sudo == True:
    system('cat '+args)
  else:
    system('sudo cat '+args)

def leave():
  '''Does the same thing as exit()'''
  exit(0)

def info():
  '''Prints information about DSAK'''
  do_version = False

  pnt(color('Name:    ',green)+color(str(__Name__),red))
  pnt(color('Year:    ',green)+color(str(__Year__),red))
  pnt(color('Author:  ',green)+color(str(__Author__),red))
  if do_version == True:
    appVer_new    = color('Version: ',green)+color(str(appVer),red)
  pnt(color('License: ',green)+color(str(__License__),red))

#def dsak_help():
#  pnt('Coming soon')

def edit(args=None,editor='$EDITOR',sudo=False):
  '''Runs an editor ($EDITOR by default)'''
  if sudo == True:
    if args == None:
      system('sudo '+editor)
      print('Exited editor')
    else:
      system('sudo '+editor+' '+args)
      print('Exited editor')
  else:
    if args == None:
      system(editor)
    else:
      system(editor+' '+args)

def rm(args,sudo=False):
  '''Removes files'''
  if sudo == True:
    system('sudo rm '+args)
  else:
    system('rm '+args)

def mkdir(args,sudo=False):
  '''Creates a directory'''
  if sudo == True:
    system('sudo mkdir '+args)
  else:
    system('mkdir '+args)

def slogan():
  '''A slogan thing'''
  pnt('"Cutting free from the conventions of typical shells"')

def echo(args,sudo=False):
  if sudo == True:
    system('sudo echo '+args)
  else:
    system('echo '+args)