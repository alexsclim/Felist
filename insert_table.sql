INSERT INTO Region
VALUES
('North Vancouver', 'British Columbia');
INSERT INTO Region
VALUES
('Vancouver', 'British Columbia');
INSERT INTO Region
VALUES
('Chilliwack', 'British Columbia');
INSERT INTO Region
VALUES
('Kelowna', 'British Columbia');
INSERT INTO Region
VALUES
('Harrison', 'British Columbia');
INSERT INTO Region
VALUES
('Richmond', 'British Columbia');
INSERT INTO Region
VALUES
('Toronto', 'Ontario');
INSERT INTO Region
VALUES
('Montreal', 'Quebec');
INSERT INTO Region
VALUES
('Victoria', 'British Columbia');

INSERT INTO Regatta
VALUES
(1, 500, 'Concord Pacific', 'False Creek', '2017-04-20', 'Vancouver', 'British Columbia');
INSERT INTO Regatta
VALUES
(2, 500, 'Harrison', 'Harrison Hot Springs', '2017-07-21', 'Vancouver', 'British Columbia');
INSERT INTO Regatta
VALUES
(3, 500, 'Steveson', 'Steveson Village', '2017-08-22', 'Richmond', 'British Columbia');

INSERT INTO User
VALUES
('admin', 'pbkdf2:sha1:1000$gGjiBSaM$167a06ab6bf0616ca26af78f75c16d21e9fd46e9'); -- password: admin
INSERT INTO User
VALUES
('user', 'pbkdf2:sha1:1000$xdwaXArt$a8c041f472a31f5929e1aa3f0a9881134ff5dee3'); -- password: pass

INSERT INTO Team
VALUES
(1, 'DragonHearts Reborn', 234.80, 'admin', 'Vancouver', 'British Columbia');
INSERT INTO Team
VALUES
(2, 'DragonHearts ThunderBreakers', 1000.80, 'user', 'Vancouver', 'British Columbia');
INSERT INTO Team
VALUES
(3, 'UBC Lightning', 1000.80, 'admin', 'Vancouver', 'British Columbia');
INSERT INTO Team
VALUES
(4, 'ZY M', 1000.80, 'admin', 'Vancouver', 'British Columbia');
INSERT INTO Team
VALUES
(5, 'Xhibit', 1000.80, 'admin', 'Vancouver', 'British Columbia');


INSERT INTO Member
VALUES
(1, 'Alex', 170.80, 6.2, 'paddler', 'left', '1995-12-18', 1);
INSERT INTO Member
VALUES
(2, 'Clarence', 130.80, 5.8, 'paddler', 'left', '1995-09-20', 1);
INSERT INTO Member
VALUES
(3, 'Felix', 140.90, 5.9, 'paddler', 'right', '1995-11-20', 2);
INSERT INTO Member
VALUES
(4, 'Bob', 130.80, 5.8, 'paddler', 'left', '1995-09-20', 1);
INSERT INTO Member
VALUES
(5, 'asd', 130.80, 5.8, 'paddler', 'left', '1995-09-20', 2);
INSERT INTO Member
VALUES
(6, 'wqwe', 130.80, 5.8, 'paddler', 'left', '1995-09-20', 1);


INSERT INTO HasPractice
VALUES
(1, 'Monday', 'False Creek', '19:00', 2, 1);
INSERT INTO HasPractice
VALUES
(2, 'Tuesday', 'Creekside', '20:00', 2, 2);
INSERT INTO HasPractice
VALUES
(3, 'Friday', 'Creekside', '19:00', 2, 2);

INSERT INTO RaceResult
VALUES
(1, 1, 2.03, 1, 1);
INSERT INTO RaceResult
VALUES
(2, 2, 2.13, 1, 2);

INSERT INTO PaddleOwns
VALUES
(1, 'Burnwater', 'Trivium', 49, 'Blue');
INSERT INTO PaddleOwns
VALUES
(2, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(2, 'Burnwater', 'Trivium', 49, 'Black');
INSERT INTO PaddleOwns
VALUES
(3, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(4, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(5, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(6, 'Wood', 'Woodlyft', 50, 'Brown');

INSERT INTO Participates
VALUES
(1, 1);
INSERT INTO Participates
VALUES
(2, 1);
