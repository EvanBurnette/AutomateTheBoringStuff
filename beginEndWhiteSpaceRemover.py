#! python3
"""beginEndWhiteSpaceRemover - removes whitespace from a string beginning and
end in the clipboard.
"""


import pyperclip

userText = pyperclip.paste()

def cleanBeginningWhitespace(text):
    """Remove whitespace from beginning of a string."""
    for i in range(len(text)):
        if not text[i].isspace() and text[i-1].isspace():
            text = text[i:]
            return text


userText = cleanBeginningWhitespace(userText)
userText = userText[::-1]
userText = cleanBeginningWhitespace(userText)
userText = userText[::-1]

pyperclip.copy(userText)
