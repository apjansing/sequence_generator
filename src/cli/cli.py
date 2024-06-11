import click

from .pure import pure


@click.group()
def generate_sequence():
    """
    This function generates a fibonacci-like sequence of numbers based on initial values and a generator function
    """
    pass


generate_sequence.add_command(pure)
