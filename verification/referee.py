from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io_template import CheckiOReferee
# from checkio.referees.checkers import to_list

from tests import TESTS

from itertools import chain
from collections import Counter


def check(input, result):
    try:
        desks, side_length = input
        if not Counter(chain(*result)) - Counter(desks):
            difs = [side_length - sum(r) for r in result]
            if difs in [[1, 1, 1, 1], [2, 0, 2, 0], [0, 2 ,0, 2]] or sorted(difs) == [0, 1, 1, 2]:
                return True, (result, 'success')
        return False, (result, 'fail')
    except Exception:
        return False, (result, 'fail')

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        checker=check,
        function_name={
            "python": "square_conference_table",
            "js": "squareConferenceTable"
        },
        cover_code={
            'python-3': {},
            'js-node': {
                # "dateForZeros": True,
            }
        }
    ).on_ready)
