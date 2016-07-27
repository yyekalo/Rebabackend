'''
This class retrive and store events from eventbrite in a database.
It also update the database in a set of intervals
'''
import json
from Event import Event
import requests
import sqlite3
import os


class Events:
    __events = list()
    __mytoken = ''
    c = None

    def __init__(self):
        self.__mytoken = ''
        try:
            response = requests.get('https://www.eventbriteapi.com/v3/events/search/?venue.city=santa&token='+ self.__mytoken)
            myevents = response.json()['events']
        except:
            print("Error unable to connect ")

        conn = sqlite3.connect('EventsDatabase.db')
        print(os.getcwd())
        self.c = conn.cursor()
        self.c.execute('''CREATE TABLE if not exists events (name text, starttime text, endtime text, venue_id text, longitude real, latitude real)''')


        for event in myevents:
            longitude = requests.get('https://www.eventbriteapi.com/v3/venues/'+ event['venue_id']+'/?token='+ self.__mytoken).json()['longitude']
            latitude = requests.get('https://www.eventbriteapi.com/v3/venues/'+ event['venue_id']+'/?token='+ self.__mytoken).json()['latitude']
            self.__events.append(Event(event['name']['text'],event['start']['local'],event['end']['local'],event['venue_id'],longitude,latitude))
            self.c.execute("insert into events VALUEs (?,?,?,?,?,?)",(event['name']['text'],event['start']['local'],event['end']['local'],event['venue_id'],float(longitude),float(latitude)))
            conn.commit()




    def getlocations(self):
        '''This function return a list of gps coordinate of events'''
        self.c.execute("select * from events")
        tempdata = self.c.fetchall()
        location = list()
        for event in tempdata:
            location.append({'longitude' : event[4],'latitude' : event[5]})
        return json.dump(location)


    def update(self):
        '''This fuction update the database of our events'''
        try:
            response = requests.get('https://www.eventbriteapi.com/v3/events/search/?venue.city=santa&token='+ self.__mytoken)
            myevents = response.json()['events']
        except:
            print("Error unable to connect ")

        for event in myevents:
            longitude = requests.get('https://www.eventbriteapi.com/v3/venues/'+ event['venue_id']+'/?token='+ self.__mytoken).json()['longitude']
            latitude = requests.get('https://www.eventbriteapi.com/v3/venues/'+ event['venue_id']+'/?token='+ self.__mytoken).json()['latitude']
            self.__events.append(Event(event['name']['text'],event['start']['local'],event['end']['local'],event['venue_id'],longitude,latitude))
            self.c.execute("insert into events VALUE(?,?,?,?,?,?)",(event['name']['text'],event['start']['local'],event['end']['local'],event['venue_id'],longitude,latitude))

