# utils.py

import os
import textwrap
import logging
import sys
from typing import Any, List


class Utility:
    """
    General-purpose utility class.

    Responsibilities:
    - Logging (info / debug / error)
    - Screen clearing
    - Text formatting for display
    """

    def __init__(self, level: int = logging.INFO) -> None:
        """
        Initialize the Utility object.

        Parameters:
            level (int): Logging level (e.g. logging.INFO, logging.DEBUG).
        """

        # Predefined text messages you may want to reuse
        self.text: dict[str, str] = {
            "ERROR": "\nOops! Something went wrong.",
            "END": "\n[Program finished]",
            "MISSING_FILE": "\nFile path not found.",
        }

        # Create (or retrieve) a logger with a stable name
        self.logger = logging.getLogger("hashi_pkg")

        # Set the minimum log level this logger will handle
        self.logger.setLevel(level)

        # Prevent adding multiple handlers if Utility is instantiated many times
        if not self.logger.handlers:
            handler = logging.StreamHandler()

            formatter = logging.Formatter(
                "[%(levelname)s] \n%(message)s"
            )

            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    # -------- Logging methods --------

    def info(self, message: Any) -> None:
        """Log a normal informational message."""
        self.logger.info(message)

    def debug(self, message: Any) -> None:
        """Log detailed debug information."""
        self.logger.debug(message)

    def error(self, message: Any) -> None:
        """Log an error message."""
        self.logger.error(message)

    # -------- Non-logging utilities --------

    def clear_screen(self) -> None:
        """Clear the terminal screen (cross-platform)."""
        os.system("cls" if os.name == "nt" else "clear")

    def clear_line(self, n: int = 1) -> None:
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

    def format_text(self, text: str, width: int = 70) -> str:
        """
        Wrap long text to fit nicely on smaller screens.

        Parameters:
            text (str): Text to wrap.
            width (int): Max characters per line.

        Returns:
            str: Wrapped text.
        """
        wrapper = textwrap.TextWrapper(width=width)
        formatted: List[str] = []

        for line in text.split("\n"):
            if not line.strip():
                formatted.append("")
            else:
                formatted.append(wrapper.fill(line))

        return "\n".join(formatted)