from typing import List, Callable
from os import path
from sympy import isprime
import dill
from loguru import logger


def write_sequence(func):
    """
    Writes or appends a sequence to a file if a filename is provided
    :param sequence: The sequence to write
    """

    def wrapper(self, *args, **kwargs):
        sequence = func(self, *args, **kwargs)
        self.sequence = sequence
        if self.filename:
            if path.exists(f"{self.filename}.csv") and not self.continue_sequence:
                logger.warning(
                    f"File {self.filename}.csv already exists. Overwriting file"
                )
            logger.info(f"Sequence: {sequence}")
            with open(
                f"{self.filename}.csv",
                "a" if self.continue_sequence else "w",
                encoding="UTF-8",
            ) as f:
                if not self.continue_sequence:
                    # Write the type of the last element in the sequence-- this could be figured out better
                    f.write(str(type(sequence[-1])) + "\n")
                for s in sequence:
                    f.write(str(s) + "\n")

            if path.exists(f"{self.filename}.pickle") and not self.continue_sequence:
                logger.warning(
                    f"File {self.filename}.pickle already exists. Overwriting file"
                )
            with open(f"{self.filename}.pickle", "wb") as f:
                f.write(dill.dumps(self))
        return sequence

    return wrapper


class SequenceGenerator:
    """
    This class generates a fibonacci-like sequence
    :param initial_values: The first n numbers in the sequence
    :param generator: A function that performs an operation on the last n numbers in the sequence
    """

    def __init__(
        self,
        initial_values: List = [1, 1],
        generator: Callable = (lambda x, y: x + y),
        filename="sequence",
        continue_sequence: bool = False,
    ):
        if continue_sequence:
            with open(f"{filename}.pickle", "rb") as f:
                self.__setstate__(dill.load(f))
            self.continue_sequence = continue_sequence
        else:
            self.continue_sequence = continue_sequence
            self.initial_values = initial_values
            self.generator = generator if generator else (lambda x, y: x + y)
            self.filename = filename
            self.sequence = initial_values.copy()
            self.value_type = type(self.initial_values[0])
        logger.info(self.__reduce__())

    def __reduce__(self):
        # Return a tuple with a callable object and its arguments for serialization
        sg_dict = self.__dict__.copy()
        sg_dict["sequence"] = sg_dict["sequence"][-len(self.initial_values) :]
        return (dill.dumps, (sg_dict,))

    def __setstate__(self, state):
        # Deserialize the object's state using dill
        self.__dict__ = dill.loads(state)

    def get_sequence(self, tail: int = -1) -> List:
        """
        Reads a sequence from a file if a filename is provided
        :return: The sequence
        """
        if self.filename and path.exists(f"{self.filename}.csv"):
            with open(f"{self.filename}.csv", "r", encoding="UTF-8") as f:
                # Extract the type name
                type_line = f.readline().strip()
                type_name = type_line.split("'")[1]
                data_type = eval(type_name)

                if tail > 0:
                    seq = f.readlines()[-tail:]
                else:
                    seq = f.readlines()
                return [data_type(s) for s in seq]
        else:
            return self.sequence

    def print_sequence(self) -> None:
        """
        Prints a sequence to the console from a file if a filename is provided,
        otherwise
        """
        sequence = self.get_sequence()
        if sequence:
            logger.info(sequence)
        else:
            logger.warning("No sequence has been generated yet")
            logger.info(sequence)

    def generate_sequence_(self, length: int) -> List:
        """
        An alternate method that generates a fibonacci-like sequence of numbers,
        but does not use the write_sequence decorator
        :param length: The number of numbers to generate
        :return: A list of numbers
        """
        to_pick = len(self.initial_values)

        if self.continue_sequence:
            sequence = []
            generating_numbers = self.get_sequence(tail=to_pick)
            for _ in range(length):
                logger.info(f"Generating numbers: {generating_numbers}")
                # Generate the next number in the sequence by applying the generator
                # to the last `length` of numbers where length is the length of initial values
                sequence.append(self.generator(*generating_numbers))
                generating_numbers = (
                    sequence[-to_pick:]
                    if len(sequence) >= to_pick
                    else generating_numbers[len(sequence) - to_pick :] + sequence
                )
        else:
            sequence = self.initial_values.copy()
            for _ in range(length - to_pick):
                # Generate the next number in the sequence by applying the generator
                # to the last n numbers where n is the length of initial values
                sequence.append(self.generator(*sequence[-to_pick:]))

        return sequence

    @write_sequence
    def generate_sequence(self, length: int) -> List:
        """
        Generates a fibonacci-like sequence of numbers
        :param n: The number of numbers to generate
        :return: A list of numbers
        """
        return self.generate_sequence_(length)
