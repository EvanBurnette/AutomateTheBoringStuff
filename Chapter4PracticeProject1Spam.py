def listToString(listArg):
    """Take a list as argument."""
    """Returns comma separated string with <and> before last item."""
    buildStr = ''
    for i in range(len(listArg) - 1):
        buildStr = buildStr + listArg[i] + ', '

    buildStr = buildStr + 'and ' + listArg[-1]
    return buildStr


spam = ['apples', 'bananas', 'tofu', 'cats']

print(listToString(spam))
