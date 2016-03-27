my_foods = ['pizza', 'falafel', 'carrot cake', 'sushi', 'thai']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice_cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

print("The first 3 items in the list are:")
print(my_foods[:4])

print("Three items from the middle of the list are")
print(my_foods[2:5])

print("The three last items in the list are:")
print(my_foods[-3:])

for food in my_foods:
    print("I really love, " + food + ".")
