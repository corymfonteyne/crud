
CREATE TABLE data_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(45),
    summary VARCHAR(45),
    description TEXT
);

INSERT INTO data_type (
    name,
    summary,
    description 
) VALUES (
    "Integers",
    "Integer values",
    "A data type that stores integer values"
);

INSERT INTO data_type (
    name,
    summary,
    description 
) VALUES (
    "Float",
    "Floating point values",
    "A data type that allows us to store multiple values afte the decimal point"
);

INSERT INTO data_type (
    name,
    summary,
    description 
) VALUES (
    "Booleans",
    "True of false values",
    "Named after George Boole (Boolean algebra); These can take 
    true of Flase as their value."
);