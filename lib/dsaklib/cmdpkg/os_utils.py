'''Operating system type utilities'''
from dsaklib.appmodules.shortcode import *
import subprocess
from os import chdir
def exit_notice():
  pnt('Press CTRL-D to exit to DSAK')
def bash(cmd=None):
  '''Runs bash'''
  if cmd == None:
    exit_notice()
    subprocess.run(['/bin/bash'])
  else:
    subprocess.run(['/bin/bash','-c',cmd])
def sh(cmd=None):
  '''Runs sh'''
  if cmd == None:
    exit_notice()
    subprocess.run(['/bin/sh'])
  else:
    subprocess.run(['/bin/sh','-c',cmd])

downloads = "Downloads"
pictures  = "Pictures"
videos    = "Videos"
documents = "Documents"
Downloads = downloads
Pictures  = pictures
videos    = videos
pics      = pictures
vids      = videos
docs      = documents

def home_goto(folder=None):
  '''Go to a home folder'''
  if folder == None:
    pnt('Switched to home directory')
    chdir(homeDir)
  else:
    chdir(str(homeDir)+"/"+folder)