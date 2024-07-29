from sequence_generator.sequence_generator import SequenceGenerator

sequence_generator = SequenceGenerator(
    initial_values=[2, 3, 5, 7],
    generator=(lambda w, x, y, z: w - x + y - z),
    filename="jansing",
    continue_sequence=True,
    steaming_mode=True,
)
# sequence_generator.generate_sequence(10)
sequence_generator.generate_sequence(10000)
