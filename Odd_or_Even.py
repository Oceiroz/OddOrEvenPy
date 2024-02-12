low = -10000
high = 100000

def get_input (input_message, input_type):
    while(True):

        raw_input = input(f"{input_message}\n")

        try:
            user_input = input_type(raw_input)
            print(f"Thanks for giving a {input_type}")
         
            break
        except ValueError:
            print(f"Please input a {input_type}")

    return user_input

while(True):
    user_input = get_input(f"Input Whole Number between {high} and {low}", int)
    if user_input >= low and user_input <= high:
            user_odd = user_input%2
            if user_odd == 1:
                print("odd")
            else:
                print("even")      
    else:
        print("your number is not in range")