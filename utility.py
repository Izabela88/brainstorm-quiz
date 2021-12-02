def input_validate(input_text, is_int=False, range_list=None):
    while True:
        user_input = input(input_text)
        if len(user_input) == 0:
            print("You must write something")
            continue
        if is_int:
            try:
                user_input = int(user_input)
            except ValueError:
                print("Please type right input,must be integer")
                continue
        if range_list and user_input not in range_list:
            str_range_list = [str(i) for i in range_list]
            print(f"Please enter a valid input, must be one of: {', '.join(str_range_list)}")
            continue
        return user_input

        

# user_input = input_validate('YOUR AGE:', is_int=True, range_list=[1,2,3])
# print(user_input)