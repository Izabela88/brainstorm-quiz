from sys import stdout
from time import sleep
from typing import Union
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown


console = Console()


def input_validate(
    input_text: str,
    is_int: bool = False,
    allowed_list: list = None,
    case_sensitive: bool = False,
    max_length: int = None,
    min_length: int = None,
) -> Union[str, int]:
    """Function validates user input and enforce him to retype correct answer.
    If validation fail function will indicate why this happened.

    :param input_text: Input method display text
    :type input_text: str
    :param is_int: If True user input must be an integer type, else False,
        defaults to False
    :type is_int: bool, optional
    :param allowed_list: User input must be within values in the list,
        defaults to None
    :type allowed_list: list, optional
    :param case_sensitive: Defines whether uppercase and lowercase letters are
        treated as distinct or equivalent. Set True for equivalent, else False,
        defaults to False
    :type case_sensitive: bool, optional
    :param max_length: Maximum user input length, defaults to None
    :type max_length: int, optional
    :param min_length: Minimum user input length, defaults to None
    :type min_length: int, optional
    :return: Return user input after validation
    :rtype: Union[str, int]
    """
    while True:
        user_input = input(input_text)
        if case_sensitive is False:
            user_input = user_input.lower()
        if len(user_input) < 1:
            console.print("This field can not be blank!\n", style="red")
            continue
        if max_length and len(user_input) > max_length:
            msg = f" Must be max {max_length}."
            console.print("[red]You entered too many characters!" + msg)
            continue
        if min_length and len(user_input) < min_length:
            msg = f" Must be min {min_length}."
            console.print("[red]You entered too few characters!" + msg)
            continue
        if is_int:
            try:
                user_input = int(user_input)
            except ValueError:
                console.print(
                    "Please type right input, must be integer\n", style="red"
                )
                continue

        if allowed_list and user_input not in allowed_list:
            str_allowed_list = [str(i) for i in allowed_list]
            console.print(
                "[red]Please enter a valid input, must be:"
                f" {', '.join(str_allowed_list)}\n"
            )
            continue
        return user_input


def time_counting() -> None:
    """Display time counter"""
    start_msg = Panel.fit(
        Markdown("\nLET'S BEGIN!", justify="center"), width=60, style="yellow1"
    )
    console.print(start_msg)
    for i in range(5, 0, -1):
        stdout.write("\r%d" % i)
        stdout.flush()
        sleep(1)
    stdout.write("\n\n")
