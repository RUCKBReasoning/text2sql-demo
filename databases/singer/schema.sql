PRAGMA foreign_keys = ON;

CREATE TABLE "singer" (
"Singer_ID" int,
"Name" text,
"Birth_Year" real,
"Net_Worth_Millions" real,
"Citizenship" text,
PRIMARY KEY ("Singer_ID")
);

CREATE TABLE "song" (
"Song_ID" int,
"Title" text,
"Singer_ID" int,
"Sales" real,
"Highest_Position" real,
PRIMARY KEY ("Song_ID"),
FOREIGN KEY ("Singer_ID") REFERENCES `singer`("Singer_ID")
);

INSERT INTO  "singer" VALUES (1,"Liliane Bettencourt","1944","30.0","France");
INSERT INTO  "singer" VALUES (2,"Christy Walton","1948","28.8","United States");
INSERT INTO  "singer" VALUES (3,"Alice Walton","1949","26.3","United States");
INSERT INTO  "singer" VALUES (4,"Iris Fontbona","1942","17.4","Chile");
INSERT INTO  "singer" VALUES (5,"Jacqueline Mars","1940","17.8","United States");
INSERT INTO  "singer" VALUES (6,"Gina Rinehart","1953","17","Australia");
INSERT INTO  "singer" VALUES (7,"Susanne Klatten","1962","14.3","Germany");
INSERT INTO  "singer" VALUES (8,"Abigail Johnson","1961","12.7","United States");

INSERT INTO  "song" VALUES ("1","Do They Know It's Christmas",1,"1094000","1");
INSERT INTO  "song" VALUES ("2","F**k It (I Don't Want You Back)",1,"552407","1");
INSERT INTO  "song" VALUES ("3","Cha Cha Slide",2,"351421","1");
INSERT INTO  "song" VALUES ("4","Call on Me",4,"335000","1");
INSERT INTO  "song" VALUES ("5","Yeah",2,"300000","1");
INSERT INTO  "song" VALUES ("6","All This Time",6,"292000","1");
INSERT INTO  "song" VALUES ("7","Left Outside Alone",5,"275000","3");
INSERT INTO  "song" VALUES ("8","Mysterious Girl",7,"261000","1");

