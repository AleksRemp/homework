CREATE TABLE IF NOT EXISTS organiser (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    message TEXT NOT NULL DEFAULT '',
    deadline DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    status INTEGER NOT NULL DEFAULT 1  
)