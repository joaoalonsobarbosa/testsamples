import os
import sockets
import mysql.connector as sql

access_key = 'testpassword'
access_key_id = 'fakeID123456789'

# root
user_input = input('Enter command: ')
os.system(user_input)

# infinite loop
while true:
    print("Hello")

# sql injection

conn = sql.connect(
    host="localhost",
    user="abid",
    password="12345",
    database="vulnerable_DB"
)

uName = getRequestString("username");
uPass = getRequestString("userpassword");

sql = 'SELECT * FROM Users WHERE Name ="' + uName + '" AND Pass ="' + uPass + '"'

cursor = conn.cursor()
cursor.execute(sql)


# Test os.command
def backup_file(filename):
    os.system(f"tar -czf /backups/{filename}.tar.gz {filename}")

backup_file("important.txt; rm -rf /")


#XSS

from flask import Flask, request

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name', '')
    return f'<h1>Hello, {name}!</h1>'  # Vulnerable to XSS

# Attacker could use: /?name=<script>alert('XSS')</script>


# Path Traversal
def get_file_content(filename):
    with open(f'/var/www/files/{filename}', 'r') as f:
        return f.read()

# Vulnerable usage
#content = get_file_content('../../../etc/passwd')
