--Ascript that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id(id NOT NULL UNIQUE INT DEFAULT 1, name VARCHAR(256));
