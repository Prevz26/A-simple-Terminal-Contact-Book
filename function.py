import os
import json 

def load_contacts():
    try:
        with open("contact.json", "r") as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Contact Empty.")
    return contacts

def save_contacts(contacts):
    try:
        with open("contact.json", "w") as file:
            json.dump(contacts, file, indent=4)
    except (FileNotFoundError):
        print("File not found")


def create_contact():
    while True:
        contacts = load_contacts()
        Name = input("Please enter your name: ").strip().lower()
        Email = input("Please enter your email: ").strip().lower()
        str_number = input("Please enter your number:").strip()
        if str_number.isdigit() and len(str_number) == 11:
            try: 
                Number = int(str_number)
            except ValueError:
                print("Please enter a valid phone number")
                continue
            if Name in contacts:
                print("name already exits")
                continue
            else:
                contacts[Name] = {"Name": Name, "Email": Email, "Phone": Number}
                save_contacts(contacts)                
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Name}'s contact has been saved")
            break
        else:
            print("Invalid number.")
    return contacts

def view_contact(contacts):
    contact = load_contacts()

    name = input("please enter a name: ").lower()
    contact = contacts.get(name) 
    if contact is not None:
        print(f"name: {contact['Name']}")
        print(f"Email: {contact['Email']}")
        print(f"Phone: {contact['Phone']}")
        print("\n")
    else:
        print("contact does not exit")
    

def list_all_contact():
    contact = load_contacts()
    if contact:
        print("Contacts:")
        for value in contact.values():
            print(f"Name: {value.get('Name', 'N/A')}")
            print(f"Email: {value.get('Email', 'N/A')}")
            print(f"Phone: {value.get('Phone', 'N/A')}")
            print("\n")
    else:
        print("No Contacts")


def update_contact(contacts):
    contacts = load_contacts()
    old_name = input("Enter the name of the contact you want to update: ")
    if old_name in contacts:
        user_input = input("Choose what you want to update: ")
        new_name = old_name 
        if user_input == "name":
            new_name = input("enter new name: ")
            contacts[new_name] = contacts.pop(old_name)
            contacts[new_name]["Name"] = new_name
            print("Name has been updated")
            save_contacts(contacts)

        elif user_input == "email":
            new_email = input("enter new email: ")
            contacts[new_name]["Email"] = new_email
            print("Email has been updated ")
            save_contacts(contacts)

        elif user_input == "phone":
            new_phone = input("enter new number: ")
            contacts[new_name]["Phone"] = new_phone
            print("phone has been updated")
            save_contacts(contacts)
    else:
        print("contact does not exist")
    


def delete(contacts):
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
    
if __name__ == "__main__":
    print("This file is a function")



