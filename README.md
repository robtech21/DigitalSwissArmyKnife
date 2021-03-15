# DigitalSwissArmyKnife
A digital multitool that uses a customized Python interpreter as a base

Note: This README file is **incomplete** and DSAK is still under heavy development so nothing will be uploaded as of now.

# About

## Information
Digital Swiss Army Knife (or DSAK for short) is a digital command line utility written in Python that runs on a customized interpreter through a modified version of the `code` module.

## Features
### cmdpkg
cmdpkg is a system of module-based command "packages" that you can import into the DSAK (or any other Python interpreter or script). By default, the __main__.py script will import cmdpkg.base by default like this:

```py
from cmdpkg.base import * #Imports base commands
```

This imports all of the base commands that will run on DSAK by default.

There are also a few other utilities that come by default:

```py
from cmdpkg.misc import * #Imports a small set of misc commands
```
Other packages I have planned:

### Base Commands
Here are a handful of base commands:

```py
cd() #Change directory
ls() #Shows your files

# The next 3 clear the screen when ran
clr()
cls()
clear()

editor() # Runs the default editor
sudo_editor() # Runs the default editor in sudo
```

# Setup
Coming soon
## Install

## Configuration

### Add to cmdpkg
