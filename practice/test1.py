
try:
    age = int(input("How old are you?\n"))
    print("You said that you are " + str(age))    
    print("You will be 100 years old in " + str(2019 + (100 - age)))
    counter = int(input("Give me a number smaller than 10\n"))
    for i in range(counter):
        print('I love you!')
except Exception as err:
    print('There was an error: {0}'.format(err))