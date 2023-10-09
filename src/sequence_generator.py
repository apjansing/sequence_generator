class SequenceGenerator:
    """
    This class generates a fibonacci-like sequence
    :param num1: The first number in the sequence
    :param num2: The second number in the sequence
    """

    def __init__(self, num1, num2):
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

    def is_prime(self, num):
        """
        Checks if a number is prime
        :param num: The number to check
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_prime_sequence(self, n):
        """
        Generates a fibonacci-like sequence of numbers
        :param n: The number of numbers to generate
        :return: A list of numbers where the indices are prime numbers
        """
        sequence = self.generate_sequence(n)
        prime_sequence = []
        for i, num in enumerate(sequence):
            if self.is_prime(i + 1):
                prime_sequence.append((i + 1, num))
            if len(prime_sequence) == n:
                break
        return prime_sequence
