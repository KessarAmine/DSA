def tournamentWinner(competitions, results):
    teams = []
    winner = []
    for games in competitions:
        for team in games:
            if [team, 0] not in teams:
                teams.append([team, 0])
    games = len(competitions)
    i = 0
    for i in range(games):
        game = competitions[i]
        if results[i] == 1:
            for team in teams:
                if team[0] == game[0]:
                    team[1] +=3
        else:
            for team in teams:
                if team[0] == game[1]:
                    team[1] +=3
    for team in teams:
        if not winner:
            winner = team
        else:
            if winner[1] < team[1]:
                winner = team
    print("winner is {} with {} points".format(winner[0], winner[1]))
    return winner[0]
