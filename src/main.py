import password_generator
import vault

def main():
    while True:
        print("----- Password Generator and Manager -----")
        print("----- 1: Password Generator -----")
        print("----- 2: Add Password -----")
        print("----- 3: View Password -----")
        print("----- 4: Quit Program -----")

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
            elif (choice == 3):
                vault.viewPassword()
            elif (choice == 4):
                break
            else:
                print("Invalid Input, Please Enter valid number between 1 - 4")
        except ValueError:
            print("Invalid Input, Please Enter valid number between 1 - 4")
        


main()