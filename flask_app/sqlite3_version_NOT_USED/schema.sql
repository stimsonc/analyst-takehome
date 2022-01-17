DROP TABLE IF EXISTS pets;

CREATE TABLE pets (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Breed TEXT NOT NULL,
    CHECK (Breed == 'cat' or Breed == 'dog')
);