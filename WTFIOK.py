from flask import Flask
from flask_ask import Ask, statement, question, session
import requests
import random


app = Flask(__name__)
ask = Ask(app, "/")

def make_excuse():
	places = ['Under the bins', 'Left on a job', 'Eaten', 'Someone\'s house', 'Accidentally gave it to the client', 'Really? Again?', 'Oh that, we lost that months ago', 'Why are you asking me for help?', 'It\'s in broken bits', 'In the van?', 'In the theatre', 'Relax, I\'m sure it\'ll turn up soon', 'Where you last had it', 'I\'m sure it will magically appear', 'Try calling it', 'The PO book drawer', 'In the corridore', 'Just go to the pub', 'With the e-stop key']
	excuses = ['I thought I told someone', 'Have you tried forgetting about it?', 'We can always buy another one', 'Have you tried turning it off and on again?', 'Just pretend nothing happend', 'It has a label on it though', 'It\'s not the end of the world', 'Just think faster', 'Pub?', 'Just ask a volunteer to find it']
	message = places[random.randint(0, len(places)-1)] + '. ' + excuses[random.randint(0, len(excuses)-1)]
	return message

@app.route('/')

def homepage():
	return "Hello world! This is a test page."

@ask.launch
def start_skill():
	welcomes = ['Whats missing?', 'What kit have you lost?', 'Whats gone?', 'What do you need?']
	welcome_message = welcomes[random.randint(0, len(welcomes)-1)]
	return question(welcome_message)

@ask.intent("KitIntent")
def excuse():
	ex = make_excuse()
	return statement(ex)

@ask.intent('AMAZON.FallbackIntent')
def excuse_fb():
	ex = make_excuse()
	return statement(ex)

@ask.intent("NothingIntent")
def nothing():
	rewards = ['Good work. Keep it that way!', 'Glad to hear it!', 'That\'s good', 'Not for long!', 'Don\'t jinx it']
	message = rewards[random.randint(0, len(rewards)-1)]
	return statement(message)

@ask.intent('AMAZON.CancelIntent')
def cancel():
	return statement('Glad you\'ve found it.')

@ask.intent('AMAZON.HelpIntent')
def help():
	return statement('This skill helps you to find lost kit. Just tell me what you\'ve lost')

@ask.intent('AMAZON.StopIntent')
def stop():
	return statement('Glad you\'ve found it.')

@ask.intent('AMAZON.NavigateHomeIntent')
def home():
	return statement('Glad you\'ve found it.')

if __name__ == '__main__':
	app.run()