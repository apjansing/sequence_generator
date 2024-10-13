import os
import pytest
from sequence_generator.sequence_generator import SequenceGenerator


def test_generate_sequence(tmpdir):
    '''
    This test generates a fibonacci-like sequence of numbers
    '''
    os.chdir(tmpdir)
    SequenceGenerator([2, 4], filename='test').generate_sequence(5)
    assert os.path.exists('test.csv')
    assert os.path.exists('test.pickle')
    with open('test.csv', 'r', encoding='UTF-8') as f:
        assert f.read().splitlines() == [
            '2',
            '4',
            '6',
            '10',
            '16',
        ]

    SequenceGenerator([1, 2]).generate_sequence(3)
    with open('sequence.csv', 'r', encoding='UTF-8') as f:
        assert f.read().splitlines() == [
            '1',
            '2',
            '3',
        ]

    with pytest.raises(FileExistsError):
        SequenceGenerator([0, 0]).generate_sequence(5)


def test_generate_sequence_with_generator(tmpdir):
    '''
    This test generates sequences of numbers based off of a generator function
    '''
    os.chdir(tmpdir)
    SequenceGenerator([1, 1, 1], generator=lambda x, y, z: x + y + z, filename='triple_1').generate_sequence(10)
    with open('triple_1.csv', 'r', encoding='UTF-8') as f:
        assert f.read().splitlines() == [
            '1',
            '1',
            '1',
            '3',
            '5',
            '9',
            '17',
            '31',
            '57',
            '105',
        ]

    SequenceGenerator(
        [40],
        generator=lambda x: x // 2 if x % 2 == 0 else 3 * x + 1,
        filename='collatz',
    ).generate_sequence(9)
    with open('collatz.csv', 'r', encoding='UTF-8') as f:
        assert f.read().splitlines() == [
            '40',
            '20',
            '10',
            '5',
            '16',
            '8',
            '4',
            '2',
            '1',
        ]

    SequenceGenerator(
        [1, 2],
        generator=lambda x, y: x + y - 3 if (x + y) % 2 == 0 else x + y,
        filename='even_odd',
    ).generate_sequence(10)
    with open('even_odd.csv', 'r', encoding='UTF-8') as f:
        assert f.read().splitlines() == [
            '1',
            '2',
            '3',
            '5',
            '5',
            '7',
            '9',
            '13',
            '19',
            '29',
        ]
