'''INFO
Name:        smolutils
Description: A bunch of random utilities that are too "smol" to have their own command sets
Author(s):   Robert Furr
Year:        2021
Extra:       Will become obsolete soon

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

from dsaklib.appmodules.shortcode import *

class diskutil:
  '''INFO
Name:        diskutil
Description: Handles disk/partition management
Author(s):      Robert Furr

(some of the def descriptions were pulled straight from the manpages lol)'''

  def dd(args,sudo=False):
    '''Convert and copy a file'''
    if sudo == True:
      system('sudo dd '+args)
    else:
      system('dd '+args)
  def mount(args,sudo=False):
    '''Mount a filesystem'''
    if sudo == True:
      system('sudo mount '+args)
    else:
      system('mount '+args)
  def umount(args,sudo=False):
    '''Unmount a filesystem'''
  unmount = umount

class webutil:
  '''INFO
Name:        webutil
Description: Web utilities
Author(s):   Robert Furr'''

  def wget(args):
    '''Runs the wget command'''
    system('wget '+args)

  def w3m(args):
    '''Runs w3m'''
    system('w3m '+args)