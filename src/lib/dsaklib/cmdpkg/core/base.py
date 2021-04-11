'''INFO
Name:        base
Description: A set of base commands that are imported by default in DSAK (core)
Author(s):   Robert Furr
Year:        2021

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

import dsaklib.appmodules.config as Config
from dsaklib.appmodules.shortcode import *

# Core packages added here
from dsaklib.cmdpkg.core.editors import *
from dsaklib.cmdpkg.core.netutils import *

def clr():
  '''Command for clearing the screen'''
  system('clear')
clear = clr
cls   = clr

def ls(args=None,nocolor=False):
  '''Command for listing files, doing color is enabled by default.'''
  currentdir = os.getcwd()
  pnt(color('⎹  🗁  ⎸Contents of directory ',green)+color(str(currentdir),red)+color(':',green))
  if args == None:
    system('ls --color=auto')
  # Disables the use of the --color=auto tag

  elif nocolor == True:
    if agrs == None:
      system('ls')
    else:
      system('ls '+args)
  else:
    system('ls --color=auto '+args)
os.path.curdir
dir = ls

hlp_py = help


def man(manpage=None,prompt=False):
  '''Allows you to get help from a manpage of your choice'''
  if manpage is None:
    prompt = True
  elif prompt is True:
    manpage = inpt('man> ')
    system('man '+manpage)
  else:
    system('man '+manpage)

def oscmd(command):
  '''Run a command through the OS using os.system()'''
  system(command)

def cd(directory=None):
  '''Allows you to change your directory'''
  do_cd = True
  if directory == None:
    directory = input('Directory?\n> ')
  if '~' in directory:
    print(color("Home dir is not supported right now, try cd(homedir)",red))
    do_cd = False
  if do_cd == True:
    directory = os.path.abspath(directory)
    if doFunEmojis == True:
      pnt(color('⎹  🗁  ⎸Attempting to switch to directory ',green)+color(directory,red))
    os.chdir(directory)
    if doFunEmojis == True:
      pnt(color('⎹  🗀  ⎸Done',green))

def up1():
  '''Go to parent directory'''
  cd('../')

def uname(args=None):
  '''Runs uname'''
  if args == None:
    if doFunEmojis == True:
      pnt(color('🖳 Uname info:',yellow))
    system('uname')
  
  else:
    pnt(color('🖳 Uname info:',yellow))
    system('uname '+args)

def cat(args,sudo=False):
  '''Runs cat'''
  if sudo == True:
    system('sudo cat '+args)
  else:
    system('cat '+args)

def leave():
  '''Does the same thing as exit()'''
  exit(0)

def info():
  '''Prints information about DSAK'''
  do_version = False

  pnt(color('Name:    ',green)+color(Config.__Name__,red))
  pnt(color('Version: ',green)+color(Config.__Version__,red))
  pnt(color('Year:    ',green)+color(Config.__Year__,red))
  pnt(color('Author:  ',green)+color(Config.__Author__,red))
  pnt(color('License: ',green)+color(Config.__License__,red))

def verinfo():
  '''Displays version info'''
  pnt('Version info:\n')
  pnt('Major Release: '+Config.fullver[0])
  pnt('Minor Release: '+Config.fullver[1])
  pnt('Patch Release: '+Config.fullver[2])

def mkdir(args,sudo=False):
  '''Creates a directory'''
  if sudo == True:
    system('sudo mkdir '+args)
  else:
    system('mkdir '+args)


def rm(args,sudo=False):
  '''Removes files or directories'''
  if sudo == True:
    system('sudo rm '+args)
  else:
    system('rm '+args)

def slogan():
  '''A slogan thing'''
  pnt(color('\n"Cutting free from the conventions of typical shells"\n',green))

def echo(args=None,sudo=False):
  '''Runs echo'''
  if sudo == True:
    if args == None:
      system('sudo echo')
    else:
      system('sudo echo '+args)
  else:
    if args == None:
      system('echo')
    else:
      system('echo '+args)

def top(args=None):
  '''Runs the top task manager'''
  if args == None:
    system('top')
  else:
    system('top '+args)

def htop(args=None):
  '''Runs the htop task manager (requires htop to be installed)'''
  if args == None:
    system('htop')
  else:
    system('htop '+args)

def basehelp():
  """Runs help('dsaklib.cmdpkg.base')"""
  help('dsaklib.cmdpkg.base')

def taskman():
  '''Runs the best terminal task manager the script can find'''
  if sp.getoutput('whereis htop') == 'htop: /usr/bin/htop /usr/share/man/man1/htop.1.gz':
    htop()
  else:
    top()