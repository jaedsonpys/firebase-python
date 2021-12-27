import pyrebase
import json

config_file = open('.config.json', 'r')
config = json.load(config_file)

firebase = pyrebase.initialize_app(config)
database = firebase.database()

database.child('users').child('jaedsonpys').set({'name': 'Jaedson'})
database.child('users').child('jaedsonpys').update({'age': 14, 'state': 'AL'})

database.child('users').child('pedro203').set({'name': 'Pedro'})
database.child('users').child('pedro203').update({'age': 24, 'state': 'RJ'})
