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

    # generate len(map_lines) unique random numbers in 1 - 1000
    sample_size = min(1000, max(1000, len(map_lines)*3))
    random_numbers = random.sample(range(1, sample_size, 1), len(map_lines))
    for i, line in enumerate(map_lines):
        temp_line = list(line)
        random.shuffle(temp_line)
        with open(f'map_bundle/{random_numbers[i]}.wet_map.txt', 'w') as f:
            f.write(f"{i:03}: {"".join(temp_line)}")

    # generate len(map_lines) unique random numbers in 1 - 1000
    sample_size = min(1000, max(1000, len(map_lines)*3))
    random_numbers = random.sample(range(1, sample_size, 1), len(map_lines)*2)
    for i, line in enumerate(map_lines):
        line_len = len(line)
        cut = random.randint(0, line_len)
        temp_line = line[:cut]
        temp_line2 = line[cut:]
        with open(f'map_bundle/{random_numbers[i]}.torn_map.txt', 'w') as f:
            f.write(f"{i:03}: {temp_line}")
        with open(f'map_bundle/{random_numbers[i+len(map_lines)] + 1}.torn_map.txt', 'w') as f:
            f.write(f"{i:03}: {temp_line2}")

    # generate len(map_lines) unique random numbers in 1 - 1000
    sample_size = min(1000, max(1000, len(map_lines)*3))
    random_numbers = random.sample(range(1, sample_size, 1), len(map_lines))
    for i, line in enumerate(map_lines):
        with open(f'map_bundle/{random_numbers[i]}.blank_page.txt', 'w') as f:
            f.write("")
