def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name_2(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician_2 = get_formatted_name('jimi', 'hendrix')
print(musician)

musician_2 = get_formatted_name_2('john', 'hooker', 'lee')
print(musician_2)
