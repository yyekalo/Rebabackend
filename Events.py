'''
This class retrive and store events from eventbrite in a database.
It also update the database in a set of intervals
'''

import requests
from Database import Database



class Events:




    def __init__(self):

        self.__mytoken = 'CBTTFWHSGZGHOGSK75AG'

        try:

            response = requests.get('https://www.eventbriteapi.com/v3/events/search/?venue.city=santa&token=CBTTFWHSGZGHOGSK75AG'+ self.__mytoken)

            self.database = Database(response,self.__mytoken)

        except:

            print("Error unable to connect ")







    def getlocations(self):

        return self.database.getlocations()






    def update(self):

        try:

            response = requests.get('https://www.eventbriteapi.com/v3/events/search/?venue.city=santa&token='+ self.__mytoken)

            self.databse.bulk_store(response,self.__mytoken)

        except:

            print("Error unable to connect ")

