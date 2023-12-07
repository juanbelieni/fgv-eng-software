CREATE TABLE user (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
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
    user TEXT,
    goal TEXT,
    page INT,
    FOREIGN KEY (user) REFERENCES user(id),
    FOREIGN KEY (goal) REFERENCES goal(id)
);