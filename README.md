# Sequence Generator

This project is a tool to generate Fibonacci-like sequences.

## Getting Stared

### Prerequisites

This project uses `poetry` to manage dependencies. To install it, follow the instructions [here](https://python-poetry.org/docs/#installation).

Once poetry is installed, you can set up the project with the following command:

```bash
poetry install
```

### Running

To run the project, you can use the following commands:

```bash
poetry run generate_sequence pure
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

```bash
poetry run generate_sequence pure --nums 7 11 -i -l 20
[(1, 7), (2, 11), (3, 18), (4, 29), (5, 47), (6, 76), (7, 123), (8, 199), (9, 322), (10, 521), (11, 843), (12, 1364), (13, 2207), (14, 3571), (15, 5778), (16, 9349), (17, 15127), (18, 24476), (19, 39603), (20, 64079)]
```

```bash
poetry run generate_sequence primes
[1, 2, 5, 13]
```

```bash
poetry run generate_sequence primes -n 7 11 -i -l 20
[(2, 11), (3, 18), (5, 47), (7, 123), (11, 843), (13, 2207), (17, 15127), (19, 39603)]
```

### Testing

To run the tests, you can use the following command:

```bash
poetry run pytest
```
