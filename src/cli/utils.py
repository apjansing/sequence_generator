# These imports are required for the safe_eval function
# pylint: disable-next=unused-import
from math import (
    ceil,
    floor,
    exp,
    log,
    log10,
    sqrt,
    sin,
    cos,
    tan,
    asin,
    acos,
    atan,
    atan2,
    pi,
)
import ast


def safe_eval(lambda_str):
    """
    Safely evaluate a lambda string by checking if the names used in the lambda string are allowed
    """
    allowed_names = {
        *[chr for chr in "abcdefghijklmnopqrstuvwxyz"],  # allowed variable names
        "abs",
        "max",
        "min",
        "sum",
        "ceil",
        "floor",
        "round",
        "trunc",
        "exp",
        "log",
        "log10",
        "sqrt",
        "sin",
        "cos",
        "tan",
        "asin",
        "acos",
        "atan",
        "atan2",
        "pi",
    }  # Add more as needed

    # Parse the lambda string
    parsed = ast.parse(lambda_str, mode="eval")

    # Walk through the AST and check if any names are not allowed
    for node in ast.walk(parsed):
        if isinstance(node, ast.Name) and node.id not in allowed_names:
            raise ValueError(f"Invalid name used in lambda expression: {node.id}")

    # If all names are allowed, then evaluate the expression
    # pylint: disable-next=eval-used
    lambda_func = eval(compile(parsed, filename="<string>", mode="eval"))
    return lambda_func
