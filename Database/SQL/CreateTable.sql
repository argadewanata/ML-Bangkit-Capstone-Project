-- Create Table SQL Script 

CREATE TABLE Places (
    Place_ID VARCHAR(45) PRIMARY KEY,
    Name VARCHAR(40) NOT NULL,  
    FormattedPhone VARCHAR(25) NOT NULL,
    FormattedAddress VARCHAR(255) NOT NULL,
    Latitude FLOAT NOT NULL,
    Longitude FLOAT NOT NULL,
    OverallRating FLOAT,
    PriceLevel FLOAT,
    Website VARCHAR(50),
    UserRatingTotal FLOAT,
    ServesBeer BOOLEAN,
    ServesWine BOOLEAN,
    ServesVegetarianFood BOOLEAN,
    WheelchairAccessibleEntrance BOOLEAN,
    Halal BOOLEAN,
    StreetAddress VARCHAR(255),
    District VARCHAR(25),
    City VARCHAR(25),
    Regency VARCHAR(25),
    Province VARCHAR(25),
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
    Name VARCHAR(25),
    Time VARCHAR(30),
    Experience VARCHAR(15),
    NumberOfReview INT,
    ReviewText VARCHAR(1000),
    Star INT,
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

