def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print(calc_average_temperature(num_list))
    print(calc_min_max_temperature(num_list))


def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5,67,32)")


def get_user_input():
    number_input = input()
    number_input_split = number_input.split(",")
    return [float(x) for x in number_input_split]


def calc_average_temperature(num_list):
    total = 0
    for numbers in num_list:
        total += numbers
    average = total / len(num_list)
    return f'The calculated average value of all temperature readings is {average}'


def calc_min_max_temperature(num_list):
    print(f'The maximum temperature in the list is {max(num_list)}')
    print(f'The minimum temperature in the list is {min(num_list)}')


if __name__ == "__main__":
    main()
