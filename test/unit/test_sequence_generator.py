from src.sequence_generator import SequenceGenerator


def test_generate_sequence():
    """
    This test generates a fibonacci-like sequence of numbers
    """
    assert SequenceGenerator([2, 4]).generate_sequence(5) == [2, 4, 6, 10, 16]
    assert SequenceGenerator([1, 2]).generate_sequence(3) == [1, 2, 3]
    assert SequenceGenerator([0, 0]).generate_sequence(5) == [0, 0, 0, 0, 0]


def test_generate_sequence_with_generator():
    """
    This test generates sequences of numbers based off of a generator function
    """
    assert SequenceGenerator(
        [1, 1, 1],
        generator=lambda x, y, z: x + y + z,
    ).generate_sequence(10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    assert SequenceGenerator(
        [40], generator=lambda x: x // 2 if x % 2 == 0 else 3 * x + 1
    ).generate_sequence(9) == [40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert SequenceGenerator(
        [1, 2], generator=lambda x, y: x + y - 3 if (x + y) % 2 == 0 else x + y
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


def test_generate_prime_index_sequence():
    """
    This test generates the first n numbers in a sequence and returns a list of tuples
    where the first element is the index of the number in the sequence and the second
    element is the number itself. The index is a prime number.
    """
    assert SequenceGenerator([2, 3]).generate_prime_index_sequence(5) == [3, 5, 13]
    assert SequenceGenerator([3, 5]).generate_prime_index_sequence(10, True) == [
        (2, 5),
        (3, 8),
        (5, 21),
        (7, 55),
    ]
    assert SequenceGenerator(
        [1, 2], generator=lambda x, y: x + y - 3 if (x + y) % 2 == 0 else x + y
    ).generate_prime_index_sequence(20, True) == [
        (2, 2),
        (3, 3),
        (5, 5),
        (7, 9),
        (11, 45),
        (13, 113),
        (17, 757),
        (19, 1977),
    ]
    assert not SequenceGenerator([0, 0]).generate_prime_index_sequence(0)


def test_generate_prime_sequence():
    """
    This test generates the first n numbers in a sequence and returns a list of tuples
    where the first element is the index of the number in the sequence and the second
    element is the number itself. The index is a prime number.
    """
    assert SequenceGenerator([2, 3]).generate_prime_sequence(5) == [2, 3, 5, 13]
    assert SequenceGenerator([3, 5]).generate_prime_sequence(10, True) == [
        (1, 3),
        (2, 5),
        (4, 13),
        (8, 89),
        (10, 233),
    ]
    assert SequenceGenerator(
        [1, 2], generator=lambda x, y: x + y - 3 if (x + y) % 2 == 0 else x + y
    ).generate_prime_sequence(20, True) == [
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 5),
        (6, 7),
        (8, 13),
        (9, 19),
        (10, 29),
        (12, 71),
        (13, 113),
        (14, 181),
        (17, 757),
        (18, 1223),
    ]
    assert not SequenceGenerator([0, 0]).generate_prime_sequence(0)
