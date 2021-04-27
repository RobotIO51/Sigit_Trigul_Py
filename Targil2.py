def checkWin(game):
    for x in range(3):
        if game[x][0] == game[x][1] == game[x][2]:
            return game[x][0]
        if game[0][x] == game[1][x] == game[2][x]:
            return game[0][x]

    if game[0][0] == game[1][1] == game[2][2]:
        return game[0][0]
    if game[0][2] == game[1][1] == game[2][0]:
        return game[0][0]
    return "Tie"


if __name__ == '__main__':
    game = [[1, 2, 0],
            [1, 2, 1],
            [2, 2, 1]]

    print(checkWin(game))

