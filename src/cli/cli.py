import click

from .pure import pure
from .prime import primes
from .prime_indices import prime_indices


@click.group()
def generate_sequence():
    """
    This function generates a fibonacci-like sequence of numbers based on initial values and a generator function
    """
    pass


generate_sequence.add_command(pure)
generate_sequence.add_command(primes)
generate_sequence.add_command(prime_indices, name="prime-indices")
