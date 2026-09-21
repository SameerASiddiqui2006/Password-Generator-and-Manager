import database

website_lst = []
username_lst = []
password_lst = []

def addPassword(website, email_username, password):
    database.insertDB(website, email_username, password)

    print("password successfully added")

def search(searchInput):
    results = database.searchDB(searchInput)

    if len(results) == 0:
        print("No result found")
    else:
        for row in results:
            print(f'{row[0]}. website: {row[1]}, email: {row[2]}, password: {row[3]}')

def viewPassword():
    records = database.get_password()

    for row in records:
        print(f'{row[0]}. website: {row[1]}, email: {row[2]}, password: {row[3]}')



def deleteRecord(deleteInput):
    try:
        database.removeDB(deleteInput)
        print("Record successfully deleted")
    except IndexError :
        print("Please enter a valid prefix")

def updatePassword(updateInput, updateChoice, newValueInput):
    try:
        if updateChoice.lower() == "website":
            website_lst[updateInput] = newValueInput
        elif updateChoice.lower() == "username" or updateChoice.lower() == "email" or updateChoice.lower() == "username/email":
            username_lst[updateInput] = newValueInput
        elif updateChoice.lower() == "password":
            password_lst[updateInput] = newValueInput
        else:
            print("Please enter valid value")
            return

        print("Value successfully updated")
    except IndexError :
        print("Please enter a valid prefix")
    
    
    

