import sqlite3

def init_db():
    connection_obj = sqlite3.connect('psdmanager.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("""
    CREATE TABLE IF NOT EXISTS password (
        password_id INTEGER PRIMARY KEY,
        website text, 
        email text,
        password text
    )
    """
    )

    connection_obj.commit()
    connection_obj.close()