import sys, random


def combinations(l):
    if not l:
        return [[]]
    c = combinations(l[1:])
    return c + [[l[0]] + x for x in c]


def check_solution(l):
    return all(l[i] < l[i + 1] for i in range(len(l) - 1))


def find_solution(cdeck):
    c = combinations(cdeck)
    maximal = []
    for x in c:
        if len(x) > 0:
            if check_solution([e[1] for e in x]):
                if len(x) > len(maximal):
                    maximal = x
    return maximal


max_size = int(sys.argv[1])
num_cards = int(sys.argv[2])

card_type = ['artifact', 'conspiracy', 'creature', 'enchantment', 'instant', 'land',
             'phenomenon', 'plane', 'planeswalker', 'scheme', 'sorcery',
             'tribal', 'vanguard']

deck = []
for x in range(num_cards):
    deck.append((random.sample(card_type, 1)[0], random.randint(1, max_size)))
print('\n'.join([x + ' ' + str(y) for x, y in deck]))

print('\n'.join([x + ' ' + str(y) for x, y in find_solution(deck)]), file=sys.stderr)
