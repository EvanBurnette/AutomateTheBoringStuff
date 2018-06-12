"""strongPassRe.py checks for strong passwords."""

import re


def isStrongPass(userPass):
    """Return True for strong password, Return False for weak password."""
    #  regular expression for 8 characters or more
    char8plusRe = re.compile(r'''.{8,}''')
    #  regex for both upper and lowercase
    upperLowerRe = re.compile(r'''[a-z]*[A-Z]|[A-Z]*[a-z]''')
    #  regex for at least one digit
    digitRe = re.compile(r'''\d''')

    if char8plusRe.search(userPass) is not None:
        if upperLowerRe.search(userPass) is not None:
            if digitRe.search(userPass) is not None:
                return True
    else:
        return False


while True:
    print("Enter a password to check for strength: (leave blank to quit)\n")
    userIn = input()
    if userIn == '':
        break
    if (isStrongPass(userIn)):
        print(userIn + " is a strong password")
    else:
        print(userIn + " is not a strong password")
        print("""Strong passwords are at least 8 characters,
              have a mix of upper and lowercase letters,
              and at least 1 digit.\n""")
