#!venv/bin/python
import string, random
from app import app
from app import mysql
from werkzeug.security import generate_password_hash, check_password_hash

randomUsername = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

randomPassword = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
print randomPassword
encryptedPassword = generate_password_hash(randomPassword)

conn = mysql.connect()
cursor = conn.cursor()

lastId = cursor.execute("SELECT * FROM Admin");
newId = lastId + 1

cursor.execute("INSERT INTO Admin(adminId, username, encryptedPassword) VALUES(%s, %s, %s)", (newId, randomUsername, encryptedPassword))
conn.commit()
