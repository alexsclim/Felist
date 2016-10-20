from flask import Flask
# from flaskext.mysql import MySQL

# mysql = MySQL()
app = Flask(__name__)
from app import views

# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
# app.config['MYSQL_DATABASE_DB'] = 'Felist'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

@app.route("/")
def index():
  return render_template('index.html')

# if __name__ == "__main__":
#     app.run()
