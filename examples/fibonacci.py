from sequence_generator.sequence_generator import SequenceGenerator

sequence_generator = SequenceGenerator(
    initial_values=[1, 1],
    generator=(lambda x, y: x + y),
    filename="fibonacci",
    continue_sequence=True,
)
# sequence_generator.generate_sequence(10, memory_safe_mode=False)
sequence_generator.generate_sequence(100000, memory_safe_mode=False, timeout=3)
sequence_generator.print_sequence()
