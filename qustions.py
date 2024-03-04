my_list = []
for numbers in range(1,55,5):
    my_list.append(numbers)
print(my_list)

def my_length(my_list):
    count = 0
    for item in my_list:
        count += 1
        return count
print(my_length(my_list))
