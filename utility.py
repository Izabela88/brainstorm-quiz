def input_validate(
    input_text: str,
    is_int: bool = False,
    range_list: list = None,
    case_sensitive: bool = False,
):
    while True:
        user_input = input(input_text)
        if case_sensitive is False:
            user_input = user_input.lower()
        if len(user_input) == 0:
            print("\nThis field can not be blank!\n")
            continue
        if is_int:
            try:
                user_input = int(user_input)
            except ValueError:
                print("\nPlease type right input, must be integer\n")
                continue
        if range_list and user_input not in range_list:
            str_range_list = [str(i) for i in range_list]
            print(
                "\nPlease enter a valid input, must be:"
                f" {', '.join(str_range_list)}\n"
            )
            continue
        return user_input
