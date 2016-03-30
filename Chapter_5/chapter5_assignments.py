alien_colour = 'blue'

if alien_colour == 'green':
    print("My alien is green! You got 5 points")

if alien_colour == 'blue':
    print("My alien is blue! You got 5 points")

if alien_colour =='green':
    print("You have just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points for shooting the alien!")

if alien_colour == 'green':
    print("You just earned 5 points!")
elif alien_colour == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")


age = 40

if age < 2:
    print("You are still a baby!")
elif age < 4:
    print("You are a toddler!")
elif age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are an adult!")
else:
    print("You are a senior!")


fruit = ['apple', 'orange', 'banana']

if 'apple' in fruit:
    print("You love apples!")
if 'orange' in fruit:
    print("Oranges are great as well!")
if 'blueberry' in fruit:
    print("Are blueberries the best fruit ever?")