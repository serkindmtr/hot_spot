from Generation.NoiseGenerator import noise_generator
from Generation.PrintFunction import print_matrix
from Generation.TargetsGenerator import target_generator


def frame_generator():
    noise = noise_generator()
    target = target_generator()

    matrix = noise + target
    return matrix


frame = frame_generator()
print_matrix(frame, 'frame')