website_lst = []
username_lst = []
password_lst = []

def addPassword(website, email_username, password):
    website_lst.append(website)
    username_lst.append(email_username)
    password_lst.append(password)

    print("password successfully added")

def viewPassword():
    for i in range(len(password_lst)):
        print(f'website: {website_lst[i]}, username: {username_lst[i]}, password: {password_lst[i]}')




