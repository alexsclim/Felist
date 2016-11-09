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

  def get_regattas(self):
    data = self.cursor.execute("SELECT * from Regatta")
    regatta = self.cursor.fetchall()
    return regatta

  def get_teams(self):
    data = self.cursor.execute("SELECT * from Team")
    teams = self.cursor.fetchall()
    return teams

  def get_team_by_id(self, team_id):
    data = self.cursor.execute("SELECT * FROM Team WHERE teamId=%s", [team_id])
    team = self.cursor.fetchall()
    return team

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
    data = self.cursor.execute("SELECT * FROM Team WHERE username= %s", [username])
    teams = self.cursor.fetchall()
    return teams

  def create_team(self, conn, team_id, team_name, practice_cost, username, city, province):
    data = self.cursor.execute("INSERT INTO Team(teamId, name, practiceCost, username, regionCity, regionProvince) VALUES (%s, %s, %s, %s, %s, %s)", [team_id, team_name, practice_cost, username, city, province])
    conn.commit()
    return

  def search_regattas(self, search):
    sql = 'Select * from Regatta where name like %s'
    args = ['%'+search+'%']
    data = self.cursor.execute(sql, args)
    regattas = self.cursor.fetchall()
    return regattas

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

  def sort_member_names_by_team_asc(self, team_id):
    data = self.cursor.execute("SELECT * from Member where teamId=%s order by memberName asc", [team_id])
    members = self.cursor.fetchall()
    return members

  def sort_member_names_asc(self):
    data = self.cursor.execute("SELECT * from Member order by memberName asc")
    members = self.cursor.fetchall()
    return members

  def sort_member_names_by_team_desc(self, team_id):
    data = self.cursor.execute("SELECT * from Member where teamId=%s order by memberName desc", [team_id])
    members = self.cursor.fetchall()
    return members

  def sort_member_names_desc(self):
    data = self.cursor.execute("SELECT * from Member order by memberName desc")
    members = self.cursor.fetchall()
    return members

def sort_paddle_members_asc(self):
    data = self.cursor.execute("SELECT * from PaddleOwns order by memberId asc")
    paddles = self.cursor.fetchall()
    return paddles

def sort_paddle_members_desc(self):
    data = self.cursor.execute("SELECT * from PaddleOwns order by memberID desc")
    paddles = self.cursor.fetchall()
    return paddles

def get_paddles(self):
    data = self.cursor.execute("SELECT * from PaddleOwns")
    paddles = self.cursor.fetchall()
    return paddles

def get_paddles_from_member(self, member_id):
    data = self.cursor.execute("SELECT * from PaddleOwns where memberID=%s", [member_id])
    paddles = self.cursor.fetchall()
    return paddles

def get_member_from_id(self, member_id):
    data = self.cursor.execute("SELECT * from Member where memberID=%s", [member_id])
    member = self.cursor.fetchall()
    return member
