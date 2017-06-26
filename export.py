from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title, sort_abc, get_genres
from pprint import pprint

pprint(count_games("/home/sevendiko/Asztal/codecool/pbwp-3rd-si-game-statistics-sevendiko/game_stat.txt"))
pprint(decide("/home/sevendiko/Asztal/codecool/pbwp-3rd-si-game-statistics-sevendiko/game_stat.txt", '1976'))
pprint(get_latest("/home/sevendiko/Asztal/codecool/pbwp-3rd-si-game-statistics-sevendiko/game_stat.txt"))
pprint(count_by_genre("/home/sevendiko/Asztal/codecool/pbwp-3rd-si-game-statistics-sevendiko/game_stat.txt", 'Survival game'))
pprint(get_line_number_by_title("/home/sevendiko/Asztal/codecool/pbwp-3rd-si-game-statistics-sevendiko/game_stat.txt", 'GTA V'))
pprint(get_genres("/home/sevendiko/Asztal/codecool/pbwp-3rd-si-game-statistics-sevendiko/game_stat.txt"))
pprint(sort_abc("/home/sevendiko/Asztal/codecool/pbwp-3rd-si-game-statistics-sevendiko/game_stat.txt"))
