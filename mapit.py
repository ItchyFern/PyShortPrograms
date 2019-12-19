#! python3
# mapit.py - Launches a map in the browser using an address from
# the command line or clipboard
# This was created using a tutorial from: Automate The Boring Stuff with Python

import webbrowser, sys
import pyperclip

if len(sys.argv) > 1:
    #get address from command line
    address = " ".join(sys.argv[1:])

webbrowser.open("https://www.google.com/maps/place/" + address)
