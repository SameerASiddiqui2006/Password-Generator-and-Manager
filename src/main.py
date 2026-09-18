import password_generator

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
                addPassword()
            elif (choice == 3):
                viewPassword()
            elif (choice == 4):
                break
            else:
                print("Invalid Input, Please Enter valid number between 1 - 4")
        except ValueError:
            print("Invalid Input, Please Enter valid number between 1 - 4")
        


main()