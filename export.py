from reports import count_games, decide, get_latest, get_genres, get_line_number_by_title, count_by_genre, sort_abc

a = count_games('game_stat.txt')
b = decide('game_stat.txt', '2011')
c = get_latest('game_stat.txt')
d = count_by_genre('game_stat.txt', 'Survival game')
e = get_line_number_by_title('game_stat.txt', 'GTA V')
f = sort_abc('game_stat.txt')
g = get_genres('game_stat.txt')


def export(filename="export.txt"):
    with open(filename, 'w') as output:
        output.write('{}\n{}\n{}\n{}\n{}\n{}\n{})'.format(str(a), str(b), str(c), str(d), str(e), str(f), str(g)))
    print("File succesfully written!")

export("export.txt")