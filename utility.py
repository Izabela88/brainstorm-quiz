from rich import print
from rich.console import Console


console = Console()


def input_validate(
    input_text: str,
    is_int: bool = False,
    range_list: list = None,
    case_sensitive: bool = False,
    max_length: int = None,
    min_length: int = None,
):
    while True:
        user_input = input(input_text)
        if case_sensitive is False:
            user_input = user_input.lower()
        if len(user_input) < 1:
            console.print("This field can not be blank!\n", style="red")
            continue
        if max_length and len(user_input) > max_length:
            txt = f" Must be max {max_length}."
            console.print(f"[red]You entered too many characters!" + txt)
            continue
        if min_length and len(user_input) < min_length:
            txt2 = f" Must be min {min_length}."
            console.print(f"[red]You entered too few characters!" + txt2)
            continue
        if is_int:
            try:
                user_input = int(user_input)
            except ValueError:
                console.print(
                    "Please type right input, must be integer\n", style="red"
                    )
                continue

        if range_list and user_input not in range_list:
            str_range_list = [str(i) for i in range_list]
            console.print(
                "[red]Please enter a valid input, must be:"
                f" {', '.join(str_range_list)}\n"
            )
            continue
        return user_input
