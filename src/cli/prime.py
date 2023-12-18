from typing import List, Optional
import click
from src.sequence_generator import SequenceGenerator
from src.cli.utils import safe_eval
from .options import length, lambda_str, indices, nums, filename, continue_sequence


@click.command(context_settings={"show_default": True})
@click.help_option("-h", "--help")
@length
@lambda_str
@indices
@nums
@filename
@continue_sequence
def primes(
    nums: List[int],
    length: int,
    indices: bool,
    filename=filename,
    lambda_str: Optional[str] = None,
    continue_sequence: bool = False,
):
    """
    Return prime numbers from a generated sequence
    """
    generator = None
    if lambda_str:
        lambda_eval = safe_eval(lambda_str)
        generator = SequenceGenerator(
            list(nums),
            lambda_eval,
            filename=filename,
            continue_sequence=continue_sequence,
        )
    else:
        generator = SequenceGenerator(
            list(nums), filename=filename, continue_sequence=continue_sequence
        )
    sequence = generator.generate_prime_sequence(length, include_indices=indices)
    print(sequence)
