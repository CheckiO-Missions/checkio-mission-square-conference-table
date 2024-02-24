"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""
from random import randint, choice


def make_random_tests(*side_lengths):
    for side_length in side_lengths:
        desks = []
        connect_type = choice([[0, 0, 2, 2], [0, 1, 1, 2], [1, 1, 1, 1]])
        for ct in connect_type:
            rest = side_length - ct
            while True:
                cut = randint(1, 60)
                if rest - cut > 0 and len(desks) < 20:
                    rest -= cut
                    desks.append(cut)
                else:
                    desks.append(rest)
                    break
        for _ in range(20 - len(desks)):
            desks.append(randint(1, side_length))
            if not randint(0, 10):
                break
        yield {'input': [desks, side_length],
               'answer': [desks, side_length]}


TESTS = {
    "Basics": [
        {
            "input": [(1, 2, 2, 3, 4), 4],
            "answer": [(1, 2, 2, 3, 4), 4],
        },
        {
            "input": [(3, 3, 3, 3), 4],
            "answer": [(3, 3, 3, 3), 4],
        },
        {
            "input": [(1, 2, 2, 3, 3, 4, 5), 5],
            "answer": [(1, 2, 2, 3, 3, 4, 5), 5],
        },
        {
            "input": [(1, 2, 3, 4, 5, 6), 6],
            "answer": [(1, 2, 3, 4, 5, 6), 6],
        },
        {
            "input": [(1, 2, 3, 4, 5, 6, 7), 8],
            "answer": [(1, 2, 3, 4, 5, 6, 7), 8],
        },
        {
            "input": [(1, 2, 3, 4, 5, 6, 7, 8), 10],
            "answer": [(1, 2, 3, 4, 5, 6, 7, 8), 10],
        },
    ],
    "Extra": [
        {
            "input": [tuple(range(1, 17)), 35],
            "answer": [tuple(range(1, 17)), 35],
        },
        {
            "input": [tuple(range(2, 22)), 54],
            "answer": [tuple(range(2, 22)), 54],
        },
    ],
    "Random": list(make_random_tests(3, 4, 5, 10, 15, 20, 30, 40, 50))
}
