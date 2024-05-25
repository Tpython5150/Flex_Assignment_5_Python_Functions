'''
The Shopping List Maker 2 Task 1

The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.
Task 2: Include a feature tp remove items from the list.
Task 3: Add a function that prnts out the entire list in a formatted way.

'''

shopping_list = ['Apples', 'Bananas', 'Bread', 'Steak', 'Chicken', 'Toothpaste', 'Mouthwash']
modified_list = []

def updated_list():
    print(f"Here is the original copy: {shopping_list}")     
        
def shopping_cart():
    while True:  
        print("\nShopping Cart")
        print("1. View Shopping Cart")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Updated List")
        print("5. Exit")
        choice = input("Enter your choice: ")        
        
        if choice == '1':
            print(f"Here's what we've got so far: {shopping_list}")
            
        elif choice == '2':
            new_item = input("Enter new item: ")
            modified_list.append(new_item)
            print(f"{new_item} has been added to the modified_list.")
            
        elif choice == '3':
            remove_item = input("Enter the item you want to remove: ")
            updated_list = modified_list + shopping_list
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} has been removed from the shopping list. ")
            else:
                print(f"{remove_item} is not in the updated list. Here is the final list: {updated_list}")
        
        elif choice == '4': 
            updated_list = shopping_list + modified_list
            print(f"Here is the updated list in the {updated_list}") 
                        
        elif choice == '5':
            print("That's all folks!")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
shopping_cart()

            