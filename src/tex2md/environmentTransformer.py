from pathlib import Path
from typing import Callable

ENVIRONMENTS_TRANSFORMERS: dict[str, Callable[[None | str | list[str]], str]] = {}


def find_matching_pairs(line: str) -> dict[int, int]:
    stack = []
    pairs = {}

    for index, char in enumerate(line):
        if char == '(':
            stack.append(index)
        elif char == ')':
            if stack:
                start_index = stack.pop()
                pairs[start_index] = index
            else:
                print(f"Warning: Unmatched closing parenthesis at index {index}")
    while stack:
        start_index = stack.pop()
        print(f"Warning: Unmatched opening parenthesis at index {start_index}")

    return pairs


def start_environment_line(environment_type: str, next_line: str) -> str:
    matching_pairs = find_matching_pairs(next_line)
    if not matching_pairs:
        first_line = ENVIRONMENTS_TRANSFORMERS[environment_type]()
        second_line = next_line
    label_start = min(matching_pairs.keys())
    label_end = matching_pairs[label_start]



def transform_environments(input_file_path: Path, output_file_path: Path):
    tab_amount = 0
    with open(output_file_path, "w") as output_file:
        with open(input_file_path, "r") as input_file:
            while line := input_file.readline():
                if line.startswith(":::"):
                    line_components = line.split()
                    if line_components[-1] != ":::":
                        output_file.write(start_environment_line(
                            line_components[-1],
                            input_file.readline()
                        ))
                        tab_amount += 1
                    else:
                        output_file.write("\n")
                        tab_amount -= 1
                else:
                    output_file.write(line)
