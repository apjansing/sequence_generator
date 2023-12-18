import click

length = click.option(
    "-l",
    "--length",
    default=10,
    type=int,
    help="Length of sequence",
)
lambda_str = click.option(
    "-L",
    "--lambda_str",
    type=str,
    help="String representation of a lambda function",
)
indices = click.option(
    "-i",
    "--indices",
    is_flag=True,
    default=False,
    help="Include indices in sequence.",
)
nums = click.option(
    "-n",
    "--nums",
    default=[1, 1],
    multiple=True,
    type=int,
    help="Sequence initiators",
)
filename = click.option(
    "-f",
    "--filename",
    default=None,
    type=str,
    help="Base filename for output files",
)
continue_sequence = click.option(
    "-c",
    "--continue-sequence",
    is_flag=True,
    default=False,
    help="(TODO)Flag to continue a sequence from a file. Also lets the SequenceGenerator know to append to the file instead of overwriting it.",
)
