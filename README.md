# DigitalSwissArmyKnife
A digital multitool that uses a customized Python interpreter as a base

The source for the modules can be found [here](https://github.com/robtech21/dsaklib) (Incomplete at the moment)

Note: This README file is **incomplete** and DSAK is still under **heavy development** so nothing will be uploaded as of now.

# About

## Information
Digital Swiss Army Knife (or DSAK for short), is a digital command line utility written in Python that runs on a customized interpreter through a modified version of the `code` module.

## Features
### cmdpkg
cmdpkg is a system of module-based command "packages" that you can import into the DSAK (or any other Python interpreter or script). By default, the `main.py` script will import `cmdpkg.base` by default like this:

```py
from cmdpkg.base import * #Imports base commands
```

There are also a few other utilities that come packaged by default, you can import them this way at the moment:

```py
from cmdpkg.misc import * #Imports a small set of misc commands
```
Other packages I have planned:

### Base Commands
Here are a handful of base commands:

Command   | Description | Function it calls
--------- | ----------- | -------------
`cd()`    | Change directory | `os.chdir()`
`ls()`    | Shows the files of your current directory | `os.system('ls')`
`clr()`   | Clears the screen | `os.system('clear')`
`cls()`   | Same as `clr()` | `clr()`
`clear()` | Same as `clr()` | `clr()`
`editor()`| Opens the default editor | `os.system('$EDITOR')`
`sudo_editor()` | Opens default editor as sudo | `os.system('sudo $EDITOR')`

(The function these call isn't exact to the source code)

### Future Module Ideas

* A MCPI command set (simplified commands from the `mcpi` module)
* Something that handles compression using `tar`
* 

# Setup
(Coming soon)
## Install
(Coming soon)
## Configuration
(Coming Soon)
### Add custom command sets to cmdpkg
(Coming soon)
