from typing import Generator, List, Callable, Optional, Union
import os
import dill
import time
from loguru import logger


class SequenceGenerator:
    """
    This class to generate sequences of values based on a generator function
    """

    def __init__(
        self,
        initial_values: List = [1, 1],
        generator: Callable = (lambda x, y: x + y),
        filename="sequence",
        continue_sequence: bool = False,
        memory_safe_mode: bool = False,
    ):
        '''
        :param initial_values: The first n values in the sequence
        :param generator: A function that performs an operation on the last n values in the sequence
        :param filename: Base filename for the sequence files. This will be used to create a .csv and .pickle file
        :param continue_sequence: If True, the sequence will be continued from the values in the .csv file
        :param memory_safe_mode: If True, the sequence will be written to the .csv file after each iteration
        '''
        if continue_sequence and os.path.exists(f"{filename}.pickle"):

            with open(f"{filename}.pickle", "rb") as f:
                self.__setstate__(dill.load(f))
            self.continue_sequence = continue_sequence
        else:
            self.continue_sequence = continue_sequence
            self.initial_values = initial_values
            self.generator = generator if generator else (lambda x, y: x + y)
            self.sequence = initial_values.copy()
            self.memory_safe_mode = memory_safe_mode
            self.initial_run = True
            filename = filename if filename else "sequence"
            self.csv_path = os.path.join('.', f"{filename}.csv")
            self.pickle_path = os.path.join('.', f"{filename}.pickle")

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
                f'''Cannot overwrite existing files on initial run. Please check for {self.csv_path} and {self.pickle_path}
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
            logger.warning(f"File {self.pickle_path} already exists. Overwriting file")
        with open(self.pickle_path, "wb") as f:
            self.initial_run = False
            f.write(dill.dumps(self))

    def get_sequence(self) -> List:
        """
        Reads a sequence from a file if a filename is provided
        :return: The sequence
        """
        return self.sequence

    def get_sequence_from_file(self, filename: Optional[str] = None) -> List:
        '''
        Reads a sequence from a file
        :param filename: The name of the file to read
        :return: The sequence
        '''
        filename = filename if filename else self.csv_path
        with open(filename, "r", encoding="UTF-8") as f:
            return f.read().splitlines()

    def yield_sequence_from_file(self, filename: Optional[str] = None) -> Generator:
        '''
        Reads a sequence from a file - useful for large sequences
        :param filename: The name of the file to read
        :return: A generator that yields each line in the file
        '''
        filename = filename if filename else self.csv_path
        with open(filename, "r", encoding="UTF-8") as f:
            for line in f:
                yield line.strip()

    def print_sequence(self) -> None:
        """
        Prints a sequence from the `self.csv_path` file if it exists
        otherwise prints the `self.sequence` attribute
        """
        if os.path.exists(self.csv_path):
            sequence = self.yield_sequence_from_file(self.csv_path)
            for next_value in sequence:
                logger.info(next_value)
        else:
            sequence = self.sequence

    def generate_sequence_(self, length: int = 1, timeout: Optional[int] = None) -> List:
        """
        An alternate method that generates a sequence of values,
        but does not use the write_sequence decorator
        :param length: The number of values to generate
        :param timeout: The number of seconds to wait before timing out
        :return: A list of values
        """
        to_pick = len(self.initial_values)
        start_time = time.time()
        if self.continue_sequence:
            sequence = []
            for _ in range(length):
                if timeout and time.time() - start_time > timeout:
                    break
                logger.trace(f"Generating values: {self.sequence}")
                # Generate the next value in the sequence by applying the generator
                # to the last `length` of values where length is the length of initial values
                sequence.append(self.generator(*self.sequence))
                self.sequence = (
                    sequence[-to_pick:]
                    if len(sequence) >= to_pick
                    else self.sequence[len(sequence) - to_pick :] + sequence
                )
        else:
            sequence = self.initial_values.copy()
            for _ in range(length - to_pick):
                if timeout and time.time() - start_time > timeout:
                    break
                # Generate the next number in the sequence by applying the generator
                # to the last n values where n is the length of initial values
                sequence.append(self.generator(*sequence[-to_pick:]))

        return sequence

    def generate_sequence(
        self,
        length: Optional[int] = None,
        memory_safe_mode: bool = False,
        timeout: Optional[int] = None,
    ) -> List:
        """
        Generates a sequence of values
        :param length: The number of values to generate
        :param timeout: The number of seconds to wait before timing out
        :param memory_safe_mode: If True, the sequence will be written to the .csv file after each iteration
        :return: A list of values
        """

        def iterate_sequence(length: int = 1, timeout: Optional[int] = None):
            sequence = self.generate_sequence_(length=length, timeout=timeout)
            self.__write_sequence(sequence)

        if length:
            if memory_safe_mode:
                for _ in range(length):
                    iterate_sequence(timeout=timeout)
            else:
                iterate_sequence(length=length, timeout=timeout)
        else:
            iterate_sequence(timeout=timeout)
