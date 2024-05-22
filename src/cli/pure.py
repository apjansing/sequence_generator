from typing import List, Optional
import click
from loguru import logger
from src.cli.utils import safe_eval
from src.sequence_generator import SequenceGenerator
from .options import length, lambda_str, indices, nums, filename, continue_sequence


@click.command(context_settings={"show_default": True})
@click.help_option("-h", "--help")
@length
@lambda_str
@indices
@nums
@filename
@continue_sequence
def pure(
    nums: List[int],
    length: int,
    indices: bool,
    filename: str,
    lambda_str: Optional[str] = None,
    continue_sequence: bool = False,
):
    """
    Generates a sequence of numbers
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
    generator.generate_sequence(length)
    if indices:
        logger.info([(i + 1, num) for i, num in enumerate(generator.get_sequence())])
    else:
        logger.info(generator.get_sequence())
