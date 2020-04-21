# django-home-station
Django-based home station which will integrate a number of different tasks.

## Web Photo Frame
First service to cover downloading images from google drive and showing them on a presentation-style format.

Objectives:
1. Make use of an old tablet.
2. Organize photos based on date, people in it and possible a points-based wheight system for duration etc


## Arduino Client
Since this service will be implemented nearby an existing Arduino-based station, it is desired to be able to work as gateway between Alexa and bluetooth.
As for now, It should be able to despatch ON/OFF commands for a string of leds connected to the arduino.


# Developer guidelines

1. No direct pushing to master or develop on this repo
2. All alexa related work should branch off of develop-alexa 
3. All django related work should branch off of develop-django
4. All google related work should branch off of develop-google
5. Use squash as merge option on all PR and wait to have at least 1 approval.
