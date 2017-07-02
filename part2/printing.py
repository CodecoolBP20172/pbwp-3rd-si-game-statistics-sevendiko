from pprint import pprint
from reports import get_most_played, sum_sold, get_selling_avg, count_longest_title, get_date_avg, get_game

pprint(get_most_played('game_stat.txt'))
pprint(sum_sold('game_stat.txt'))
pprint(get_selling_avg('game_stat.txt'))
pprint(count_longest_title('game_stat.txt'))
pprint(get_date_avg('game_stat.txt'))
pprint(get_game('game_stat.txt', 'The Sims 3'))
