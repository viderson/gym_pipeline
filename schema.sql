DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS training_sessions;

CREATE TABLE IF NOT EXISTS training_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    training_day TEXT NOT NULL,
    body_weight REAL NOT NULL,
    mood TEXT,
    date TEXT
);

CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    exercise TEXT NOT NULL,
    weight REAL NOT NULL,
    reps INTEGER NOT NULL,
    FOREIGN KEY (session_id) REFERENCES training_sessions(id) ON DELETE CASCADE
);