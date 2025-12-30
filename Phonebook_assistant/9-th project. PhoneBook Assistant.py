def main():
    contacts = {}
    meeting = "Hello! How can I help you?(Write help to see all commands)"
    print(meeting)
    while True:
        choosing = input("Enter a command: ")
        answer = choosing.split()

        command = answer[0].lower()

        if command in ["exit", "close"]:
           print("Okay. Goodbye!")
           break
        
        elif command == "add":
            if len(answer) != 3:
                print("Usage: <name> <phone>")
                continue
            name = answer[1]
            phone = answer[2]
            contacts[name] = phone
            print(f"The contact {name} was successfully added!")
        
        elif command == "change":
            if len(answer) != 3:
                print("Usage: <name> <new_phone>")
                continue
            name = answer[1]
            new_phone = answer[2]
            
            if name in contacts:
                contacts[name] = new_phone
                print("Your phone was successfully updated")
                continue
            else:
                print("No contacts were found.")
                
           
        elif command == "all":
            if not contacts:
                print("No contacts were found.")
            else:
                print("All contacts:")
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
        
        elif command == "phone":
            if len(answer) != 2:
                print("Usage: <name>")
                continue
            name = answer[1]
            if name in contacts:
                print(f"Here is the phone of {name}: {contacts[name]}")
                continue
            else:
                print("No contacts were found.")

        elif command == "help":
            print("Here are all commands, that you can use:\nadd\nchange\nall\nphone\nhelp")
            continue

        else:
            print("Unknown command")
            continue


if __name__ == "__main__":
    main()

