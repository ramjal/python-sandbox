birthday_dictionary = {
	"Albert Einstein": "14Mar1879",
	"Benjamin Franklin": "17Jan1706",
    "Ramin Jalali": "18Apr1962",
}

name = input("Who's birthday do you want to look up?\n")

if name in birthday_dictionary:
    print(birthday_dictionary[name])
