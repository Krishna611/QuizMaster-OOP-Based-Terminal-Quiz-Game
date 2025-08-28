# quizmaster/utils.py

import os
import random

def clear_screen():
    """Clear terminal screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")

def pause(msg: str = "Press Enter to continue..."):
    try:
        input(msg)
    except EOFError:
        pass

def safe_int_input(prompt: str, valid_range: range | None = None) -> int:
    """
    Read integer input repeatedly until valid.
    If valid_range provided, ensures returned int in that range.
    """
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if valid_range is not None and val not in valid_range:
                min_r, max_r = min(valid_range), max(valid_range)
                print(f"Please enter a number in {min_r}-{max_r}.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a number.")

def shuffled(iterable):
    items = list(iterable)
    random.shuffle(items)
    return items
