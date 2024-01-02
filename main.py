import function
import os
def main():
    print("WELCOME TO CONTACT BOOK\n")

    while True:
        contacts = function.load_contacts()
        print("1. Create a new contact\n")
        print("2. View an existing contact\n")
        print("3. List all existing contacts\n")
        print("4. Update an existing contact\n")
        print("5. Delete an existing contact\n")
        print("6. Exit\n")
        
        choice = input( "Enter your choice: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                function.create_contact()
            elif choice == 2:
                function.view_contact(contacts)
            elif choice == 3:
                function.list_all_contact()
            elif choice == 4:
                function.update_contact(contacts)
            elif choice == 5:
                function.delete(contacts)
            elif choice == 6:
                break
        else:
            print("Enter a valid choice")
            
if __name__ == "__main__":
    main()