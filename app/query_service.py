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

  def get_last_member_id(self):
    data = self.cursor.execute("SELECT * FROM Member")
    return data

  def get_members(self):
    data = self.cursor.execute("SELECT * from Member")
    members = self.cursor.fetchall()
    return members

  def get_member_memberName_by_id(self, member_id):
    data = self.cursor.execute("SELECT * from Member WHERE memberId=%s", [member_id])
    memberName = self.cursor.fetchall()[0]['memberName']
    return memberName

  def get_member_weight_by_id(self, member_id):
    data = self.cursor.execute("SELECT * from Member WHERE memberId=%s", [member_id])
    weight = self.cursor.fetchall()[0]['weight']
    return weight

  def get_member_height_by_id(self, member_id):
    data = self.cursor.execute("SELECT * from Member WHERE memberId=%s", [member_id])
    height = self.cursor.fetchall()[0]['height']
    return height

  def get_member_role_by_id(self, member_id):
    data = self.cursor.execute("SELECT * from Member WHERE memberId=%s", [member_id])
    role = self.cursor.fetchall()[0]['role']
    return role

  def get_member_paddle_side_by_id(self, member_id):
    data = self.cursor.execute("SELECT * from Member WHERE memberId=%s", [member_id])
    paddleSide = self.cursor.fetchall()[0]['paddleSide']
    return paddleSide

  def get_member_date_of_birth_by_id(self, member_id):
    data = self.cursor.execute("SELECT * from Member WHERE memberId=%s", [member_id])
    dateOfBirth = self.cursor.fetchall()[0]['dateOfBirth']
    return dateOfBirth

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

  def create_member(self, conn, member_id, name, weight, height, role, paddle_side, date_of_birth, team_id):
    data = self.cursor.execute("INSERT INTO Member(memberId, memberName, weight, height, role, paddleSide, dateOfBirth, teamId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [member_id, name, weight, height, role, paddle_side, date_of_birth, team_id])
    conn.commit()
    return

  def update_member_by_id(self, conn, name, weight, height, role, paddle_side, date_of_birth, member_id):
    data = self.cursor.execute("UPDATE Member SET memberName=%s, weight=%s, height=%s, role=%s, paddleSide=%s, dateOfBirth=%s WHERE memberId=%s", [name, weight, height, role, paddle_side, date_of_birth, member_id])
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
