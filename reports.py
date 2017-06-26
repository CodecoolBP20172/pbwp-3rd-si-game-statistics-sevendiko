def count_games(filename):
    with open(filename) as f:
        games = sum(1 for _ in f)
        return games


def decide(filename, year):
    with open(filename) as f:
        games = f.readlines()
        dates = [date.split('\t')[2] for date in games]
        for year in dates:
            if year not in dates:
                return False
            else:
                return True


def get_latest(filename):
    with open(filename) as f:
        games = f.readlines()
        latest = max([year.split('\t')[2] for year in games])
        for item in games:
            if latest in item:
                game = str(item.split('\t')[0])
        return game


def count_by_genre(filename, genre):
    with open(filename) as f:
        games = f.readlines()
        genres = [genres.split('\t')[3] for genres in games]
        if genre in genres:
            counted_by_genre = genres.count(genre)
            return counted_by_genre


def get_line_number_by_title(filename, title):
    with open(filename) as f:
        games = f.readlines()
        titles = [title.split('\t')[0] for title in games]
        try:
            line_number_of_title = titles.index(title) + 1
            return line_number_of_title
        except ValueError:
            return ('There is no game from the given year')


def sort_abc(filename):
    with open(filename) as f:
        games = f.readlines()
        titles = sorted(title.split('\t')[0] for title in games)
        return titles


def get_genres(filename):
    with open(filename) as f:
        games = f.readlines()
        genres = {genres.split('\t')[3] for genres in games}
        return sorted(genres, key=str.swapcase)

