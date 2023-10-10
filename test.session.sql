-- https://www.youtube.com/watch?v=Cz3WcZLRaWc&ab_channel=Fireship

-- @block
CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    country VARCHAR(2)
);

-- @block
INSERT INTO Users (email, bio, country)
VALUES(
    'hello@world.com',
    'i love u',
    'US'
)

-- @block
SELECT email, id FROM Users

WHERE country = 'US'
AND email LIKE 'hello%'

ORDER BY id DESC
LIMIT 2;

-- @block
CREATE INDEX email_index ON Users(email);

-- @block
CREATE TABLE Rooms(
    id INT AUTO_INCREMENT,
    street VARCHAR(255),
    owner_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (owner_id) REFERENCES Users(id)
);

-- @block
INSERT INTO Rooms (owner_id, street)
VALUES
    (1, 'san diego sailboat'),
    (1, 'nantucket cottage'),
    (1, 'vail cabin'),
    (1, 'sf cardboard box');


--@block
SELECT
    Users.id AS user_id,
    Rooms.id AS room_id,
    email,
    street
FROM users
INNER JOIN Rooms ON Rooms.owner_id = Users.id;

-- @block
CREATE TABLE Bookings(
    id INT AUTO_INCREMENT,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY (guest_id) REFERENCES Users(id),
    FOREIGN KEY (room_id) REFERENCES Rooms(id)
);

-- @block Rooms as a user has booked
SELECT
    guest_id,
    street,
    check_in
FROM Bookings
INNER JOIN Rooms On Rooms.owner_id = guest_id;
