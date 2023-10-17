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

### Running with the CLI

To run the project, you can use the following commands:

```bash
# Generate the Fibonacci sequence
poetry run generate_sequence pure
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

```bash
# Continue the sequence
poetry run generate_sequence pure -n 34 -n 55
[34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]
```

```bash
# Generate the Lucas sequence with a length is 20 and showing the indices
poetry run generate_sequence pure -n 2 -n 1 -i -l 20
[(1, 2), (2, 1), (3, 3), (4, 4), (5, 7), (6, 11), (7, 18), (8, 29), (9, 47), (10, 76), (11, 123), (12, 199), (13, 322), (14, 521), (15, 843), (16, 1364), (17, 2207), (18, 3571), (19, 5778), (20, 9349)]

```

```bash
# Generate a custom sequence with a length is 20 and showing the indices
poetry run generate_sequence pure -n 1 -n 2 -L "lambda x, y: x + y - 3 if (x + y) % 2 == 0 else x + y" -i -l 20
[(1, 1), (2, 2), (3, 3), (4, 5), (5, 5), (6, 7), (7, 9), (8, 13), (9, 19), (10, 29), (11, 45), (12, 71), (13, 113), (14, 181), (15, 291), (16, 469), (17, 757), (18, 1223), (19, 1977), (20, 3197)]
```

```bash
# Generate a list of primes from the Fibonacci sequence
poetry run generate_sequence primes          
[2, 3, 5, 13]
```

```bash
# Generate a list of primes from the Lucas sequence with a length of 20 and showing the indices
poetry run generate_sequence primes -n 2 -n 1 -i -l 20
[(1, 2), (3, 3), (5, 7), (6, 11), (8, 29), (9, 47), (12, 199), (14, 521), (17, 2207), (18, 3571), (20, 9349)]
```

```bash
# Generate a list of primes from a custom sequence with a length is 20 and showing the index
poetry run generate_sequence primes -n 1 -n 2 -L "lambda x, y: x + y - 3 if (x + y) % 2 == 0 else x + y" -i -l 20
[(2, 2), (3, 3), (4, 5), (5, 5), (6, 7), (8, 13), (9, 19), (10, 29), (12, 71), (13, 113), (14, 181), (17, 757), (18, 1223)]
```

```bash
# Generate a Fibonacci sequence where the indices are prime numbers
poetry run generate_sequence prime-indices
[1, 2, 5, 13]
```

```bash
# Generate a Fibonacci sequence where the indices are prime numbers and length is 20
poetry run generate_sequence prime-indices -i -l 20
[(2, 1), (3, 2), (5, 5), (7, 13), (11, 89), (13, 233), (17, 1597), (19, 4181)]
```

```bash
# Generate a custom sequence where the indices are prime numbers and length is 20 and showing the indices
poetry run generate_sequence prime-indices -n 7 -n 11 -i -l 20 -L "lambda x, y: x + y - 3 if (x + y) % 2 == 0 else x + y"
[(2, 11), (3, 15), (5, 35), (7, 87), (11, 579), (13, 1511), (17, 10339), (19, 27063)]
```

### Testing

To run the tests, you can use the following command:

```bash
poetry run pytest
```
