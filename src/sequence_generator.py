from sympy import isprime


class SequenceGenerator:
    """
    This class generates a fibonacci-like sequence
    :param num1: The first number in the sequence
    :param num2: The second number in the sequence
    """

    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def generate_sequence(self, n):
        """
        Generates a fibonacci-like sequence of numbers
        :param n: The number of numbers to generate
        :return: A list of numbers
        """
        sequence = [self.num1, self.num2]
        for i in range(2, n):
            sequence.append(sequence[i - 1] + sequence[i - 2])
        return sequence

    def generate_prime_sequence(self, n: int, include_indices: bool = False):
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
