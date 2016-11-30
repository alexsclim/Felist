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
INSERT INTO Region
VALUES
('Shatin', 'Hong Kong');
INSERT INTO Region
VALUES
('No City', 'No Province');

INSERT INTO Regatta
VALUES
(1, 500, 'Concord Pacific', 'False Creek', '2017-04-20', 'Vancouver', 'British Columbia');
INSERT INTO Regatta
VALUES
(2, 500, 'Harrison', 'Harrison Hot Springs', '2017-07-21', 'Vancouver', 'British Columbia');
INSERT INTO Regatta
VALUES
(3, 500, 'Steveson', 'Steveson Village', '2017-08-22', 'Richmond', 'British Columbia');
INSERT INTO Regatta
VALUES
(4, 500, 'Hong Kong Dragon Boat Regatta', 'Sha Tin Town Centre', '2017-08-23', 'Shatin', 'Hong Kong');
INSERT INTO Regatta
VALUES
(5, 500, 'Ontario Regatta', 'Lake Ontario', '2018-08-24', 'Toronto', 'Ontario');

INSERT INTO User
VALUES
('admin', 'pbkdf2:sha1:1000$gGjiBSaM$167a06ab6bf0616ca26af78f75c16d21e9fd46e9'); -- password: admin
INSERT INTO User
VALUES
('user', 'pbkdf2:sha1:1000$xdwaXArt$a8c041f472a31f5929e1aa3f0a9881134ff5dee3'); -- password: pass

INSERT INTO Team
VALUES
(0, 'Free-agents', 0, 'admin', 'No City', 'No Province');
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
(5, 'Xhibit', 1000.80, 'admin', 'Toronto', 'Ontario');
INSERT INTO Team
VALUES
(6, 'Felix Best Team', 1000.80, 'admin', 'Toronto', 'Ontario');


INSERT INTO Member
VALUES
(1, 'Alex', 170.80, 6.2, 'paddler', 'left', '1995-12-17', 1);
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
(6, 'Vicky', 65.65, 4.3, 'paddler', 'right', '1995-06-30', 2);
INSERT INTO Member
VALUES
(7, 'Andrea', 62.23, 4.2, 'paddler', 'right', '1995-09-11', 3);
INSERT INTO Member
VALUES
(8, 'Melissa', 100.10, 5.4, 'paddler', 'left', '1995-09-21', 3);
INSERT INTO Member
VALUES
(9, 'Anson', 125.59, 5.8, 'paddler', 'left', '1995-01-03', 4);
INSERT INTO Member
VALUES
(10, 'Lilian', 85.57, 5.7, 'paddler', 'right', '1995-05-27', 4);
INSERT INTO Member
VALUES
(11, 'Kevin', 285.50, 6.2, 'paddler', 'left', '1995-09-23', 4);
INSERT INTO Member
VALUES
(12, 'Alan', 130.80, 5.8, 'paddler', 'right', '1995-07-19', 5);
INSERT INTO Member
VALUES
(13, 'Amy', 110.50, 5.6, 'paddler', 'left', '1995-10-31', 5);
INSERT INTO Member
VALUES
(14, 'Ana', 100.20, 5.4, 'paddler', 'right', '1995-09-20', 6);
INSERT INTO Member
VALUES
(15, 'Kae', 180.25, 5.11, 'paddler', 'left', '1995-09-20', 6);

INSERT INTO RaceResult
VALUES
(1, 1, 2.03, 1, 1);
INSERT INTO RaceResult
VALUES
(2, 2, 2.13, 1, 2);
INSERT INTO RaceResult
VALUES
(3, 3, 2.33, 1, 3);
INSERT INTO RaceResult
VALUES
(4, 4, 2.85, 1, 4);
INSERT INTO RaceResult
VALUES
(5, 5, 2.93, 1, 5);
INSERT INTO RaceResult
VALUES
(6, 1, 1.95, 2, 1);
INSERT INTO RaceResult
VALUES
(7, 2, 2.05, 2, 5);
INSERT INTO RaceResult
VALUES
(8, 3, 2.15, 2, 3);
INSERT INTO RaceResult
VALUES
(9, 4, 2.25, 2, 4);
INSERT INTO RaceResult
VALUES
(10, 5, 2.35, 2, 2);
INSERT INTO RaceResult
VALUES
(11, 1, 2.45, 3, 3);
INSERT INTO RaceResult
VALUES
(12, 2, 2.55, 3, 1);
INSERT INTO RaceResult
VALUES
(13, 3, 2.65, 3, 2);
INSERT INTO RaceResult
VALUES
(14, 4, 2.75, 3, 4);
INSERT INTO RaceResult
VALUES
(15, 1, 2.75, 4, 6);
INSERT INTO RaceResult
VALUES
(16, 2, 2.76, 4, 5);
INSERT INTO RaceResult
VALUES
(17, 3, 2.77, 4, 4);
INSERT INTO RaceResult
VALUES
(18, 4, 2.78, 4, 3);
INSERT INTO RaceResult
VALUES
(19, 5, 2.79, 4, 2);
INSERT INTO RaceResult
VALUES
(20, 1, 2.65, 5, 5);
INSERT INTO RaceResult
VALUES
(21, 2, 2.66, 5, 4);
INSERT INTO RaceResult
VALUES
(22, 3, 2.67, 5, 3);
INSERT INTO RaceResult
VALUES
(23, 4, 2.68, 5, 2);
INSERT INTO RaceResult
VALUES
(24, 5, 2.69, 5, 1);

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
INSERT INTO PaddleOwns
VALUES
(7, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(8, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(9, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(10, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(11, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(12, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(13, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(14, 'Wood', 'Woodlyft', 50, 'Brown');
INSERT INTO PaddleOwns
VALUES
(15, 'Burnwater', 'Trivium', 49, 'Black');

