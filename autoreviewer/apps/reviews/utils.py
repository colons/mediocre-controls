from os.path import join, dirname
from random import random, choice

from django.conf import settings


def review(game):
    score = random()

    reviewed = {
        'score': score * settings.MAX_SCORE,
        'summary': u'I thought it was {}.'.format(
            random_summary_for(score)
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


def random_summary_for(score):
    summaries = []
    for line in lines_from('summaries'):
        range_str, summary = line.split(' ', 1)
        low, high = [float(n)/settings.MAX_SCORE
                     for n in range_str.split('-')]
        if low <= score <= high:
            summaries.append(summary)

    return choice(summaries)


def get_accolade(positive):
    quality = random_line_from('qualities')
    evaluation = random_line_from('positive' if positive else 'negative')
    return ' '.join((evaluation, quality)).capitalize()


def lines_from(slug):
    with open(join(dirname(__file__), 'corpus', '{}.txt'.format(slug))) as f:
        return [l.strip() for l in f.readlines() if l.strip()]


def random_line_from(slug):
    return choice(lines_from(slug))
