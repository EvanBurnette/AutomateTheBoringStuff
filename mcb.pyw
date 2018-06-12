#! python3
# mcb.pyw - Save and loads pieces of text to clipboard.
# Usage:    py.exe mcb.pyw save <keyword> - Saves clipboard to keyboard.
#           py.exe mcb.pyw delete <keyword> - deletes a key:value pair from shelf
#           py.exe mcb.pyw delete all - deletes all key:value pairs from shelf
#           py.exe mcb.pyw <keyword> - Loads value of keyword to clipboard.
#           py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mdb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2].lower() == 'all':
        for k in mcbShelf:
            del mcbShelf[k]
    else:
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
