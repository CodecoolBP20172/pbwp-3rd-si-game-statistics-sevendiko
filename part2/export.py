from reports import get_most_played, sum_sold, get_selling_avg, count_longest_title, get_date_avg, get_game, count_grouped_by_genre

a = get_most_played('game_stat.txt')
b = sum_sold('game_stat.txt')
c = get_selling_avg('game_stat.txt')
d = count_longest_title('game_stat.txt')
e = get_date_avg('game_stat.txt')
f = get_game('game_stat.txt', 'The Sims 3')
g = count_grouped_by_genre('game_stat.txt')


def export(filename="export.txt"):
    with open(filename, 'w') as output:
        output.write('{}\n{}\n{}\n{}\n{}\n{}\n{})'.format(str(a), str(b), str(c), str(d), str(e), str(f), str(g)))
    print("File succesfully written!")

export("export.txt")
