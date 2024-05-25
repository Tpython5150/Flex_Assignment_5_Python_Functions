
'''
The Shopping List Maker 2 Task 1

The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.
Task 2: Include a feature tp remove items from the list.
Task 3: Add a function that prnts out the entire list in a formatted way.

'''

shopping_list = ['Apples', 'Bananas', 'Bread', 'Steak', 'Chicken', 'Toothpaste', 'Mouthwash']


def shopping_cart():
    print("\nShopping List:")
    for item in shopping_list:
        print(f"- {item}")
        
def add_item():
    new_item = input("Enter the item you want to add: ")
    shopping_list.append(new_item)
    print(f"'{new_item}' has been added to the shopping list.")


def remove_item():
    item_to_remove = input("Enter the item you want to remove: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        print(f"'{item_to_remove}' has been removed from the shopping list.")
    else:
        print(f"'{item_to_remove}' is not in the shopping list!")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Print Shopping List")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            shopping_cart()
        elif choice == '4':
            print("That's all folks!")
            break  
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()


