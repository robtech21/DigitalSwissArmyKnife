[Back to main wiki page](wiki.md)

# Usage

__This page covers how to use the DSAK terminal__

## Contents

* [Using the interpreter](#using-the-interpreter)
* [Using commands](#using-commands)


<br><br>


## Using the Interpreter

DSAK is built on top of a custom Python interpeter, so it functions exactly like a standard interpreter. Here are a few examples:

<br>

__Hello World__
```
⎹\⎺⎺⎺⎺⎸[/home/boba/coding-projects/DSAK/DigitalSwissArmyKnife]
⎹⎻\⎻⎻⎻⎸[boba@alpha]
⎹⎼⎼\⎼⎼⎸[>>>]$ print('Hello, world!')
Hello, world!
```

<br>

__Boolean Operations__
```
⎹\⎺⎺⎺⎺⎸[/home/boba/coding-projects/DSAK/DigitalSwissArmyKnife]
⎹⎻\⎻⎻⎻⎸[boba@alpha]
⎹⎼⎼\⎼⎼⎸[>>>]$ value = False
⎹\⎺⎺⎺⎺⎸[/home/boba/coding-projects/DSAK/DigitalSwissArmyKnife]
⎹⎻\⎻⎻⎻⎸[boba@alpha]
⎹⎼⎼\⎼⎼⎸[>>>]$ bool(value)
False
```

<br>

__Making a Function__
```
⎹\⎺⎺⎺⎺⎸[/home/boba/coding-projects/DSAK/DigitalSwissArmyKnife]
⎹⎻\⎻⎻⎻⎸[boba@alpha]
⎹⎼⎼\⎼⎼⎸[>>>]$ def hello():
⎹⎼⎼⎼\⎼⎸[...]*   print('Hello, World!')
⎹⎼⎼⎼\⎼⎸[...]* 
⎹\⎺⎺⎺⎺⎸[/home/boba/coding-projects/DSAK/DigitalSwissArmyKnife]
⎹⎻\⎻⎻⎻⎸[boba@alpha]
⎹⎼⎼\⎼⎼⎸[>>>]$ hello()
Hello, World!
⎹\⎺⎺⎺⎺⎸[/home/boba/coding-projects/DSAK/DigitalSwissArmyKnife]
⎹⎻\⎻⎻⎻⎸[boba@alpha]
⎹⎼⎼\⎼⎼⎸[>>>]$ 
```

<br>

__Basic Math__
```
⎹\⎺⎺⎺⎺⎸[/home/boba/coding-projects/DSAK/DigitalSwissArmyKnife]
⎹⎻\⎻⎻⎻⎸[boba@alpha]
⎹⎼⎼\⎼⎼⎸[>>>]$ result = 2+2
⎹\⎺⎺⎺⎺⎸[/home/boba/coding-projects/DSAK/DigitalSwissArmyKnife]
⎹⎻\⎻⎻⎻⎸[boba@alpha]
⎹⎼⎼\⎼⎼⎸[>>>]$ print('2 plus 2 is',result,'quick maths')
2 plus 2 is 4 quick maths
⎹\⎺⎺⎺⎺⎸[/home/boba/coding-projects/DSAK/DigitalSwissArmyKnife]
⎹⎻\⎻⎻⎻⎸[boba@alpha]
⎹⎼⎼\⎼⎼⎸[>>>]$ 
```

<br><br>

## Using Commands

DSAK is filled to the brim with useful commands you can find in your shell. You can even [add your own!](cmdpkg.md) Here are some of the essential commands and their usage examples:

### `ls`
__Description:__ Command that allows you to view files in a directory

__Command(s) that do the same thing:__ `dir`

__Usage Examples:__

```
⎹\⎺⎺⎺⎺⎸[/home/boba/coding-projects/DSAK/DigitalSwissArmyKnife]
⎹⎻\⎻⎻⎻⎸[boba@alpha]
⎹⎼⎼\⎼⎼⎸[>>>]$ ls()
⎹  🗁  ⎸Contents of directory /home/boba/coding-projects/DSAK/DigitalSwissArmyKnife:
dsakvenv  LICENSE  README.md  screenshot1.png  src  start
```

```
⎹\⎺⎺⎺⎺⎸[/home/boba/coding-projects/DSAK/DigitalSwissArmyKnife]
⎹⎻\⎻⎻⎻⎸[boba@alpha]
⎹⎼⎼\⎼⎼⎸[>>>]$ ls('-l')
⎹  🗁  ⎸Contents of directory /home/boba/coding-projects/DSAK/DigitalSwissArmyKnife:
total 372
drwxrwxr-x. 1 boba boba     56 Mar 28 09:17 dsakvenv
-rw-r--r--. 1 boba boba  35149 Mar 27 13:39 LICENSE
-rw-r--r--. 1 boba boba   3970 Apr  9 21:10 README.md
-rw-r--r--. 1 boba boba 335149 Apr  9 21:05 screenshot1.png
drwxrwxr-x. 1 boba boba     20 Apr  9 21:05 src
-rwxrwxr-x. 1 boba boba     43 Apr  6 21:40 start
```

### `cd`