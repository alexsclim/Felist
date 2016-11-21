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
    regattas = self.cursor.fetchall()
    return regattas


  def get_leaderboard(self):
    data = self.cursor.execute("SELECT COUNT(resultId), name FROM RaceResult Ra, Team T WHERE Ra.teamId = T.teamId AND Ranking = 1 GROUP BY T.teamId")
    leaderboard = self.cursor.fetchall()
    return leaderboard

  def get_number_of_teams_from_leaderboard(self):
    data = self.cursor.execute("SELECT DISTINCT teamId FROM RaceResult WHERE Ranking = 1")
    numberOfTeams = self.cursor.rowcount
    return numberOfTeams

  def get_raceresults_join_team_from_regatta(self, regatta_id):
    data = self.cursor.execute("SELECT* FROM RaceResult, Team WHERE RaceResult.teamId = Team.teamId AND regattaId=%s", [regatta_id])
    raceresults = self.cursor.fetchall()
    return raceresults

  def get_average_time_from_regatta(self, regatta_id):
    data = self.cursor.execute("SELECT AVG(timeSeconds) FROM RaceResult WHERE regattaId=%s", [regatta_id]);
    average_time = self.cursor.fetchall()
    return average_time

  def get_regatta_by_id(self, regatta_id):
    data = self.cursor.execute("SELECT * FROM Regatta WHERE regattaId=%s", [regatta_id])
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
    data = self.cursor.execute("SELECT MAX(memberId) FROM Member")
    member_id = self.cursor.fetchall()[0]['MAX(memberId)']
    return member_id

  def get_last_regatta_id(self):
    data = self.cursor.execute("SELECT MAX(regattaId) FROM Regatta")
    regatta_id = self.cursor.fetchall()[0]['MAX(regattaId)']
    return regatta_id

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

  def get_user_by_team_id(self, team_id):
    data = self.cursor.execute("SELECT * FROM Team WHERE teamId= %s", [team_id])
    username = self.cursor.fetchall()[0]['username']
    return username

  def create_team(self, conn, team_id, team_name, practice_cost, username, city, province):
    data = self.cursor.execute("INSERT INTO Team(teamId, name, practiceCost, username, regionCity, regionProvince) VALUES (%s, %s, %s, %s, %s, %s)", [team_id, team_name, practice_cost, username, city, province])
    conn.commit()
    return

  def create_member(self, conn, member_id, name, weight, height, role, paddle_side, date_of_birth, team_id):
    data = self.cursor.execute("INSERT INTO Member(memberId, memberName, weight, height, role, paddleSide, dateOfBirth, teamId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [member_id, name, weight, height, role, paddle_side, date_of_birth, team_id])
    conn.commit()
    return

  def create_regatta(self, conn, regatta_id, name, raceLength, location, raceDate, city, province):
    data = self.cursor.execute("INSERT INTO Regatta(regattaId, name, raceLength, location, raceDate, regionCity, regionProvince) VALUES (%s, %s, %s, %s, %s, %s, %s)", [regatta_id, name, raceLength, location, raceDate, city, province])
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

  def search_regattas_with_all_teams_from_province(self, search):
    data = self.cursor.execute('SELECT* FROM Regatta Re WHERE NOT EXISTS (SELECT T.teamId FROM Team T WHERE T.regionProvince = %s AND NOT EXISTS (SELECT Race.teamId FROM RaceResult Race WHERE T.teamId = Race.teamId AND Re.regattaId = Race.regattaId))', [search])
    regattas = self.cursor.fetchall();
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

  def delete_regatta(self, conn, regattaId):
    data = self.cursor.execute("Delete from Regatta WHERE regattaId = %s", [regattaId])
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

  def sort_paddle_brand_asc(self):
    data = self.cursor.execute("SELECT * from PaddleOwns order by brand asc")
    paddles = self.cursor.fetchall()
    return paddles

  def sort_paddle_brand_desc(self):
    data = self.cursor.execute("SELECT * from PaddleOwns order by brand desc")
    paddles = self.cursor.fetchall()
    return paddles

  def get_paddles(self):
    data = self.cursor.execute("SELECT * from PaddleOwns")
    paddles = self.cursor.fetchall()
    return paddles

  def get_paddles_from_member(self, member_id):
    data = self.cursor.execute("SELECT * from PaddleOwns where memberID=%d", [member_id])
    paddles = self.cursor.fetchall()
    return paddles

  def get_member_and_paddles_from_id(self, member_id):
    data = self.cursor.execute("SELECT * from Member m, PaddleOwns p where m.memberId={0} AND p.memberId={1}".format(member_id, member_id))
    member_with_paddle = self.cursor.fetchall()
    return member_with_paddle

  def get_distinct_provinces(self):
    data = self.cursor.execute("SELECT DISTINCT regionProvince FROM Team")
    provinces = self.cursor.fetchall()
    return provinces

  def avg_members_per_team(self):
    data = self.cursor.execute("SELECT AVG(member_count) FROM (SELECT count(memberId) as member_count FROM member GROUP BY teamId) as count")
    avg_members = self.cursor.fetchall()
    return avg_members

  def fastest_avg_team(self):
    data = self.cursor.execute("SELECT MIN(first_race) FROM (SELECT AVG(timeSeconds) as first_race FROM RaceResult GROUP BY teamId) as races")
    fastest_start = self.cursor.fetchall()
    return fastest_start

  def fastest_avg_race(self):
    data = self.cursor.execute("SELECT fastest.fastest_avg, names.name FROM (SELECT MIN(first_race) as fastest_avg FROM (SELECT AVG(timeSeconds) as first_race, regattaId FROM RaceResult GROUP BY regattaId) as times) as fastest, (SELECT AVG(timeSeconds) as first_race, regattaId FROM RaceResult GROUP BY regattaId) as ids,(SELECT name, regattaId from Regatta) as names WHERE ids.first_race=fastest.fastest_avg AND ids.regattaId=names.regattaId")
    fastest_start = self.cursor.fetchall()
    return fastest_start
