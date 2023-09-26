CREATE TABLE spending (
    id serial primary key,
    Date date,
    City VARCHAR(50),
    CardType VARCHAR(50),
    ExpType VARCHAR(20),
    Gender VARCHAR(1),
    Amount integer
);

COPY spending(id, City, Date, CardType, ExpType, Gender, Amount)
FROM '/Users/jeremysingh/Documents/GitHub/Financial-Data-Gender-Classifier/Credit card transactions - India - Simple.csv'
DELIMITER ','
CSV HEADER;