import collections
import random


def words():
    with open("input.txt") as f:
        for line in f:
            for word in line.split():
                yield word


def suffix_table(generator):
    suffixes = collections.defaultdict(list)
    w1, w2 = None, None
    for w3 in generator():
        suffixes[(w1, w2)].append(w3)
        w1, w2 = w2, w3
    suffixes[(w1, w2)].append(None)
    return suffixes


def generate_text(suffixes, n_words):
    w1, w2 = None, None
    count = 0
    while count < n_words:
        w3 = random.choice(suffixes[(w1, w2)])
        if w3 is None:
            w1, w2 = None, None
        else:
            yield w3
            count += 1
            w1, w2 = w2, w3


suffixes = suffix_table(words)
for w in generate_text(suffixes, n_words=100):
    print(w)
