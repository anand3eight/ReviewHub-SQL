import sqlite3

class DBSQLUser :
    def __init__(self):
        self.conn = sqlite3.connect('DBOperations/ReviewProject.db')
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.cur = self.conn.cursor()
        self.query = str()

    def insertUser(self, user):
        self.query = f"""
        INSERT INTO User(Username, Name, Country)
        VALUES('{(user['Username'])}', '{user['Name']}', '{user['Country']}');
        """
        print(self.query)
        self.cur.execute(self.query)
        self.conn.commit()
        print('Inserted User')

    def searchUsernames(self) :
        self.query = f"""
            SELECT Username FROM User"""
        self.cur.execute(self.query)
        res = self.cur.fetchall()
        return [x[0] for x in res]

    def insertCompany(self, companyDetails):
        self.query = f"""
            INSERT INTO Company(Publisher, CompanyName, Address, Country, Phone, Email)
            VALUES('{companyDetails['Publisher']}', '{companyDetails['Name']}', '{companyDetails['Address']}', 
                    '{companyDetails['Country']}', {companyDetails['Phone']}, '{companyDetails['Email']}')"""
        self.cur.execute(self.query)
        self.conn.commit()
        print('Inserted Company')

    def fetchCompanyNames(self, companyName):
        self.query = f"""
              SELECT CompanyName FROM Company;"""
        self.cur.execute(self.query)
        res = self.cur.fetchall()
        resultlist = list()
        for x in res :
            if companyName in x[0] :
                resultlist.append(x[0])
        return resultlist

    def fetchCompanyByName(self, companyName):
        self.query = f"""
                    SELECT * FROM Company
                    WHERE CompanyName LIKE '%{companyName}%';"""
        self.cur.execute(self.query)
        res = self.cur.fetchall()
        resultlist = list()
        for x in res:
            dc = {'User': x[0], 'Name': x[1], 'Address': x[2], 'Country': x[3], 'Phone' : x[4], 'Email' : x[5]}
            resultlist.append(dc)
        return resultlist

    def fetchCompanyByLocation(self, companyLocation):
        self.query = f"""
            SELECT * FROM Company
            WHERE Address LIKE '%{companyLocation}%';"""
        self.cur.execute(self.query)
        res = self.cur.fetchall()
        resultlist = list()
        for x in res:
            dc = {'User': x[0], 'Name': x[1], 'Address': x[2], 'Country': x[3], 'Phone' : x[4], 'Email' : x[5]}
            resultlist.append(dc)
        return resultlist
    
    def insertCompanyReview(self, companyReview):
        try :
            self.query = f"""
                INSERT INTO CompanyReview(User, CompanyName, Rating, Review)
                VALUES('{companyReview['User']}', '{companyReview['Name']}', '{companyReview['Rating']}', '{companyReview['Review']}');"""
            self.cur.execute(self.query)
            self.conn.commit()
            print('Inserted Company Review')
        except sqlite3.IntegrityError :
            self.query = f"""
                UPDATE CompanyReview SET Rating = '{companyReview['Rating']}', Review = '{companyReview['Review']}'
                WHERE User = '{companyReview['User']}' AND CompanyName = '{companyReview['Name']}';"""
            self.cur.execute(self.query)
            self.conn.commit()
            print('Inserted Company Review')

    def fetchCompanyReviews(self, companyName):
        self.query = f"""
                    SELECT * FROM CompanyReview
                    WHERE CompanyName LIKE '%{companyName}%';"""
        self.cur.execute(self.query)
        res = self.cur.fetchall()
        resultlist = list()
        for x in res:
            dc = {'User': x[0], 'Name': x[1], 'Rating': x[2], 'Review': x[3]}
            resultlist.append(dc)
        return resultlist

    def getAverageCompanyRating(self, filter, value):
        if filter == 'Location' :
            self.query = f"""
                SELECT avg(C.Rating)
                FROM CompanyReview C
                WHERE CompanyName = (SELECT CompanyName 
                                     FROM Company 
                                     WHERE Address = '{value}');"""
        else :
            self.query = f"""
                SELECT avg(C.Rating)
                FROM CompanyReview C
                WHERE CompanyName = '{value}';
            """
        self.cur.execute(self.query)
        res = self.cur.fetchall()
        return res[0][0]

    def insertPlace(self, placeDetails):
        self.query = f"""
                    INSERT INTO Place(Publisher, PlaceName, Address, Country)
                    VALUES('{placeDetails['Publisher']}', '{placeDetails['Name']}', '{placeDetails['Address']}', 
                            '{placeDetails['Country']}')"""
        self.cur.execute(self.query)
        self.conn.commit()
        print('Inserted Place')

    def fetchPlaceNames(self, placeName):
        self.query = f"""
                      SELECT PlaceName FROM Place;"""
        self.cur.execute(self.query)
        res = self.cur.fetchall()
        resultlist = list()
        for x in res:
            if placeName in x[0]:
                resultlist.append(x[0])
        return resultlist

    def fetchPlaceByName(self, placeName):
        self.query = f"""
            SELECT * FROM Place
            WHERE PlaceName LIKE '%{placeName}%';"""
        self.cur.execute(self.query)
        res = self.cur.fetchall()
        resultlist = list()
        for x in res :
            dc = {'User' : x[0], 'Name' : x[1], 'Address' : x[2], 'Country' : x[3]}
            resultlist.append(dc)
        return resultlist

    def fetchPlaceByLocation(self, placeLocation):
        self.query = f"""
                    SELECT * FROM Place
                    WHERE Address LIKE '%{placeLocation}%';"""
        self.cur.execute(self.query)
        res = self.cur.fetchall()
        resultlist = list()
        for x in res:
            dc = {'User': x[0], 'Name': x[1], 'Address': x[2], 'Country': x[3]}
            resultlist.append(dc)
        return resultlist

    
    def insertPlaceReview(self, placeReview):
        try :
            self.query = f"""
                INSERT INTO PlaceReview(User, PlaceName, Rating, Review)
                VALUES('{placeReview['User']}', '{placeReview['Name']}', '{placeReview['Rating']}', '{placeReview['Review']}');"""
            self.cur.execute(self.query)
            self.conn.commit()
            print('Inserted Place Review')
        except sqlite3.IntegrityError :
            self.query = f"""
                UPDATE PlaceReview SET Rating = '{placeReview['Rating']}', Review = '{placeReview['Review']}'
                WHERE User = '{placeReview['User']}' AND PlaceName = '{placeReview['Name']}';"""
            self.cur.execute(self.query)
            self.conn.commit()
            print('Inserted Place Review')

    def fetchPlaceReviews(self, placeName):
        self.query = f"""
                    SELECT * FROM PlaceReview
                    WHERE PlaceName LIKE '%{placeName}%';"""
        self.cur.execute(self.query)
        res = self.cur.fetchall()
        resultlist = list()
        for x in res:
            dc = {'User': x[0], 'Name': x[1], 'Rating': x[2], 'Review': x[3]}
            resultlist.append(dc)
        return resultlist

    def getAveragePlaceRating(self, filter, value):
        if filter == 'Location' :
            self.query = f"""
                SELECT avg(P.Rating)
                FROM PlaceReview P
                WHERE PlaceName = (SELECT PlaceName 
                                     FROM Place 
                                     WHERE Address = '{value}');"""
        else :
            self.query = f"""
                SELECT avg(P.Rating)
                FROM PlaceReview P
                WHERE PlaceName = '{value}';
            """
        self.cur.execute(self.query)
        res = self.cur.fetchall()
        return res[0][0]




if __name__ == '__main__' :
    dbObj = DBSQLUser()
    placeReview = {'User' : 'anand3', 'Name' : 'Eiffel Tower', 'Rating' : 4, 'Review' : 'Great place for visit in Summer!'}
    place = {'Publisher' : 'anand5', 'Name' : 'Statue of Liberty', 'Address' : 'NYC', 'Country' : 'US'}
    company = {'Publisher' : 'anand3', 'Name' : 'Stark Industries', 'Address' : 'NYC', 'Country' : 'US', 'Phone' : 1234567890, 'Email' : 'anand@gmail.com'}
    print(dbObj.searchUsernames())
