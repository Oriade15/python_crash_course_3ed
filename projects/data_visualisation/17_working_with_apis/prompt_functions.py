def prompt_user_choice(prompt, options):
    """ Prompt a user with a set of options and 
    returns an index for their choice.  """
    is_prompting_active = True
    while is_prompting_active:
        print(prompt)
        for index in range(len(options)):
            print(f"{index+1}. {options[index]}")

        choice_index = int(input("\nSelect an option (number): ")) - 1
        if choice_index in range(len(options)):
            is_prompting_active = False
            return choice_index
        else:
            print("You entered an invalid option. Please try again.\n")