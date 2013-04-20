#!/usr/bin/python

# Import XBMC module
import xbmc
 
# First we need to create an object containing the getMusicInfoTag() class from XBMC.Player(). 
# This is in order to use the same instance of the class twice and not create a new class
# for every time we query for information. 
# This is a bit important to notice, as creating many instances is rarely
# a good thing to do (unless you need it, but not in this case).
 
tag = xbmc.Player().getMusicInfoTag()
 
# Now tag contains the getMusicInfoTag() class which then again contains song information.
# Now we use this object to get the data by calling functions within that class:
 
artist = tag.getArtist()
title = tag.getTitle()
 
# Now you have two strings containing the information. An example of what you could do next is to print it:
 
print "Playing: " + artist + " - " + title
 
# This will produce i.e: "Playing: AC/DC - Back in black"