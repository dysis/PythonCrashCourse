def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    :param unprinted_designs:
    :param completed_models:
    :return:
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)



def show_completed_models(completed_models):
    """
    Show all the models that were printed.
    :param completed_models:
    :return:
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted =  ['iphone case', 'robot pendant', 'dodecahedron']
done = []

# Using [:] sends a copy of the list so the original doesn't get modified
print_models(unprinted[:], done)
show_completed_models(done)

print(unprinted)
print(done)