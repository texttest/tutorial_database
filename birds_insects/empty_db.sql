

CREATE TABLE wildlife (
    internalId        INT,
    name        VARCHAR(100),
    type        VARCHAR(16),
);


CREATE TABLE observations (
    internalId        INT,
    date         DATETIME,
    PRIMARY KEY (internalId),
    FOREIGN KEY (wildlife) REFERENCES wildlife(internalId)
);
