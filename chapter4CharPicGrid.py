#! python3


def listToPicGrid(listArg):
    """Turn a list of lists into printed strings in output."""
    for i in range(len(listArg[0])):
        picStr = ''
        for j in range(len(listArg)):
            picStr += listArg[j][i]
        print(picStr)
    return


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

listToPicGrid(grid)
