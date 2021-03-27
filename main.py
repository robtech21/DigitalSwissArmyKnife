#!/usr/bin/env python3
import dsaklib
from dsaklib import *
from dsaklib.appmodules.shortcode import *
from dsaklib.cmdpkg.base import *
from dsaklib.cmdpkg.testing import *
from dsaklib.appmodules.config import *

if welcome_msg == True:
  pnt(color("Digital Swiss Army Knife",red))
  pnt(color("Welcome to the ",green)+color('Future\n',red))
  pnt(color('Pre-Release ',red)+color('Version\nType ',green)+color('help() ',red)+color('for DSAK help or ',green)+color('python_help() ',red)+color('for normal help\n'))
code.interact(banner='', readfunc=None, local=locals(),exitmsg=color('Exit',green))
