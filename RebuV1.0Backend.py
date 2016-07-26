from flask import Flask , jsonify
from Events import Events

app = Flask(__name__)

Events = Events()

@app.route('/api/v1.0/locations', methods = ['GET'])
def get_location():
    return "hellow world"
    return jsonify(Events.getlocations())

if __name__ == '__main__':
    app.run()





