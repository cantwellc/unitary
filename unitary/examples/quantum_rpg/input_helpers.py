"""Functions for safe and user-friendly input."""
from typing import Callable, Optional, Sequence, TextIO

import sys
import unitary.examples.quantum_rpg.qaracter as qaracter

_USER_INPUT = Callable[[str], str]
_INVALID_MESSAGE = "Invalid number selected."


def get_user_input_function(user_input: Optional[Sequence[str]] = None) -> _USER_INPUT:
    """Returns a lambda for getting user input.

    If user input is provided as a list (ie. for tests or scripts),
    then consume that list.
    If not, use stdin.
    """
    if user_input is not None:
        iter_input = iter(user_input)
        return lambda _: next(iter_input)
    else:
        return input


def get_user_input_number(
    get_user_input: _USER_INPUT,
    message: str = "",
    max_number: Optional[int] = None,
    invalid_message: Optional[str] = _INVALID_MESSAGE,
    file: TextIO = sys.stdout,
):
    """Helper to get a valid number from the user.

    This will only accept valid numbers from the user from 1 to max_number.
    If max_number is not supplied, any number will be accepted.

    User will be prompted until a valid number is returned.
    """
    while True:
        try:
            user_input = int(get_user_input(message or ""))
        except ValueError as e:
            if invalid_message:
                print(invalid_message, file=file)
            else:
                print(e, file=file)
            continue
        if max_number is None or (user_input > 0 and user_input <= max_number):
            return user_input
        if invalid_message:
            print(invalid_message, file=file)
        else:
            print("number out of range", file=file)


def get_user_input_qaracter_name(
    get_user_input: _USER_INPUT,
    qaracter_type: Optional[str] = "a new qaracter",
    file: TextIO = sys.stdout,
):
    while True:
        user_input = get_user_input(f"Please enter a name for {qaracter_type}:")
        if qaracter.Qaracter.is_valid_name(user_input):
            return user_input
        print("Invalid qaracter name", file=file)
