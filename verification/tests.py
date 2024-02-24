"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""
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
            "input": [tuple(range(2, 22)), 54],
            "answer": [tuple(range(2, 22)), 54],
        },
        {
            "input": [tuple(range(1, 17)), 35],
            "answer": [tuple(range(1, 17)), 35],
        },
    ],
}
