# django-home-station
Django-based home station which will integrate a number of different tasks in the form of django apps.

## Objectives
1. Learn Django. (Follow TDD as much as possible) 
2. Exploit the Google API
3. Learn how to interact with Alexa
4. Make use of an old tablet.
5. Organize photos 

## Web Photo Frame
First app to create covers two features:

1) Download images from a personal google drive account. 
- This feature will be develop as an independent feature based on the branch develop-google-api.
- Exact query format is yet to be defined

2) Create a Django app consisting on two main urls. This feature will be based on the branch develop-photo-frame 

2.1) A user database manipulation view to arrange photos and give them metadata based on a number of possible inputs.
Since Photos will be provided by the google API, work with a local set of photos and a local dict of name:google_id value pairs
Photos properties:
- Name
- Location (It should be validated as a real city/country/town etc)
- People in it. A list of names (previously/in-site configured)
- Date
- Description
- Points (Scale  0-10)
- google_id: holds id provided by google drive
- id: Internal id (automatic)
Person properties:
- Name
- Group (friends, family, pets, nature, others)

2.2) A single interface where photos will be shown on a presentation-style format.
- Default behaviour will be to randomly pick pictures from the database and display them during a fixed duration. 
- Via Combo box for each propert set on 2.1, user will be able to filter only those that match se selected properties.
- There must exists an extra combo box to select for how long the pictures will remain on the page (5s, 15s, 30s, 45s, 60s) 
- Page outline is yet to be decided. Initially, all combo boxes will appear on a single menu placed on the top of the page.
- Description and list of people's name in it should appear on the bottom of the picture (Add a checkbox to the menu to add this or not)

## Alexa client

This app will consists on two main features.

1) An Alexa skill will contact this client in order to switch on/off the Arduino Client
2) It is desired to study if it's possible to query Alexa for state of devices. (Focus on obtaining for how long a device was on/off)

## Arduino Client
Since this service will be implemented nearby an existing Arduino-based station, it is desired to be able to work as gateway between Alexa and bluetooth.
As for now, It should be able to despatch ON/OFF commands for a string of leds connected to the arduino.


# Developer guidelines

1. No direct pushing to master or develop on this repo
2. All alexa related work should branch off of develop-alexa-integration
3. All photo frame related work should branch off of develop-photo-frame
4. All google related work should branch off of develop-google-api
5. Use squash as merge option on all PRs and wait to have at least 1 approval.
