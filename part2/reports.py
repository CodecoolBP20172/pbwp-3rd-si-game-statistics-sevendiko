def most_played(filename):
    with open(filename) as f:
        games = f.readlines()
        sell = [sell.split('\t')[1] for sell in games]
        title = [title.split('\t')[0] for title in games]
        sellbytitle = dict(zip(title, sell))
        max_key = max(sellbytitle, key=lambda k: sellbytitle[k])
        print(max_key)
        


most_played('game_stat.txt')

"""
maxsell = str(int(max(map(float, sell))))
        for game in games:    
            if maxsell in game:
                game = str(games.split('\t')[0])
        print(game)
"""