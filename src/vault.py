website_lst = []
username_lst = []
password_lst = []

def addPassword(website, email_username, password):
    website_lst.append(website)
    username_lst.append(email_username)
    password_lst.append(password)

    print("password successfully added")

def search(searchInput):
    if searchInput in website_lst:
        indices = [index for index, value in enumerate(website_lst) if value == searchInput]
        
        for index in indices:
            print(f'username: {username_lst[index]}, password: {password_lst[index]}')
    else:
        print(f'{searchInput} was not found')



def viewPassword():
    for i in range(len(password_lst)):
        print(f'{i}. website: {website_lst[i]}, username: {username_lst[i]}, password: {password_lst[i]}')

def deleteRecord(deleteInput):
    try:
        del website_lst[deleteInput]
        del username_lst[deleteInput]
        del password_lst[deleteInput]

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
    
    
    

