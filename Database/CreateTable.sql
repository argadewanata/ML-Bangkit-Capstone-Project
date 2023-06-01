-- Create Table SQL Script 

CREATE TABLE Places (
    Place_ID VARCHAR(45) PRIMARY KEY,
    Name VARCHAR(40) NOT NULL,  
    FormattedPhone VARCHAR(25) NOT NULL,
    FormattedAddress VARCHAR(70) NOT NULL,
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
    StreetAddress VARCHAR(40),
    District VARCHAR(25),
    City VARCHAR(25),
    Regency VARCHAR(25),
    Province VARCHAR(25),
    PostalNumber VARCHAR(25)
);


CREATE TABLE Categories(
    Place_ID VARCHAR(35),
    Cafe BOOLEAN,
    Restaurant BOOLEAN,
    Bar BOOLEAN,
    FOREIGN KEY(Place_ID) REFERENCES Places(Place_ID)
);

CREATE TABLE Reviews(
    Place_ID VARCHAR(35),
    Name VARCHAR(25),
    Time VARCHAR(30),
    Experience VARCHAR(15),
    NumberOfReview INT,
    ReviewText VARCHAR(1000),
    Star INT,
    FOREIGN KEY(Place_ID) REFERENCES Places(Place_ID)
);

CREATE TABLE WorkingHour(
    Place_ID VARCHAR(35),
    MondayOpenHour CHAR(5),
    MondayCloseHour CHAR(5),
    TuesdayOpenHour CHAR(5),
    TuesdayCloseHour CHAR(5),
    WednesdayOpenHour CHAR(5),
    WednesdayCloseHour CHAR(5),
    ThursdayOpenHour CHAR(5),
    ThursdayCloseHour CHAR(5),
    FridayOpenHour CHAR(5),
    FridayCloseHour CHAR(5),
    SaturdayOpenHour CHAR(5),
    SaturdayCloseHour CHAR(5),
    SundayOpenHour CHAR(5),
    SundayCloseHour CHAR(5),
    FOREIGN KEY(Place_ID) REFERENCES Places(Place_ID)
);

