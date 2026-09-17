import secrets

def passwordGenerator():
    password = secrets.token_hex(10)
    print(password)

    while True:

        try:
            print("Do you want to use this password?")
            print("1 for yes")
            print("2 for no")
            choice = int(input())
            if choice == 1:
                print("Would you like to save this password? ")
                print("1 for yes")
                print("2 for no")
                choice = int(input())

                if choice == 1:
                    addPassword()
                    break
                elif choice == 2:
                    print("Program will quit now")
                    break
            elif choice == 2:
                print("Program will quit now")
                break
        except ValueError:
            print("Please provide valid input, either 1 or 2 only")


