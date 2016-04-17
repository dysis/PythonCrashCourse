def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('cat', 'molly')

describe_pet('dog', 'pepe')

describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'cat', pet_name = 'molly')


def describe_pet_2(pet_name, animal_type = 'cat'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet_2('molly')
describe_pet_2('pepe', 'dog')
