import database

website_lst = []
username_lst = []
password_lst = []

def addPassword(website, email_username, password):
    database.insertDB(website, email_username, password)

    print("password successfully added")

def search(searchInput):
    if searchInput in website_lst:
        indices = [index for index, value in enumerate(website_lst) if value == searchInput]
        
        for index in indices:
            print(f'username: {username_lst[index]}, password: {password_lst[index]}')
    else:
        print(f'{searchInput} was not found')



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
    
    
    

