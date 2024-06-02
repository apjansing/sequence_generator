import os
from sequence_generator import SequenceGenerator
import pytest


def test_generate_sequence(tmpdir):
    """
    This test generates a fibonacci-like sequence of numbers
    """
    assert SequenceGenerator([2, 4], filename=tmpdir.join("test")).generate_sequence(5) == [
        2,
        4,
        6,
        10,
        16,
    ]
    assert os.path.exists(tmpdir.join("test.csv"))
    assert os.path.exists(tmpdir.join("test.pickle"))

    assert SequenceGenerator([1, 2], filename=None).generate_sequence(3) == [1, 2, 3]
    assert SequenceGenerator([0, 0], filename=None).generate_sequence(5) == [
        0,
        0,
        0,
        0,
        0,
    ]


def test_generate_sequence_with_generator(tmpdir):
    """
    This test generates sequences of numbers based off of a generator function
    """
    assert SequenceGenerator([1, 1, 1], generator=lambda x, y, z: x + y + z, filename=tmpdir).generate_sequence(10) == [
        1,
        1,
        1,
        3,
        5,
        9,
        17,
        31,
        57,
        105,
    ]
    assert SequenceGenerator(
        [40], generator=lambda x: x // 2 if x % 2 == 0 else 3 * x + 1, filename=None
    ).generate_sequence(9) == [40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert SequenceGenerator(
        [1, 2],
        generator=lambda x, y: x + y - 3 if (x + y) % 2 == 0 else x + y,
        filename=None,
    ).generate_sequence(10) == [
        1,
        2,
        3,
        5,
        5,
        7,
        9,
        13,
        19,
        29,
    ]
