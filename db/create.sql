CREATE TABLE user (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    bio TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE goal (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    public BIT NOT NULL,
    book TEXT NOT NULL,
    password TEXT 
);

CREATE TABLE progress (
    user FOREIGN KEY,
    goal FOREIGN KEY,
    page INT
);