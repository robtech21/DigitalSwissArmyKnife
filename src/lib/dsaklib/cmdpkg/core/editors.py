'''INFO
Name:        editors
Description: Editor commands for DSAK (core)
Author(s):   Robert Furr
Year:        2021

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

from dsaklib.appmodules.shortcode import *

defaultEditor = sp.getoutput('echo $EDITOR')
currentEditor = sp.getoutput('echo $EDITOR')

def edit(args=None,editor=currentEditor,sudo=False):
  '''Runs an editor of your choice'''
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

def vi(args=None,sudo=False):
  '''Runs the vi editor'''
  if sudo is True:
    if args is None:
      edit(args=None,editor='vi',sudo=True)
    else:
      edit(args=args,editor='vi',sudo=True)
  else:
    if args is None:
      edit(args=None,editor='vi')
    else:
      edit(args=args,editor='vi')

def nano(args=None,sudo=False):
  '''Runs the nano editor'''
  if sudo is True:
    if args is None:
      edit(args=None,editor='vi',sudo=True)
    else:
      edit(args=args,editor='vi',sudo=True)
  else:
    if args is None:
      edit(args=None,editor='vi')
    else:
      edit(args=None,editor='vi')