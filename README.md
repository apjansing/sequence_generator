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
poetry run generate_sequence pure -n 7 -n 11 -i -l 20
[(1, 7), (2, 11), (3, 18), (4, 29), (5, 47), (6, 76), (7, 123), (8, 199), (9, 322), (10, 521), (11, 843), (12, 1364), (13, 2207), (14, 3571), (15, 5778), (16, 9349), (17, 15127), (18, 24476), (19, 39603), (20, 64079)]
```

```bash
poetry run generate_sequence pure -n 1 -n 2 -L "lambda x, y: x + y - 3 if (x + y) % 2 == 0 else x + y" -i -l 20
[(1, 1), (2, 2), (3, 3), (4, 5), (5, 5), (6, 7), (7, 9), (8, 13), (9, 19), (10, 29), (11, 45), (12, 71), (13, 113), (14, 181), (15, 291), (16, 469), (17, 757), (18, 1223), (19, 1977), (20, 3197)]
```

```bash
poetry run generate_sequence primes          
[2, 3, 5, 13]
```

```bash
poetry run generate_sequence primes -n 7 -n 11 -i -l 20
[(1, 7), (2, 11), (4, 29), (5, 47), (8, 199), (10, 521), (13, 2207), (14, 3571), (16, 9349)]
```

```bash
poetry run generate_sequence primes -n 1 -n 2 -L "lambda x, y: x + y - 3 if (x + y) % 2 == 0 else x + y" -i -l 20
[(2, 2), (3, 3), (4, 5), (5, 5), (6, 7), (8, 13), (9, 19), (10, 29), (12, 71), (13, 113), (14, 181), (17, 757), (18, 1223)]
```

### Testing

To run the tests, you can use the following command:

```bash
poetry run pytest
```
