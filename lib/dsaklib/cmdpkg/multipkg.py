'''INFO
Name:        multipkg
Description: Utilize multiple Linux package managers through DSAK
Author(s):   Robert Furr
Year:        2021

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''



from os import system

class pip:
  '''Pip package manager commands'''
  def pip(args=None):
    '''A blank slate pip command'''
    system('python3 -m pip '+args)

  def install(package):
    '''Installs package(s) via pip'''
    system('python3 -m pip install '+package)

  def upgrade():
    '''Upgrades pip'''
    confirm = input('You are about to upgrade pip, do you want to continue? (y/n)\n> ')
    if confirm == 'y':
      print('Attempting to upgrade pip')
    else:
      print('Aborted')