from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title, sort_abc, get_genres
from pprint import pprint

pprint(count_games("game_stat.txt"))
pprint(decide("game_stat.txt", '1976'))
pprint(get_latest("game_stat.txt"))
pprint(count_by_genre("game_stat.txt", 'Survival game'))
pprint(get_line_number_by_title("game_stat.txt", 'GTA V'))
pprint(get_genres("game_stat.txt"))
pprint(sort_abc("game_stat.txt"))
