'''This class hold the information of an event
name  ->     name of the event
startime ->  The local start time of the event
endtime - > The local end time of the event
venueid ->  The venue's id in Eventbrite
longitude -> The longitude of the events location
latitude -> The latitude of the events location
'''



class Event:

    def __init__(self,eventname,starttime,endtime,venueid,longitude=None, latitude=None):
        self.name=eventname
        self.starttime = starttime
        self.endtime = endtime
        self.venueid = venueid
        self.longitude = longitude
        self.latitude =  latitude

