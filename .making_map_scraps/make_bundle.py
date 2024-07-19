#!/TODO:Path to local python
from itertools import cycle
import random
import lorem


if __name__ == "__main__":
    with open('ascii_map.txt', 'r') as f:
        ascii_map = f.read()
    map_lines = ascii_map.split('\n')

    # generate len(map_lines) unique random numbers in 1 - 1000
    sample_size = min(1000, max(1000, len(map_lines)*3))
    random_numbers = random.sample(range(1, sample_size, 1), len(map_lines))
    # turn random_numbers into an iterator so we can use next()
    random_numbers = cycle(random_numbers)

    # randomize the order of the map lines
    map_lines_shuffled = random.sample([i for i in range(len(map_lines))], len(map_lines))

    file_number = next(random_numbers)
    for i in map_lines_shuffled:
        with open(f'map_bundle/{file_number:03}.map.txt', 'a') as f:
            f.write(f"{i:03}: {map_lines[i]}")
            # randomly choose to use the same number or progress
            if random.randint(0, 1) > 0.5:
                file_number = next(random_numbers)
                print(f"Using the next number: {file_number}")
            else:
                print(f"Using the same number: {file_number}")
                f.write('\n')
                # Write up to 10 lines of random lorem ipsum
                for j in range(random.randint(0, 10)):
                    # write one line of random lorem ipsum
                    lorem_line = lorem.get_sentence()
                    f.write(f"{random.randint(0, len(map_lines)):003} {lorem_line}\n")



    # generate len(map_lines) unique random numbers in 1 - 1000
    sample_size = min(1000, max(1000, len(map_lines)*3))
    random_numbers = random.sample(range(1, sample_size, 1), len(map_lines))
    for i, line in enumerate(map_lines):
        temp_line = list(line)
        random.shuffle(temp_line)
        with open(f'map_bundle/{random_numbers[i]:03}.wet_map.txt', 'w') as f:
            f.write(f"{i:03}: {"".join(temp_line)}")

    # generate len(map_lines) unique random numbers in 1 - 1000
    sample_size = min(1000, max(1000, len(map_lines)*3))
    random_numbers = random.sample(range(1, sample_size, 1), len(map_lines)*2)
    for i, line in enumerate(map_lines):
        line_len = len(line)
        cut = random.randint(0, line_len)
        temp_line = line[:cut]
        temp_line2 = line[cut:]
        with open(f'map_bundle/{random_numbers[i]:03}.torn_map.txt', 'w') as f:
            f.write(f"{i:03}: {temp_line}")
        with open(f'map_bundle/{random_numbers[i+len(map_lines)] + 1}.torn_map.txt', 'w') as f:
            f.write(f"{i:03}: {temp_line2}")

    # generate len(map_lines) unique random numbers in 1 - 1000
    sample_size = min(1000, max(1000, len(map_lines)*3))
    random_numbers = random.sample(range(1, sample_size, 1), len(map_lines))
    for i, line in enumerate(map_lines):
        with open(f'map_bundle/{random_numbers[i]:03}.blank_page.txt', 'w') as f:
            f.write("")
