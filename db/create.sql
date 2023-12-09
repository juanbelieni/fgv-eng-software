CREATE TABLE user (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    bio TEXT NOT NULL,
    password TEXT NOT NULL
);

'''
CREATE TABLE goal (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    public BIT NOT NULL,
    book TEXT NOT NULL,
    password TEXT 
);
'''

CREATE TABLE goal (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    host TEXT NOT NULL,
    public BIT NOT NULL,
    hidden BIT NOT NULL,
    book TEXT NOT NULL,
    FOREIGN KEY (host) REFERENCES user(id)
);

CREATE TABLE user_goal (
    user TEXT NOT NULL,
    goal TEXT NOT NULL,
    PRIMARY KEY (user, goal),
    FOREIGN KEY (user) REFERENCES user(id),
    FOREIGN KEY (goal) REFERENCES goal(id)
);

CREATE TABLE progress (
    user TEXT NOT NULL,
    goal TEXT NOT NULL,
    page FLOAT NOT NULL,
    FOREIGN KEY (user) REFERENCES user(id),
    FOREIGN KEY (goal) REFERENCES goal(id)
);