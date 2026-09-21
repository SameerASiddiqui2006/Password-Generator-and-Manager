import sqlite3

def init_db():
    connection_obj = sqlite3.connect('psdmanager.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        password_id INTEGER PRIMARY KEY,
        website text, 
        email text,
        password text
    )
    """
    )

    connection_obj.commit()
    connection_obj.close()

def get_password():
    connection_obj = sqlite3.connect('psdmanager.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("SELECT * FROM passwords")

    records = cursor_obj.fetchall()
    return records


def insertDB(website, email_username, password):
    connection_obj = sqlite3.connect('psdmanager.db')
    cursor_obj = connection_obj.cursor()

    insert_values = (website, email_username, password)
    insert_query = "INSERT INTO passwords (website, email, password) VALUES (?, ?, ?)"

    cursor_obj.execute(insert_query, insert_values)

    connection_obj.commit()
    connection_obj.close()

def searchDB(searchInput):
    connection_obj = sqlite3.connect('psdmanager.db')
    cursor_obj = connection_obj.cursor()
    
    search_query = ("SELECT * FROM passwords WHERE website = ?")
    search_value = (searchInput,)

    cursor_obj.execute(search_query, search_value)
    results = cursor_obj.fetchall()

    return results

def removeDB (deleteInput):
    connection_obj = sqlite3.connect('psdmanager.db')
    cursor_obj = connection_obj.cursor()
    
    delete_values = (deleteInput,)
    delete_query = "DELETE FROM passwords WHERE password_id = ?"
    cursor_obj.execute(delete_query, delete_values)
    
    connection_obj.commit()
    connection_obj.close()