import click
from .pure import pure
from .prime import primes


@click.group()
@click.help_option("-h", "--help")
def generate_sequence():
    """
    This function generates a fibonacci-like sequence of numbers
    """
    pass


generate_sequence.add_command(pure)
generate_sequence.add_command(primes)
