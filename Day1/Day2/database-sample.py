import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('Create table If not exists users (user_id integer PRIMARY KEY autoincrement , first_name text not null, last_name text not null)')

def new_user(c,firstname,lastname):
    c.execute("insert into users(first_name,last_name) values ('"+firstname+"','"+lastname+"')")
    conn.commit()

def get_record():
    #new_user(c,"John","Doe")
    print("Enter firstname")
    fn=input()

    print("Enter lastname")
    ln=input()

    new_user(c,fn,ln)


print("Select the option:\n 1.Show all rows\n 2.Insert record")
try:
    selection = input()
    if selection == "1":
        c.execute('select * from users')
    if selection == "2":
        get_record()
        c.execute('select * from users')
except Exception:
    print("invalid input")

'''
c.execute('insert into users(id,name,family) values (1,"Kaur","chahal")')
c.execute('insert into users(id,name,family) values (2,"Kaur","chahal")')
c.execute('insert into users(id,name,family) values (3,"Kaur","chahal")')
c.execute('select * from users')'''
rows = c.fetchall()

for row in rows:
    print(row)
    