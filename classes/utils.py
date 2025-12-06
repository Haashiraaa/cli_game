# utils.py

import sys

def clear_line(n: int = 1):
    """
    Clear the previous N lines in the terminal.

    Parameters:
        n (int): Number of lines to erase. Useful for animations.

    Uses basic ANSI escape codes:
        - \033[1A → move cursor up by one line
        - \033[2K → clear the entire current line
    """
    for _ in range(n):
        sys.stdout.write("\033[1A")     # Move cursor up
        sys.stdout.write("\r\033[2K")   # Clear line
    sys.stdout.flush()
