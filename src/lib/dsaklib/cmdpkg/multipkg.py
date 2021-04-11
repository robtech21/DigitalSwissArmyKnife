'''INFO
Name:        multipkg
Description: Utilize multiple Linux package managers through DSAK
Author(s):   Robert Furr
Year:        2021

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

pnt   = print
inpt  = input

from os import system

class multipkg:
  '''Just a class that prevents potential value screwups in other modules'''
  def viewhelp():
    '''Not a lot here'''
    help('dsaklib.cmdpkg.multipkg')
  
  def confirm(action):
    '''Confirmation message'''
    global choice
    choice = inpt('Action(s): '+action+'\nContinue? (y/n)\nconfirm> ')
  
  def abort():
    '''Aborted message'''
    pnt('Aborted')

class pip:
  '''pip package manager class'''
  def main(args=None):
    '''Blank slate pip command'''
    if args == None:
      system('python3 -m pip')
    else:
      system('python3 -m pip '+args)

  def install(package):
    '''Installs pip package(s)'''
    multipkg.confirm('Install package(s) '+package)
    if choice == 'y':
      pip.main('install '+package)
    else:
      multipkg.abort()
  
  def uninstall(package):
    '''Uninstalls pip package(s)'''
    multipkg.confirm('Uninstall package(s) '+package)
    if choice == 'y':
      pip.main('uninstall '+package)
    else:
      multipkg.abort()

  def upgrade():
    '''Upgrades pip'''
    multipkg.confirm('Upgrade pip')
    if choice == 'y':
      pip.main('install --upgrade pip')
    else:
      multipkg.abort()

class apt:
  '''apt package manager class'''

  def main(args=None):
    '''Blank slate apt command'''
    if args == None:
      system('sudo apt')
    else:
      system('sudo apt '+args)

  def update(args=None):
    '''Run sudo apt update (no arguments by default)'''
    multipkg.confirm('Update using apt')
    if choice == 'y':
      apt.main('update')
    else:
      multipkg.abort()
  
  def upgrade(args=None):
    '''Run sudo apt upgrade (no arguments by default)'''
    multipkg.confirm('Upgrade using apt')
    if choice == 'y':
      apt.main('upgrade')
    else:
      multipkg.abort()