from typing import List, Optional
import click
from src.sequence_generator import SequenceGenerator
from src.cli.utils import safe_eval


@click.command(context_settings={"show_default": True})
@click.help_option("-h", "--help")
@click.option(
    "-l",
    "--length",
    default=10,
    type=int,
    help="Length of sequence",
)
@click.option(
    "-L",
    "--lambda_str",
    type=str,
    help="String representation of a lambda function",
)
@click.option(
    "-i",
    "--indices",
    is_flag=True,
    default=False,
    help="Include indices in sequence.",
)
@click.option(
    "-n",
    "--nums",
    default=[1, 1],
    multiple=True,
    type=int,
    help="Sequence initiators",
)
def primes(
    nums: List[int], length: int, indices: bool, lambda_str: Optional[str] = None
):
    """
    Return prime numbers from a generated sequence
    """
    generator = None
    if lambda_str:
        lambda_eval = safe_eval(lambda_str)
        generator = SequenceGenerator(list(nums), lambda_eval)
    else:
        generator = SequenceGenerator(list(nums))
    sequence = generator.generate_prime_sequence(length, include_indices=indices)
    print(sequence)
