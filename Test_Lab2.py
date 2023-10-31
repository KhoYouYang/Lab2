import Lab2


def test_find_min_max():
    result = []
    input_test = [5.0, 67.0, 32.0]
    test_result = ['Minimum value = 5.0', 'Maximum value = 67.0']
    result = Lab2.find_min_max(input_test)
    assert (result == test_result)

def test_calc_average():
    result = []
    input_test = [5.0, 67.0, 32.0]
    test_result = 34.666666666666664
    result = Lab2.calc_average(input_test)
    assert (result == test_result)

def test_calc_median_temp():
    result = []
    input_test = [5.0, 67.0, 32.0]
    test_result = 32.0
    result = Lab2.calc_median_temperature(input_test)
    assert (result == test_result)