CREATE DATABASE IF NOT EXISTS felist;
use felist;

CREATE TABLE IF NOT EXISTS Region(
    city char(50),
    province char(50),
    PRIMARY KEY(city, province)
);

CREATE TABLE IF NOT EXISTS RegattaDetails(
  regattaId int,
  name char(40),
  location char(30),
  raceLength int,
  raceDate date,
  PRIMARY KEY(regattaId)
);

CREATE TABLE IF NOT EXISTS User(
  username char(20) ,
  encryptedPassword char(100),
  PRIMARY KEY(username)
);

CREATE TABLE IF NOT EXISTS RegattaLocation(
  location char(30),
  regionCity char(50) NOT NULL,
  regionProvince char(50) NOT NULL,
  regattaId int,
  PRIMARY KEY(location),
  FOREIGN KEY(regattaId) REFERENCES RegattaDetails(regattaId)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY(regionCity, regionProvince) REFERENCES Region(city, province)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
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
        ON DELETE NO ACTION
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS PracticeTeam(
  teamId int,
  practiceId int,
  PRIMARY KEY(practiceId),
  FOREIGN KEY(teamId) REFERENCES Team(teamId)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS PracticeLocation(
  teamId int,
  location char(50),
  PRIMARY KEY(teamId),
  FOREIGN KEY(teamId) REFERENCES PracticeTeam(teamId)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS PracticeTime(
  practiceId int,
  dayOfWeek char(10),
  startTime time,
  duration int,
  PRIMARY KEY(practiceId),
  FOREIGN KEY(practiceId) REFERENCES PracticeTeam(practiceId)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS ResultReference(
  regattaId int,
  teamId int,
  resultId int,
  PRIMARY KEY(resultId, teamId),
  FOREIGN KEY(teamId) REFERENCES Team(teamId)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  FOREIGN KEY(regattaId) REFERENCES RegattaDetails(regattaId)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS ResultDetails(
  resultId int,
  teamId int,
  ranking int,
  timeSeconds decimal,
  PRIMARY KEY (resultId, teamId),
  FOREIGN KEY (resultId, teamId) REFERENCES ResultReference(resultId, teamId)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS PaddleSize(
  memberId int,
  brand char(15),
  size int,
  PRIMARY KEY(memberId, brand),
  FOREIGN KEY(memberId) REFERENCES Member(memberId)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS PaddleDetails(
  memberId int,
  brand char(15),
  type char(20),
  colour char(15),
  PRIMARY KEY(memberId, brand),
  FOREIGN KEY(memberId, brand) REFERENCES PaddleSize(memberId, brand)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Participates(
    teamId int,
    regattaId int,
    PRIMARY KEY(teamId, regattaId),
    FOREIGN KEY(teamId) REFERENCES Team(teamId),
    FOREIGN KEY(regattaId) REFERENCES RegattaDetails(regattaId)
);
