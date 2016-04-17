def make_shirt(text = "I Love Python!", size = 'large'):
    print("\nYour t-shirt will be size " + size + " and will say " + text + ".")

make_shirt()
make_shirt(size = 'medium')
make_shirt(text = "I Love Games!")


def describe_city(city, country = 'canada'):
    print("\n" + city.title() + " is in " + country.title() + ".")

describe_city('toronto')
describe_city('vancouver')
describe_city('lisbon', country = 'portugal')