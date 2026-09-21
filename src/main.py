import password_generator
import vault
import database

def main():
    database.init_db()
    
    while True:
        print("----- Password Generator and Manager -----")
        print("----- 1: Password Generator -----")
        print("----- 2: Add Password -----")
        print("----- 3: Search -----")
        print("----- 4: View Password -----")
        print("----- 5: Delete Password -----")
        print("----- 6: Update Password -----")
        print("----- 7: Quit Program -----")

        try: 
            choice = int(input())

            if (choice == 1):
                password_generator.passwordGenerator()
            elif (choice == 2):
                print("What is the website where this password will be used? ")
                website = input()
                print("What is the Username / Email associated with this password? ")
                email_username = input()
                print("What is the password? ")
                password = input()
                vault.addPassword(website, email_username, password)
            elif (choice ==3):
                print("What website do you want to search the password for?")
                searchInput = input()
                vault.search(searchInput)
            elif (choice == 4):
                vault.viewPassword()
            elif(choice == 5):
                vault.viewPassword()
                print("Enter the prefix number you want to delete: ")
                deleteInput = int(input())
                vault.deleteRecord(deleteInput)
            elif (choice == 6):
                vault.viewPassword()
                print("Enter the prefix number you want to update: ")
                updateInput = int(input())

                print("What do you want to update (website, username/email or password)")
                updateChoice = input()

                print("What's the new value? ")
                newValueInput = input()

                vault.updatePassword(updateInput, updateChoice, newValueInput)
            elif (choice == 7):
                print("Are you sure you want to quit (Y/N)")
                quitInput = input()

                if quitInput.lower() == "y":
                    break
                elif quitInput.lower() == "n":
                    continue
                else:
                    print("Please type valid input")
            else:
                print("Invalid Input, Please Enter valid number between 1 - 7")
        except ValueError:
            print("Invalid Input, Please Enter valid number between 1 - 7")
        
main()