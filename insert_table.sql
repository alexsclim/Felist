INSERT INTO Region
VALUES
('North Vancouver', 'British Columbia');
INSERT INTO Region
VALUES
('Vancouver', 'British Columbia');
INSERT INTO Region
VALUES
('Washington', 'Seattle');
INSERT INTO Region
VALUES
('Harrison', 'British Columbia');
INSERT INTO Region
VALUES
('Richmond', 'British Columbia');
INSERT INTO Region
VALUES
('Tsuen Wan', 'Hong Kong');

INSERT INTO RegattaDetails
VALUES
(1, 'Concord Pacific', 'False Creek', 500, '2017-04-20');
INSERT INTO RegattaDetails
VALUES
(2, 'Harrison', 'Harrison Hot Springs', 500, '2017-07-21');
INSERT INTO RegattaDetails
VALUES
(3, 'Steveson', 'Steveson Village', 500, '2017-08-22');

INSERT INTO User
VALUES
(1, 'admin', 'admin');
INSERT INTO User
VALUES
(2, 'felix', 'tso');

INSERT INTO RegattaLocation
VALUES
('False Creek', 'Vancouver', 'British Columbia', 1);
INSERT INTO RegattaLocation
VALUES
('Harrison Hot Springs', 'Harrison', 'British Columbia', 2);
INSERT INTO RegattaLocation
VALUES
('Steveson Village', 'Richmond', 'British Columbia', 3);

INSERT INTO Team
VALUES
(1, 'DragonHearts Reborn', 234.80, 1, 'Vancouver', 'British Columbia');
INSERT INTO Team
VALUES
(2, 'DragonHearts ThunderBreakers', 1000.80, 1, 'Vancouver', 'British Columbia');

INSERT INTO Member
VALUES
(1, 'Alex', 170.80, 6.2, 'paddler', 'left', '1995-12-18', 1);
INSERT INTO Member
VALUES
(2, 'Clarence', 130.80, 5.8, 'paddler', 'left', '1995-09-20', 1);

INSERT INTO PracticeTeam
VALUES
(1, 1);
INSERT INTO PracticeTeam
VALUES
(2, 2);

INSERT INTO PracticeLocation
VALUES
(1, 'Creekside Community Centre');
INSERT INTO PracticeLocation
VALUES
(2, 'False Creek Community Centre');

INSERT INTO PracticeTime
VALUES
(1, 'Monday', '19:00', 2);
INSERT INTO PracticeTime
VALUES
(2, 'Friday', '20:00', 2);

INSERT INTO ResultReference
VALUES
(1, 1, 1);
INSERT INTO ResultReference
VALUES
(1, 2, 2);

INSERT INTO ResultDetails
VALUES
(1, 1, 1, 2.03);
INSERT INTO ResultDetails
VALUES
(2, 2, 2, 2.13);

INSERT INTO PaddleSize
VALUES
(1, 'Burnwater', 49);
INSERT INTO PaddleSize
VALUES
(2, 'Wood', 50);

INSERT INTO PaddleDetails
VALUES
(1, 'Burnwater', 'Trivium', 'Blue');
INSERT INTO PaddleDetails
VALUES
(2, 'Wood', 'Woodlyfe', 'Brown');

INSERT INTO Participates
VALUES
(1, 1);
INSERT INTO Participates
VALUES
(2, 1);

