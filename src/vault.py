import database

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
    database.updateRecordDB(updateInput, updateChoice, newValueInput)

    
    
    

