from Generation.NoiseGenerator import noise_generator
from Generation.PrintFunction import print_matrix
from Generation.TargetsGenerator import target_generator


def frame_generator_with_several_targets(height, width, x_target, y_target, gamma, amplitude, print_attribute='no_print'):
    noise = noise_generator(height, width)
    target = target_generator(height, width, x_target, y_target, gamma, amplitude)

    matrix = noise + target
    # matrix = target
    if (print_attribute == 'print'):
        print_matrix(matrix, 'frame')
    return matrix
