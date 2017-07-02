import math as m
from collections import Counter


def get_most_played(filename):
    with open(filename) as f:
        games = f.readlines()
        sell = [sell.split('\t')[1] for sell in games]
        sell = map(float, sell)
        title = [title.split('\t')[0] for title in games]
        sellbytitle = dict(zip(title, sell))
        max_key = max(sellbytitle, key=lambda k: sellbytitle[k])
        return max_key


def sum_sold(filename):
    with open(filename) as f:
        games = f.readlines()
        sell = [sell.split('\t')[1] for sell in games]
        sell = sum(map(float, sell))
        return sell


def get_selling_avg(filename):
    with open(filename) as fi:
        countgames = sum(1 for _ in fi)
    with open(filename) as f:
        games = f.readlines()
        sell = [sell.split('\t')[1] for sell in games]
        sell = sum(map(float, sell))
        avgsell = sell / countgames
        return avgsell


def count_longest_title(filename):
    with open(filename) as f:
        games = f.readlines()
        titles = [title.split('\t')[0] for title in games]
        titles = max(titles, key=len)
        return len(titles)


def get_date_avg(filename):
    with open(filename) as fi:
        countgames = sum(1 for _ in fi)
    with open(filename) as f:
        games = f.readlines()
        dates = [date.split('\t')[2] for date in games]
        dates = sum(map(int, dates))
        avgdate = dates / countgames
        return m.ceil(avgdate)


def get_game(filename, title):
    properties = []
    with open(filename) as f:
        games = f.readlines()
        titles = [title.split('\t')[0] for title in games]
        for prop in games:
            if title in prop:
                p = prop
                p = p.replace('\t', ', ')
                p = p.replace('\n', '')
                properties.append(p)
                return(properties)


def count_grouped_by_genre(filename):
    with open(filename) as f:
        games = f.readlines()
        genres = [genre.split('\t')[3] for genre in games]
        result = Counter(genres)
        return result
