from random import random


def review(game):
    return u'{} - {:.1f}/10'.format(game['name'], random() * 10)
