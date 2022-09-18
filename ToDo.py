import json
import os

myList = []
# Json file read 
myFile = os.path.dirname(__file__)
path_file = os.path.join(myFile, "myList.json")
if os.path.exists(path_file):
    with open(path_file, "r") as f:
        myList = json.load(f)
else:
    myList = []
######################################################
print("\n-------------------- LISTE ------------------------\n")

show = """
Choose an option:

    \t1: Add an item
    \t2: Delete an item
    \t3: Show the list
    \t4: Empty the  list
    \t5: close
"""


# Function remove
def removed(str):
    if choice_1 == "Y":
        remove_item = input("remove your item: ").capitalize()
        if remove_item in myList:
            myList.remove(remove_item)
            print(
                f"The item {remove_item} has just been removed. \nThe list now contains the following items: {myList}")
    else:
        print("Okay!")


print(show)  # Show the options

while True:

    choice = input("Your choice 👉🏾 : ")

    if choice == "1":
        add_item = input("Add an item: ").capitalize()
        if add_item in myList:
            print("The item is already in the myList.")
        else:
            myList.append(add_item)
            myList.sort()
            print(f"The item {add_item} has been successfully added.")

    elif choice == "2":
        remove_item = input("Delete an item: ").capitalize()
        if remove_item in myList:
            myList.remove(remove_item)
            print(
                f"The iten {remove_item} has just been removed."
                f"\nThe myList now contains the following items: {myList}")
        else:
            print(
                f"The item {remove_item} is not in your list. \nYour list contains the following elements: {myList}")
            choice_1 = input("Do you want to remove an item from the list again? (Y/N) \n").capitalize()
            removed(choice_1)  # Function remove

    elif choice == "3":
        if myList:
            print("\nYour list: \n ")
            for index, element in enumerate(myList, 1):
                print(f"{index}. {element} \n ")
        else:
            print("Your list contains no items.")

    elif choice == "4":
        myList.clear()
        print("The list has just been emptied. ")

    elif choice == "5":
        # Write in the Json's file
        with open(path_file, "w") as f:
            json.dump(myList, f)
        ##########################################
        print("Goodbye !!")
        exit()

    else:
        print("Please enter a valid choice !!")
