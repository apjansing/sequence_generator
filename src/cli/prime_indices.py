from typing import List, Optional
import click
from src.sequence_generator import SequenceGenerator
from src.cli.utils import safe_eval
from .options import (
    length,
    lambda_str,
    indices,
    nums,
)


@click.command(context_settings={"show_default": True})
@click.help_option("-h", "--help")
@length
@lambda_str
@indices
@nums
def prime_indices(
    nums: List[int], length: int, indices: bool, lambda_str: Optional[str] = None
):
    """
    Return only the prime indices from a generated sequence
    """
    generator = None
    if lambda_str:
        lambda_eval = safe_eval(lambda_str)
        generator = SequenceGenerator(list(nums), lambda_eval)
    else:
        generator = SequenceGenerator(list(nums))
    sequence = generator.generate_prime_index_sequence(length, indices)
    print(sequence)
