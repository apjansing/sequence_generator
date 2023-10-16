from sympy import isprime
from typing import List


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
    ):
        self.initial_values = initial_values
        self.generator = generator

    def generate_sequence(self, n):
        """
        Generates a fibonacci-like sequence of numbers
        :param n: The number of numbers to generate
        :return: A list of numbers
        """
        sequence = self.initial_values.copy()
        for _ in range(len(self.initial_values), n):
            sequence.append(self.generator(*sequence[-len(self.initial_values) :]))
        return sequence

    def generate_prime_index_sequence(self, n: int, include_indices: bool = False):
        """
        Generates a fibonacci-like sequence of numbers
        :param n: The number of numbers to generate
        :param include_indices: Whether to include indices in the sequence
        :return: A list of numbers where the indices are prime numbers
        """
        sequence = self.generate_sequence(n)
        prime_sequence = []
        for i, num in enumerate(sequence):
            if isprime(i + 1):
                if include_indices:
                    prime_sequence.append((i + 1, num))
                else:
                    prime_sequence.append(num)
            if len(prime_sequence) == n:
                break
        return prime_sequence

    def generate_prime_sequence(self, n: int, include_indices: bool = False):
        """
        Generates a sequence of prime numbers based on the initial values and generator
        :param n: The number of numbers to generate
        :param include_indices: Whether to include indices in the sequence
        :return: A list of numbers where the indices are prime numbers
        """
        sequence = self.generate_sequence(n)
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
