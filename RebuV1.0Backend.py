from flask import Flask , jsonify
from Events import Events
import json

app = Flask(__name__)

Events = Events()

@app.route('/api/v1.0/locations', methods = ['GET'])
def get_location():
    '''This function return the gps location of all the events in and around santa rosa'''


    return Events.getlocations()


@app.route("/")
def test():

    return json.dumps('Welcome to my website')

if __name__ == '__main__':
    app.run()





