from typing import List, Callable, Union
import os
import dill
from loguru import logger


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
        memory_safe_mode: bool = False,
    ):
        if continue_sequence and os.path.exists(f"{filename}.pickle"):

            with open(f"{filename}.pickle", "rb") as f:
                self.__setstate__(dill.load(f))
            self.continue_sequence = continue_sequence
        else:
            self.continue_sequence = continue_sequence
            self.initial_values = initial_values
            self.generator = generator if generator else (lambda x, y: x + y)
            self.filename = filename if filename else "sequence"
            self.sequence = initial_values.copy()
            self.memory_safe_mode = memory_safe_mode
            self.initial_run = True

        self.csv_path = os.path.join('.', f"{self.filename}.csv")
        self.pickle_path = os.path.join('.', f"{self.filename}.pickle")

        if self.initial_run:
            self.__write_sequence(self.sequence)
        logger.info(self.__reduce__())

    def __reduce__(self):
        # Return a tuple with a callable object and its arguments for serialization
        sg_dict = self.__dict__.copy()
        sg_dict["sequence"] = sg_dict["sequence"][-len(self.initial_values) :]
        return (dill.dumps, (sg_dict,))

    def __setstate__(self, state):
        # Deserialize the object's state using dill
        self.__dict__ = dill.loads(state)

    def __write_sequence(self, sequence_portion: Union[List, int]) -> None:
        """
        Writes or appends a sequence to a file if a filename is provided
        :param sequence: The sequence to write
        """
        csv_exists = os.path.exists(self.csv_path)
        pickle_exists = os.path.exists(self.pickle_path)
        if self.initial_run and (csv_exists or pickle_exists):
            raise FileExistsError(
                f'''Cannot overwrite existing files on initial run. Please check for {self.filename}.csv and {self.filename}.pickle
                and either delete them or set continue_sequence to True
                '''
            )

        sequence_portion = sequence_portion if isinstance(sequence_portion, list) else [sequence_portion]

        if csv_exists and not self.continue_sequence:
            logger.warning(f"File {self.csv_path} already exists. Overwriting file")
        with open(
            self.csv_path,
            "a" if self.continue_sequence else "w",
            encoding="UTF-8",
        ) as f:
            for s in sequence_portion:
                f.write(str(s) + "\n")

        if pickle_exists and not self.continue_sequence:
            logger.warning(f"File {self.filename}.pickle already exists. Overwriting file")
        with open(f"{self.filename}.pickle", "wb") as f:
            self.initial_run = False
            f.write(dill.dumps(self))

    def get_sequence(self) -> List:
        """
        Reads a sequence from a file if a filename is provided
        :return: The sequence
        """
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

    def generate_sequence_(self, length: int = 1) -> List:
        """
        An alternate method that generates a fibonacci-like sequence of numbers,
        but does not use the write_sequence decorator
        :param length: The number of numbers to generate
        :return: A list of numbers
        """
        to_pick = len(self.initial_values)

        if self.continue_sequence:
            sequence = []
            for _ in range(length):
                logger.trace(f"Generating numbers: {self.sequence}")
                # Generate the next number in the sequence by applying the generator
                # to the last `length` of numbers where length is the length of initial values
                sequence.append(self.generator(*self.sequence))
                self.sequence = (
                    sequence[-to_pick:]
                    if len(sequence) >= to_pick
                    else self.sequence[len(sequence) - to_pick :] + sequence
                )
        else:
            sequence = self.initial_values.copy()
            for _ in range(length - to_pick):
                # Generate the next number in the sequence by applying the generator
                # to the last n numbers where n is the length of initial values
                sequence.append(self.generator(*sequence[-to_pick:]))

        return sequence

    def generate_sequence(self, length: int) -> List:
        """
        Generates a fibonacci-like sequence of numbers
        :param n: The number of numbers to generate
        :return: A list of numbers
        """
        sequence = []
        if self.memory_safe_mode:
            for _ in range(length):
                next_value = self.generate_sequence_()[0]
                self.__write_sequence(next_value)
        else:
            sequence = self.generate_sequence_(length)
            self.__write_sequence(sequence)
