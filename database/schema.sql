DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS training_sessions;
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS training_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    training_day TEXT NOT NULL,
    body_weight REAL NOT NULL,
    mood TEXT,
    date TEXT,
    chest REAL,
    arms REAL,
    waist REAL,
    legs REAL,
    shoulders REAL,
    training_duration_minutes REAL,
    sleep_hours REAL,
    stress_level INTEGER,
    program_phase TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    exercise TEXT NOT NULL,
    muscle_group TEXT NOT NULL,
    weight REAL NOT NULL,
    reps INTEGER NOT NULL,
    FOREIGN KEY (session_id) REFERENCES training_sessions(id) ON DELETE CASCADE
);