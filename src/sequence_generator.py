from sympy import isprime
from typing import List
from loguru import logger
import pandas as pd
from os import path


def write_sequence(func):
    """
    Writes or appends a sequence to a file if a filename is provided
    :param sequence: The sequence to write
    """

    def wrapper(self, *args, **kwargs):
        sequence = func(self, *args, **kwargs)
        self.sequence = sequence
        if self.filename:
            if path.exists(f"{self.filename}.csv") and not self.continue_sequence:
                logger.warning(
                    f"File {self.filename}.csv already exists. Overwriting file"
                )
            pd.DataFrame(sequence).to_csv(
                f"{self.filename}.csv",
                mode="a" if self.continue_sequence else "w",
                header=False,
            )
        return sequence

    return wrapper


class SequenceGenerator:
    """
    This class generates a fibonacci-like sequence
    :param initial_values: The first n numbers in the sequence
    :param generator: A function that performs an operation on the last n numbers in the sequence
    """

    def __init__(
        self,
        initial_values: List = [1, 1],
        generator=(lambda x, y: x + y),
        filename="sequence",
        continue_sequence: bool = False,
    ):
        self.initial_values = initial_values
        self.generator = generator if generator else (lambda x, y: x + y)
        self.filename = filename
        self.continue_sequence = continue_sequence
        self.sequence = []
        self.value_type = type(self.initial_values[0])

    def get_sequence(self, tail: int = -1):
        """
        Reads a sequence from a file if a filename is provided
        :return: The sequence
        """

        def get_num_lines(fname):
            i = 0
            with open(fname, "r", encoding="UTF-8") as f:
                for i, _ in enumerate(f):
                    pass
            return i + 1

        if self.filename and path.exists(f"{self.filename}.csv"):
            num_lines = get_num_lines(f"{self.filename}.csv")
            with open(f"{self.filename}.csv", "r", encoding="UTF-8") as f:
                if tail > 0:
                    seq = pd.read_csv(
                        f, header=None, skiprows=range(1, num_lines - tail)
                    )
                seq = pd.read_csv(f, header=None)
                logger.info(seq)
                return seq[1].tolist()
        else:
            return self.sequence

    def print_sequence(self):
        """
        Prints a sequence to the console from a file if a filename is provided,
        otherwise
        """
        sequence: pd.DataFrame = self.get_sequence()
        if sequence:
            logger.info(sequence)
        else:
            logger.warning("No sequence has been generated yet")
            logger.info(sequence)

    def generate_sequence_(self, n):
        """
        An alternate method that generates a fibonacci-like sequence of numbers,
        but does not use the write_sequence decorator
        :param n: The number of numbers to generate
        :return: A list of numbers
        """
        sequence = self.initial_values.copy()
        for _ in range(n - len(self.initial_values)):
            # Generate the next number in the sequence by applying the generator
            # to the last n numbers where n is the length of initial values
            sequence.append(self.generator(*sequence[-len(self.initial_values) :]))
        return sequence

    @write_sequence
    def generate_sequence(self, n):
        """
        Generates a fibonacci-like sequence of numbers
        :param n: The number of numbers to generate
        :return: A list of numbers
        """
        return self.generate_sequence_(n)

    @write_sequence
    def generate_prime_index_sequence(self, n: int, include_indices: bool = False):
        """
        Generates a fibonacci-like sequence of numbers
        :param n: The number of numbers to generate
        :param include_indices: Whether to include indices in the sequence
        :return: A list of numbers where the indices are prime numbers
        """
        sequence: pd.DataFrame = self.generate_sequence_(n)
        prime_sequence = []
        for idx, num in enumerate(sequence):
            if isprime(idx + 1):
                if include_indices:
                    prime_sequence.append((idx + 1, num))
                else:
                    prime_sequence.append(num)
            if len(prime_sequence) == n:
                break
        return prime_sequence

    @write_sequence
    def generate_prime_sequence(self, n: int, include_indices: bool = False):
        """
        Generates a sequence of prime numbers based on the initial values and generator
        :param n: The number of numbers to generate
        :param include_indices: Whether to include indices in the sequence
        :return: A list of numbers where the indices are prime numbers
        """
        sequence = self.generate_sequence_(n)
        prime_sequence = []
        for idx, num in enumerate(sequence):
            if isprime(num):
                if include_indices:
                    prime_sequence.append((idx + 1, num))
                else:
                    prime_sequence.append(num)
            if len(prime_sequence) == n:
                break
        return prime_sequence
