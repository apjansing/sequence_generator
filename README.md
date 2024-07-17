# Sequence Generator

This project is a tool to generate Fibonacci-like sequences.

## Getting Stared

### Prerequisites

This project uses `poetry` to manage dependencies. To install it, follow the instructions [here](https://python-poetry.org/docs/#installation).

Once poetry is installed, you can set up the project with the following command:

```bash
poetry install
```

### Examples in Python

```python
from sequence_generator import SequenceGenerator


def fibonacci_sequence(n):
    generator = SequenceGenerator([1, 1])
    return generator.generate_sequence(n)


if __name__ == "__main__":
    sequence = fibonacci_sequence(10)
    print(sequence) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
```

```python
from sequence_generator import SequenceGenerator


def custom_sequence(n, generator: SequenceGenerator = SequenceGenerator()):
    return generator.generate_sequence(n)


if __name__ == "__main__":
    generator = SequenceGenerator(
        [2, 3, 5],
        generator=lambda x, y, z: x + y + z if (x + y + z) % 2 == 1 else x + y + z - 1,
    )
    sequence = custom_sequence(10, generator=generator)
    print(sequence) # [2, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201, 2209, 4063, 7473, 13745, 25281, 46499, 85525, 157305]
```

### Testing

To run the tests, you can use the following command:

```bash
poetry run pytest
```
