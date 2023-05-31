-- Create Table SQL Script 

CREATE TABLE Places(
    Places_ID VARCHAR(35) PRIMARY KEY,
    Name VARCHAR(40) NOT NULL,
    FormattedPhone VARCHAR(15) NOT NULL,
    FormattedAddress VARCHAR(70) NOT NULL,
    Latitude FLOAT NOT NULL,
    Longitude FLOAT NOT NULL,
    OverallRating FLOAT(2, 2) NOT NULL,
    PriceLevel INT NOT NULL,
    Website VARCHAR(50) NOT NULL,
    UserRatingTotal INT NOT NULL,
    ServesBeer BOOLEAN NOT NULL,
    ServesWine BOOLEAN NOT NULL,
    ServesVegetarian BOOLEAN NOT NULL,
    Halal BOOLEAN NOT NULL,
    WheelchairAccesibleEntrance BOOLEAN NOT NULL,
    StreetAddress VARCHAR(40),
    District VARCHAR(20),
    City VARCHAR(20),
    Regency VARCHAR(20),
    Province VARCHAR(20),
    PostalNumber VARCHAR(10),
    PhotoLink VARCHAR(50)
);

CREATE TABLE Categories(
    Places_ID VARCHAR(35),
    Cafe BOOLEAN,
    Restaurant BOOLEAN,
    Bar BOOLEAN,
    FOREIGN KEY(Places_ID) REFERENCES Places(Places_ID)
);

CREATE TABLE Reviews(
    Places_ID VARCHAR(35),
    Name VARCHAR(25),
    Time VARCHAR(30),
    Experience VARCHAR(15),
    NumberOfReview INT,
    ReviewText VARCHAR(1000),
    Star INT,
    FOREIGN KEY(Places_ID) REFERENCES Places(Places_ID)
);

CREATE TABLE WorkingHour(
    Places_ID VARCHAR(35),
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
    FOREIGN KEY(Places_ID) REFERENCES Places(Places_ID)
);

