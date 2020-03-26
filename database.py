import sqlite3

#establish connection with database
with sqlite3.connect('User_info.db') as db:
    cursor=db.cursor()

#create table user
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_info(
user_name VARCHAR(20) NOT NULL,   
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL,
phone VARCHAR(20) NOT NULL,
email VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL
)
""")

db.commit()
