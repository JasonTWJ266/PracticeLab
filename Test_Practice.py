import Practice

print("Test Practice")


def test_find_min_max():
    result = []
    max_min_list = [50, 60, 70, 80, 90, 100]
    test_max_min_list = [50, 100]
    result = Practice.find_min_max(max_min_list)
    assert (result == test_max_min_list)


def test_calc_average():
    result = []
    average_list = [1, 2, 3, 4, 5]
    test_average_list = [3]
    result = Practice.calc_average(average_list)
    assert (result == test_average_list)


def test_calc_median_temperature():
    result = []
    median_list = [1, 2, 3, 4, 5]
    test_median_list = [3]
    result = Practice.calc_median_temperature(median_list)
    assert (result == test_median_list)
