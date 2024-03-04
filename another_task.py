# new_number = []
# for numbers in range(10):
#     userInput = int(input("Enter ten number: "))
#     if userInput not in new_number:
#         new_number.append(userInput)
#     else:
#         print("Duplicate Number")
# print(new_number)


def sum_collection(my_numbers):
    total_sum = sum(my_numbers)
    return total_sum


def remove_item(items, element):
    if element in items:
        items.remove(element)
        return element
    else:
        return None


def find_intersection(element_one, element_two):
    view_one = set(element_one)
    view_two = set(element_two)
    new_element = view_one.union(view_two)
    return new_element
