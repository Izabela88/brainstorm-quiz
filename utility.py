def input_validate(input_text, is_int=False, range_list=None):
    while True:
        user_input = input(input_text).lower()
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
                f"\nPlease enter a valid input, must be: {', '.join(str_range_list)}\n"
            )
            continue
        return user_input
