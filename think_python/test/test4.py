"""
Print this:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""

def pipes():
    print('|' + ' '*9 + '|' + ' '*9 + '|')

def plus_dashes():
    print('+ ' + '- '*4 + '+ ' + '- '*4 + '+')

def print_box():
    plus_dashes()
    pipes()
    pipes()
    pipes()
    pipes()
    plus_dashes()
    pipes()
    pipes()
    pipes()
    pipes()
    plus_dashes()
    

print_box()
