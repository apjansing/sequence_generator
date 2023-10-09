from src.sequence_generator import SequenceGenerator


def test_generate_sequence():
    """
    This test generates a fibonacci-like sequence of numbers
    """
    assert SequenceGenerator(2, 4).generate_sequence(5) == [2, 4, 6, 10, 16]
    assert SequenceGenerator(1, 2).generate_sequence(3) == [1, 2, 3]
    assert SequenceGenerator(0, 0).generate_sequence(5) == [0, 0, 0, 0, 0]


def test_is_prime():
    """
    This test checks if a number is prime
    """
    assert SequenceGenerator(1, 1).is_prime(2) is True
    assert SequenceGenerator(1, 1).is_prime(3) is True
    assert SequenceGenerator(1, 1).is_prime(4) is False
    assert SequenceGenerator(1, 1).is_prime(11) is True
    assert SequenceGenerator(1, 1).is_prime(15) is False


def test_generate_prime_sequence():
    """
    This test generates the first n numbers in a sequence and returns a list of tuples
    where the first element is the index of the number in the sequence and the second
    element is the number itself. The index is a prime number.
    """
    assert SequenceGenerator(2, 3).generate_prime_sequence(5) == [
        (2, 3),
        (3, 5),
        (5, 13),
    ]
    assert SequenceGenerator(3, 5).generate_prime_sequence(10) == [
        (2, 5),
        (3, 8),
        (5, 21),
        (7, 55),
    ]
    assert SequenceGenerator(2, 11).generate_prime_sequence(101) == [
        (2, 11),
        (3, 13),
        (5, 37),
        (7, 98),
        (11, 673),
        (13, 1762),
        (17, 12077),
        (19, 31618),
        (23, 216713),
        (29, 3888757),
        (31, 10180898),
        (37, 182688802),
        (41, 1252167677),
        (43, 3278217538),
        (47, 22469237273),
        (53, 403194103237),
        (59, 7235024620993),
        (61, 18941540367202),
        (67, 339892150743298),
        (71, 2329655458722473),
        (73, 6099117173012162),
        (79, 109444216963475618),
        (83, 750141822684015313),
        (89, 13460748837304345757),
        (97, 632368666673421753602),
        (101, 4334319321640991403877),
    ]
    assert not SequenceGenerator(0, 0).generate_prime_sequence(0)
