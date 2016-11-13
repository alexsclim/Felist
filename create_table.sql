CREATE DATABASE IF NOT EXISTS felist;
use felist;

CREATE TABLE IF NOT EXISTS Region(
    city char(50),
    province char(50),
    PRIMARY KEY(city, province)
);

CREATE TABLE IF NOT EXISTS Regatta(
  regattaId int,
  raceLength int,
  name char(40),
  location char(30),
  raceDate date,
  regionCity char(50) NOT NULL,
  regionProvince char(50) NOT NULL,
  PRIMARY KEY(regattaId),
  FOREIGN KEY(regionCity, regionProvince) REFERENCES Region(city, province)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS User(
  username char(20) ,
  encryptedPassword char(100),
  PRIMARY KEY(username)
);

CREATE TABLE IF NOT EXISTS Team(
  teamId int,
  name char(50),
  practiceCost decimal,
  username char(20) NOT NULL,
  regionCity char(50) NOT NULL,
  regionProvince char(50) NOT NULL,
  PRIMARY KEY(teamId),
  FOREIGN KEY(username) REFERENCES user(username)
      ON DELETE NO ACTION
      ON UPDATE CASCADE,
  FOREIGN KEY(regionCity, regionProvince) REFERENCES Region(city, province)
      ON DELETE NO ACTION
      ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Member(
  memberId int,
  memberName char(30),
  weight float,
  height float,
  role char(20),
  paddleSide char(10),
  dateOfBirth date,
  teamId int NOT NULL,
  PRIMARY KEY(memberId),
  FOREIGN KEY(teamId) REFERENCES Team(teamId)
    ON DELETE NO ACTION,
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS HasPractice(
  practiceId int,
  dayOfWeek char(10),
  location char(50),
  startTime time,
  duration int,
  teamId int,
  PRIMARY KEY(practiceId, teamId),
  FOREIGN KEY(teamId) REFERENCES Team(teamId)
);

CREATE TABLE IF NOT EXISTS RaceResult(
  resultId int,
  ranking int,
  timeSeconds decimal,
  regattaId int NOT NULL,
  teamId int,
  PRIMARY KEY(teamId, resultId),
  FOREIGN KEY(regattaId) REFERENCES Regatta(regattaId)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY(teamId) REFERENCES Team(teamId)
    ON DELETE NO ACTION
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS PaddleOwns(
  memberId int,
  brand char(20),
  type char(20),
  size int,
  colour char(15),
  PRIMARY KEY(memberId, brand),
  FOREIGN KEY(memberId) REFERENCES Member(memberId)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Participates(
    teamId int,
    regattaId int,
    PRIMARY KEY(teamId, regattaId),
    FOREIGN KEY(teamId) REFERENCES Team(teamId),
    FOREIGN KEY(regattaId) REFERENCES Regatta(regattaId)
);
