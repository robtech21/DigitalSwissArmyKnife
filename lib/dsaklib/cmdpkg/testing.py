'''INFO
Name:        testing
Description: A blank slate command set used for testing
Author(s):   Robert Furr
Year:        2021

This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

# This should not be edited. So if you edit this and put it in a PR, I will decline it.

line1 = '━'
line2 = '┃'
corn1 = '┏'
corn2 = '┓'
corn3 = '┗'
corn4 = '┛'
plusl = '╋'
rightl= '┣'
leftl = '┫'
nl    = "\n"
# ┏
# ┗
# ┓
# ┛
# ┣
# ┫
# ┳
# ┻
# ╋

test_table = ('''

┏━┳━┓
┃a┃b┃
┣━╋━┫
┃c┃d┃
┗━┻━┛
''')

def table():

  print(\
    corn1+line1+corn2+nl+\
    line2+"E"+line2+nl+\
    corn3+line1+corn4\
    )