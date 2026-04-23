#Import inventory class from the inventory module
from inventory import Inventory

#CLI entry point for the Inventory Management System
def manage_inventory():

    #Create inventory instance (to handle API communication)
    inventory = Inventory()
    
    while True:
        #Display MENU Options
        print("\n------------Inventory Management System------------")
        print("1. Add New Item")
        print("2. View Inventory Details")
        print("3. Update Item's Price and Stock")
        print("4. Delete Item")
        print("5. Get Item Details Remotely")
        print("6. Exit")
        print("----------------------------------------------------\n")

        #Get user selection
        choice = input("Choose an option: ")

        #CREATE operation
        if choice == "1":
            inventory.add_new_item()

        #READ operation
        elif choice == "2":
            inventory.view_inventory_details()

        #UPDATE operation
        elif choice == "3":
            inventory.price_stock_update()

        #DELETE operation
        elif choice == "4":
            inventory.delete_item()

        #EXTERNAL API lookup
        elif choice == "5":
            inventory.get_remote_item()

        #EXIT program -> Exit loop and stop option display
        elif choice == "6":
            print("Exiting the system...")
            break

        #Handle invalid input
        else:
            print("Invalid option. Please try again.")

#Run CLI only when file is executed directly
if __name__ == "__main__":
    manage_inventory()