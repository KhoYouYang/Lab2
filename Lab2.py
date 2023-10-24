import statistics

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    numlist = get_user_input()
    print(numlist)
    calc_average(numlist)
    find_min_max(numlist)
    sort_temperature(numlist)
    calc_median_temperature(numlist)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def calc_average(numlist):
    total = 0.0
    for x in numlist:
        total += x
    average = total/len(numlist)
    print(average)
    return average

def get_user_input():
    templist = input()
    splitlist = templist.split(", ")
    floatlist = [float(x) for x in splitlist]
    return floatlist
def find_min_max(numlist):
    print(min(numlist))
    print(max(numlist))
def sort_temperature(numlist):
    numlist.sort()
    print(numlist)
def calc_median_temperature(numlist):
    median = statistics.median(numlist)
    print(median)

if __name__ == "__main__":
    main()
