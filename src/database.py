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

def insertDB(website, email_username, password):
    connection_obj = sqlite3.connect('psdmanager.db')
    cursor_obj = connection_obj.cursor()

    insert_values = (website, email_username, password)
    insert_query = "INSERT INTO passwords (website, email, password) VALUES (?, ?, ?)"

    cursor_obj.execute(insert_query, insert_values)

    connection_obj.commit()
    connection_obj.close()
