-- Ascript that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
	id INT NOT NULL  DEFAULT 1,
       UNIQUE KEY (id),	
	name VARCHAR(256));
