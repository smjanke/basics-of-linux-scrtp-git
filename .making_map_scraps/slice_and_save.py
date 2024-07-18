#!/TODO:Path to local python
import random


if __name__ == "__main__":
    with open('ascii_map.txt', 'r') as f:
        ascii_map = f.read()
    map_lines = ascii_map.split('\n')

    # generate len(map_lines) unique random numbers in 1 - 1000
    sample_size = min(1000, max(1000, len(map_lines)*3))
    random_numbers = random.sample(range(1, sample_size, 1), len(map_lines))

    for i, line in enumerate(map_lines):
        with open(f'map_bundle/{random_numbers[i]}.map.txt', 'w') as f:
            f.write(f"{i:03}: {line}")
