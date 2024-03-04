def list_sort(number):
    num = len(number)
    for i in range(num):
        for k in range(0, num - i - 1):
            if number[k] > number[k + 1]:
                number[k], number[k + 1] = number[k + 1], number[k]


def print_ascending_order(sample_list):
    list_sort(sample_list)
    for num in sample_list:
        print(num, end=' ')


sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
print_ascending_order(sample_list)
