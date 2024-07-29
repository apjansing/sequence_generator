from sequence_generator.sequence_generator import SequenceGenerator

sequence_generator = SequenceGenerator(
    initial_values=[1, 1],
    generator=(lambda x, y: x + y),
    filename="fibonacci",
    continue_sequence=True,
    steaming_mode=False,
)
# sequence_generator.generate_sequence(10)
sequence_generator.generate_sequence(10000)
