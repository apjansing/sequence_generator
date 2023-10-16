from typing import List
import click
from src.cli.utils import safe_eval
from src.sequence_generator import SequenceGenerator
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
def pure(nums: List[int], lambda_str: str, length: int, indices: bool):
    """
    Generates a sequence of numbers
    """
    generator = None
    if lambda_str:
        lambda_eval = safe_eval(lambda_str)
        generator = SequenceGenerator(list(nums), lambda_eval)
    else:
        generator = SequenceGenerator(list(nums))
    sequence = generator.generate_sequence(length)
    if indices:
        print([(i + 1, num) for i, num in enumerate(sequence)])
    else:
        print(sequence)
