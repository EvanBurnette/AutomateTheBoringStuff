#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

else:
    # Grab a street address from clipboard
    address = pyperclip.paste()
# Open the web browser to the Google Maps page for the address.
webbrowser.open('https://www.google.com/maps/place/' + address)

print(address)
