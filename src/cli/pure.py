from typing import List
import click
from src.cli.utils import safe_eval
from src.sequence_generator import SequenceGenerator


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
