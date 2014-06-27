from os.path import join, dirname
from random import random, choice


def review(game):
    score = random()

    reviewed = {
        'score': score * 10,
        'summary': u'I thought it was {}.'.format(
            random_line_from('summaries')
        ),
        'pros': [
            get_accolade(True) for i in
            xrange(int(random() * score * 5))
        ],
        'cons': [
            get_accolade(False) for i in
            xrange(int(random() * (1 - score) * 5))
        ],
    }

    reviewed.update(game)
    return reviewed


def get_accolade(positive):
    quality = random_line_from('qualities')
    evaluation = random_line_from('positive' if positive else 'negative')
    return ' '.join((evaluation, quality)).capitalize()


def random_line_from(slug):
    with open(join(dirname(__file__), 'corpus', '{}.txt'.format(slug))) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    return choice(lines)
