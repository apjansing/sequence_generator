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
