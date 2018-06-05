"""Replicate the str.strip() function with regular expressions."""
import re
import pyperclip


def stripRe(userText):
    """Replicate the str.strip() function with regular expressions."""
    endsSpaceRe = re.compile(r'^\s+|\s+$')
    userText = endsSpaceRe.sub('', userText)
    return userText


userClip = pyperclip.paste()
userClip = stripRe(userClip)
pyperclip.copy(userClip)
