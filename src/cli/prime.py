from typing import Tuple
import click
from src.sequence_generator import SequenceGenerator


@click.command()
@click.help_option("-h", "--help")
@click.option(
    "-n",
    "--nums",
    default=[1, 1],
    nargs=2,
    type=int,
    show_default=True,
    help="Sequence initiators (2 numbers)",
)
@click.option(
    "-l",
    "--length",
    default=10,
    type=int,
    help="Length of sequence",
)
@click.option(
    "-i",
    "--indices",
    is_flag=True,
    show_default=True,
    default=False,
    help="Include indices in sequence.",
)
def primes(nums: Tuple[int, int], length: int, indices: bool):
    """
    This function generates a fibonacci-like sequence of numbers
    """
    sequence = SequenceGenerator(nums[0], nums[1]).generate_prime_sequence(
        length, indices
    )
    print(sequence)
