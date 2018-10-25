"""
Print 4X4 similar to this :
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
"""
def call2(f):
    f()
    f()
    
def call4(f):
    call2(f)
    call2(f)

def pipes():
    print('|' + ' '*9, end='')

def dashes():    
    print('+ ' + '- '*4, end='')

def print_pipes2():
    call2(pipes)

def print_pipes4():
    call2(print_pipes2)
    print('|')  

def print_dashes2():
    call2(dashes)

def print_dashes4():
    call2(print_dashes2)
    print('+')    

def print_pipesbox():
    call4(print_pipes4)
    
def print_row4():
    print_dashes4()
    print_pipesbox()
    
def print_box():
    call4(print_row4)
    print_dashes4()
    
print_box()
