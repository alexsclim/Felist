class QueryService:

  def __init__(self, cursor):
    self.cursor = cursor

  def get_members_from_team(self, team_id):
    data = self.cursor.execute("SELECT * from Member where teamId =%s", [team_id])
    members = self.cursor.fetchall()
    return members

  def get_last_team_id(self):
    data = self.cursor.execute("SELECT * from Team")
    return data

  def get_teams(self):
    data = self.cursor.execute("SELECT * from Team")
    teams = self.cursor.fetchall()
    return teams

  def get_members(self):
    data = self.cursor.execute("SELECT * from Member")
    members = self.cursor.fetchall()
    return members

  def username_exists(self, username):
    data = self.cursor.execute("SELECT * FROM User WHERE username = %s", [username])
    return data

  def get_hashed_password(self, username):
    data = self.cursor.execute("SELECT * FROM User WHERE username = %s", [username])
    hashed_password = self.cursor.fetchall()[0]['encryptedPassword']
    return hashed_password

  def create_user(self, conn, username, hashed_password):
    self.cursor.execute("INSERT INTO User(username, encryptedPassword) VALUES (%s, %s)", [username, hashed_password])
    conn.commit()
    return

  def get_current_user_teams(self, username):
    data = self.cursor.execute("SELECT name FROM Team WHERE username= %s", [username])
    teams = self.cursor.fetchall()
    return teams

  def create_team(self, conn, team_id, team_name, practice_cost, username, city, province):
    data = self.cursor.execute("INSERT INTO Team(teamId, name, practiceCost, username, regionCity, regionProvince) VALUES (%s, %s, %s, %s, %s, %s)", [team_id, team_name, practice_cost, username, city, province])
    conn.commit()
    return

  def search_teams(self, search):
    sql = 'Select * from Team where name like %s'
    args = ['%'+search+'%']
    data = self.cursor.execute(sql, args)
    teams = self.cursor.fetchall()
    return teams

  def delete_member(self, conn, memberId):
    data = self.cursor.execute("Delete from Member WHERE memberId = %s", [memberId])
    conn.commit()
    return
