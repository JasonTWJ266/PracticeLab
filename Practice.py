import statistics


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(calc_average(num_list))
    print(find_min_max(num_list))
    print(sort_temperature(num_list))
    print(calc_median_temperature(num_list))


def display_main_menu():
    print("display_main_menu")


def get_user_input():
    user_input = input()
    user_input_split = user_input.split(",")
    return [float(x) for x in user_input_split]


def calc_average(num_list):
    total = 0
    for numbers in num_list:
        total += numbers
    average = total / len(num_list)
    return [average]


def find_min_max(num_list):
    maximum = max(num_list)
    minimum = min(num_list)
    return [minimum, maximum]


def sort_temperature(num_list):
    sorted_num_list = sorted(num_list)
    return f'Sorted Temperature is {sorted_num_list}'


def calc_median_temperature(num_list):
    num_list_median = statistics.median(num_list)
    return [num_list_median]


if __name__ == "__main__":
    main()
