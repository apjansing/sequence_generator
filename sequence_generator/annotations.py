from os import path
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
                logger.warning(f"File {self.filename}.csv already exists. Overwriting file")
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
                logger.warning(f"File {self.filename}.pickle already exists. Overwriting file")
            with open(f"{self.filename}.pickle", "wb") as f:
                f.write(dill.dumps(self))
        return sequence

    return wrapper
