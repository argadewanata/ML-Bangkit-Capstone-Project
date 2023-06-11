-- Create Table SQL Script 

CREATE TABLE User(
    User_ID CHAR(3) PRIMARY KEY,
    FullName VARCHAR(255),
    Email VARCHAR(255),
    Latitude FLOAT,
    Longitude FLOAT,
    Password VARCHAR(35)
);

CREATE TABLE Wishlist(
    User_ID CHAR(3),
    Place_ID VARCHAR(45),
    FOREIGN KEY(User_ID) REFERENCES User(User_ID),
    FOREIGN KEY(Place_ID) REFERENCES Places(Place_ID)
);

CREATE TABLE Recommendation(
    User_ID CHAR(3),
    Place_ID VARCHAR(45),
    FOREIGN KEY(User_ID) REFERENCES User(User_ID),
    FOREIGN KEY(Place_ID) REFERENCES Places(Place_ID)
);

CREATE TABLE Places (
    Place_ID VARCHAR(45) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,  
    FormattedPhone VARCHAR(25),
    FormattedAddress VARCHAR(255),
    Latitude FLOAT,
    Longitude FLOAT,
    OverallRating FLOAT,
    PriceLevel FLOAT,
    Website VARCHAR(255),
    UserRatingTotal FLOAT,
    ServesBeer BOOLEAN,
    ServesWine BOOLEAN,
    ServesVegetarianFood BOOLEAN,
    WheelchairAccessibleEntrance BOOLEAN,
    Halal BOOLEAN,
    StreetAddress VARCHAR(255),
    District VARCHAR(255),
    City VARCHAR(255),
    Regency VARCHAR(255),
    Province VARCHAR(255),
    PostalNumber VARCHAR(25)
);

CREATE TABLE Types(
    Place_ID VARCHAR(45),
    Bar BOOLEAN,
    Cafe BOOLEAN,
    Restaurant BOOLEAN,
    FOREIGN KEY(Place_ID) REFERENCES Places(Place_ID)
);

CREATE TABLE Reviews(
    Place_ID VARCHAR(45),
    Name VARCHAR(255),
    Star INT,
    ReviewText VARCHAR(5000),
    FOREIGN KEY(Place_ID) REFERENCES Places(Place_ID)
);

CREATE TABLE OperationHours(
    Place_ID VARCHAR(45),
    Monday_Open CHAR(5),
    Monday_Close CHAR(5),
    Tuesday_Open CHAR(5),
    Tuesday_Close CHAR(5),
    Wednesday_Open CHAR(5),
    Wednesday_Close CHAR(5),
    Thursday_Open CHAR(5),
    Thursday_Close CHAR(5),
    Friday_Open CHAR(5),
    Friday_Close CHAR(5),
    Saturday_Open CHAR(5),
    Saturday_Close CHAR(5),
    Sunday_Open CHAR(5),
    Sunday_Close CHAR(5),
    FOREIGN KEY(Place_ID) REFERENCES Places(Place_ID)
);

