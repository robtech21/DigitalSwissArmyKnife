'''INFO
Name:        cmdparser
Description: An experimental CLI parser for DSAK
Author(s):   Robert Furr
Year:        2021
Extra:       May never be used

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

from dsaklib.appmodules.shortcode import *
from dsaklib.cmdpkg.base import ls
import cmd

class CMD:
  '''Main class'''
  def cli():
    '''Interactive interface'''
    term = cmd.Cmd()
    while True:
      terminput = inpt('cli> ')
      result = term.parseline(terminput)
      if result[0] == 'exit':
        break
      if result[0] == 'ls':
        if result[1] == "":
          ls()
        else:
          ls(result[1])
        