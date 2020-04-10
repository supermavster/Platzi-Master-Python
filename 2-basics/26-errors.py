# -*- codign: utf-8 -*-

countries = {
    'colombia':  49,
    'mexico': 122,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

def run():
    while True:
        country = str(input("Give a country:\n")).lower()
        try:
            print(" The count of people of {} is {}".format(country, countries[country]))
        except KeyError: #KeyError: 'hola'
            print("We don't have the data of {} is a KeyError".format(country))
            addCountry(country)


def addCountry(country):
    print("Do you want add this country: {} to the list?".format(country))
    option = int(input("1 -> Yes or 0 -> No\n"))
    if (option == 1):
        manyPeople = int(input("Give a size of the population of this country\n"))
        countries[country] = manyPeople

if __name__ == "__main__":
    run()