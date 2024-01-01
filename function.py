import os

contacts = {}
def create_contact():
    while True:
        name = input("Please enter your name: ").strip().lower()
        email = input("Please enter your email: ").strip().lower()
        str_number = input("Please enter your number:").strip()
        if str_number.isdigit() and len(str_number) == 11:
            try:
                number = int(str_number)
            except ValueError:
                print("Please enter a valid phone number")
                continue
            contacts[name] = {"name": name, 'email': email, 'phone': number}
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{name}'s contact has been saved")
            break
        else:
            print("Invalid number.")
    return contacts

def view_contact():
    name = input("please enter a name: ").lower()
    contact = contacts.get(name)
    if contact is not None:
        print(f"name: {contact['name']}")
        print(f"Email: {contact['email']}")
        print(f"Phone: {contact['phone']}")
        print("\n")
    else:
        print("contact does not exit")
    

def list_all_contact():
    if contacts is not None:
        for _, contact in contacts.items():
            print(f"{contact['name']}: ")
            print(f"Name: {contact['name']}")
            print(f"Email: {contact['email']}")
            print(f"Phone: {contact['phone']}")
            print("\n")
    else:
        print("No Contacts")
    

def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        user_input = input("Choose what you want to update: ")
        if user_input == "name":
            new_name = input("enter new name: ")
            contacts[name]["name"] = [new_name]
            print("Name has been updated")

        elif user_input == "email":
            new_email = input("enter new email: ")
            contacts[name]["email"] = [new_email]
            print("Email has been updated ")

        elif user_input == "phone":
            new_phone = input("enter new number: ")
            contacts[name]["phone"] = [new_phone]
            print("phone has been updated")
    else:
        print("contact does not exist")
    
    

def delete():
    name = input("Enter the name of the contact you wish to delete: ")
    if name in contacts:
        user_input = input(f"Are you sure you want to delete {name} contact details (y/n) ")
        if user_input == "y":
            del contacts[name]
            print(f"{name} contact has successfully been deleted")
        elif user_input == "n":
            exit()
        else:
            print("enter a valid option")
    
    



