def header():
    print("Country Application")
    print("Command Menu")
    print("view --> View country name")
    print("add --> Add a country")
    print("delete --> Delete a country")
    print("exit --> Exit application")
    print()

def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country codes:"
    for code in codes:
        codes_line += code + " "
    print(codes_line)

def view(countries):
    display_codes(countries)
    code = input("Enter country code:   ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name :   {name}. \n")
    else:
        print("There is no country with that code")

def add(countries):
    code = input("Enter aa country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code. \n")
    else:
        name = input("Enter country name:   ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added. \n")

def delete(countries):
    code = input("Enter country code:   ")
    code =  code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted")
    else:
        print("There is no country with that code. \n")

def main():
    countries = {"GB": "England","MX": "Mexico", "FR": "France"}

    header()

    while True:
        command = input("Command:  ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "delete":
            delete(countries)
        elif command == "exit":
            break
        else:
            print("Not a valid command, please try again. \n")

if __name__ == "__main__":
    main()




