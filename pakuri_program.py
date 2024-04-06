from pakudex import Pakudex

def display_menu():
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")

def list_pakuri(pakudexObj):
    species_list = pakudexObj.get_species_array()
    if species_list:
        print("Pakuri In Pakudex:")
        index = 1
        for species in species_list:
            print(f"{index}. {species}")
            index += 1
    else:
        print("No Pakuri in Pakudex yet!")

def show_pakuri(pakudexObj):
    species = input("Enter the name of the species to display: ")
    stats = pakudexObj.get_stats(species)
    if stats:
        attack, defense, speed = stats
        print(f"Species: {species}")
        print(f"Attack: {attack}")
        print(f"Defense: {defense}")
        print(f"Speed: {speed}")
    else:
        print("Error: No such Pakuri!")

def add_pakuri(pakudexObj):
    if pakudexObj.get_capacity() == pakudexObj.get_size():
        print("Error: Pakudex is full!")
    else:
        species = input("Enter the name of the species to add: ")
        success = pakudexObj.add_pakuri(species)
        if success:
            print(f"Pakuri species {species} successfully added!")

def evolve_pakuri(pakudexObj):
    species = input("Enter the name of the species to evolve: ")
    success = pakudexObj.evolve_species(species)
    if success:
        print(f"{species} has evolved!")
    else:
        print("Error: No such Pakuri!")

def sort_pakuri(pakudexObj):
    pakudexObj.sort_pakuri()
    print("Pakuri have been sorted!")


def main():

    print("Welcome to Pakudex: Tracker Extraordinaire!")

    check1 = True
    PakudexCapacity = 0

    while check1:

        capacity_str = input("Enter max capacity of the Pakudex: ")

        for i in range(len(capacity_str)):
            if (capacity_str[i] == '-'):
                break

            if (capacity_str[i] >= '0' and capacity_str[i] <= '9'):
                PakudexCapacity = int(capacity_str)
                check1 = False

        if(check1 is True):
            print("Please enter a valid size.")

    pakudexObj = Pakudex(PakudexCapacity)

    print(f"The Pakudex can hold {PakudexCapacity} species of Pakuri.")


    while True:
        display_menu()
        choice = input("What would you like to do? ")
        if choice == "1":
            list_pakuri(pakudexObj)
        elif choice == "2":
            show_pakuri(pakudexObj)
        elif choice == "3":
            add_pakuri(pakudexObj)
        elif choice == "4":
            evolve_pakuri(pakudexObj)
        elif choice == "5":
            sort_pakuri(pakudexObj)
        elif choice == "6":
            print("Thanks for using Pakudex! Bye!")
            break
        else:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()