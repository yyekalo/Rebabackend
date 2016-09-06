
import sqlite3
import pprint
import requests
import Event
import json




class Database:

    Events = list()



    def __init__(self, data=None,token=None):

            print("we got connection")
            self._connection = sqlite3.connect('EventsDatabase.db')


            print("we got cursor")
            self._cursor = self._connection.cursor()

            print("we got execute")
            self._cursor.execute('''CREATE TABLE if not exists events (name text, starttime text, endtime text, venue_id text, longitude real, latitude real)''')

            print("we got data")
            if not data==None:
                self.bulk_store(data,token)

            print("we got done")




    def _save(self):

        self._connection.commit()






    def bulk_store(self,data,token):

        try:

            print("we got before")

            pprint.pprint(data)

            events = data['events']

            print("we got events done now")

            for event in events:
                longitude = requests.get('https://www.eventbriteapi.com/v3/venues/'+ event['venue_id']+'/?token='+ token).json()['longitude']
                latitude = requests.get('https://www.eventbriteapi.com/v3/venues/'+ event['venue_id']+'/?token='+ token).json()['latitude']
                self.Events.append(Event(event['name']['text'],event['start']['local'],event['end']['local'],event['venue_id'],longitude,latitude))
                self._cursor.execute("insert into events VALUEs (?,?,?,?,?,?)",(event['name']['text'],event['start']['local'],event['end']['local'],event['venue_id'],float(longitude),float(latitude)))
                self._save()
        except:
            print('we got erro in bulk store')







    def getlocations(self):
        '''

        :return: This function retun a josn formated list of gps locatin of events
        '''
        self.c.execute("select * from events")
        tempdata = self.c.fetchall()
        location = list()
        for event in tempdata:
            location.append({'longitude' : event[4],'latitude' : event[5]})

            pprint.pprint(json.dumps(location))

        return json.dumps(location)



    #TODO implment this function
    def get(self,list):
       '''
       :param list: This is the list of the set of data needed (eg,event name,event start time)
       :return:  This returnn a json formated of the set of data requested in the list
       '''

       return json.dumps("to be implmented")



