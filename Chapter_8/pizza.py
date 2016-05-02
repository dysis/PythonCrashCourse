def make_pizza_old(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza_old('pepperoni')
make_pizza_old('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """Summerize the pizza we are about to make."""
    print("\nWe are making a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza_size(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza_size(16,'pepperoni')
make_pizza_size(12, 'mushrooms', 'green peppers', 'extra cheese')