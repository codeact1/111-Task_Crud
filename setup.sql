--Create a  task table


CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(128),
    subtitle VARCHAR(256),
    body TEXT,
    active BOOLEAN DEFAULT 1
);

--Records for the table
INSERT INTO task(
    title,
    subtitle,
    body
) VALUES (
    "Wash the car",
    "trim the hedges",
    "Make the bed"
);

INSERT INTO task(
    title,
    subtitle,
    body
) VALUES (
    "Look for gold",
    "Rake the leaves",
    "Study"
);

INSERT INTO task(
    title,
    subtitle,
    body
) VALUES (
    "Feed the dog",
    "Drop off recyclables",
    "Practice"
);

