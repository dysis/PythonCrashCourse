users = ['admin', 'diana', 'jeff', 'molly']

if users == []:
    print("We need to find some users!")
else:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Welcome, " + user.title() + ".")


current_users = ['diana', 'jeff', 'Molly', 'phi', 'sigma']

new_users= ['phi', 'Sigma', 'clover', 'k', 'dio']

for user in new_users:
    if user.lower() in current_users:
        print("Sorry, that username is taken! Try a new username.")
    else:
        print(user.title() + ", that username is available!")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    elif number == 4:
        print(str(number) + "th")
    elif number == 5:
        print(str(number) + "th")
    elif number == 6:
        print(str(number) + "th")
    elif number == 7:
        print(str(number) + "th")
    elif number == 8:
        print(str(number) + "th")
    elif number == 9:
        print(str(number) + "th")