import sqlite3

if __name__ == '__main__' :
    conn = sqlite3.connect('ReviewProject.db')
    cur = conn.cursor()
    createUser = """
    CREATE TABLE User
    (
        Username varchar(50) CONSTRAINT PK_User PRIMARY KEY,
        Name varchar(100),
        Country varchar(20)
    );
    """
    createPlace = """
    CREATE TABLE Place
    (
        Publisher varchar(50),
        PlaceName varchar(100) CONSTRAINT PK_Place PRIMARY KEY ,
        Address varchar(20),
        Country varchar(30),
        CONSTRAINT FK_Place
        FOREIGN KEY(Publisher)
        REFERENCES User(Username)
    );
    """

    createCompany = """
    CREATE TABLE Company
    (
        Publisher varchar(50) ,
        CompanyName varchar(100) CONSTRAINT PK_Company PRIMARY KEY,
        Address varchar(20),
        Country varchar(30),
        Phone number(10),
        email varchar(30),
        CONSTRAINT FK_Company
        FOREIGN KEY(Publisher)
        REFERENCES User(Username)
    );
    """

    createCompanyReview = """
    CREATE TABLE CompanyReview
    (
        User varchar(50),
        CompanyName varchar2(100),
        rating number(2),
        review varchar(200),
        CONSTRAINT FK1_CompanyReview
        FOREIGN KEY(User)
        REFERENCES User(Username),
        CONSTRAINT FK2_CompanyReview
        FOREIGN KEY(CompanyName)
        REFERENCES Company(CompanyName),
        CONSTRAINT PK_CompanyReview
        PRIMARY KEY(User, CompanyName)
    );
    """

    createPlaceReview = """
    CREATE TABLE PlaceReview
    (   
        User varchar(50),
        PlaceName varchar2(100),
        Rating number(2),
        Review varchar(200),
        CONSTRAINT FK1_PlaceReview
        FOREIGN KEY(User)
        REFERENCES User(Username),
        CONSTRAINT FK2_PlaceReview
        FOREIGN KEY(PlaceName)
        REFERENCES Place(PlaceName),
        CONSTRAINT PK_PlaceReview
        PRIMARY KEY(User, PlaceName)
    );
    """
    dropQuery = "DROP TABLE CompanyReview"
    cur.execute(createPlaceReview)
    conn.close()