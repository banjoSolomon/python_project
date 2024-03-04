# x = 7
# x *= 5
# print(x)
# x = 12
# x **= 2
# print(x)
# x = 7 * 5
# rint(f'7 times 5 is {x}')

# total = 0
# grade_counter = 0
# grade = int(input("Enter grade, -1 to end: "))
# while grade != -1:
#   total += grade
#  grade_counter += 1
# grade = int(input("Enter grade, -1 to end: "))
# if grade_counter != 0:
#   average = total / grade_counter
#  print(f'Class average is {average:.2f}')
# else:
#   print('no grade were entered')


# student_tuple = 'john', 'Green', 3.3
# print(student_tuple)
# len(student_tuple)
# print(student_tuple)

# tuple1 = (10, 20, 30)
# tuple2 = tuple1
# print(tuple2)
# tuple1 += (40, 50)
# print(tuple1)
# numbers = [1, 2, 3, 4, 5]
# numbers += (6, 7)
# print(numbers)

# sample_list = []
# s = 'abc'
# sample_list.extend(s)
# print(sample_list)
# t = (1, 2, 3)
# sample_list.extend(t)
# print(sample_list)

# numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
# list(filter(lambda x: x % 2 != 0, numbers))
# print(numbers)
def number_of_letter_number_of_lower(check):
    number_of_digit = 0
    number_of_letters = 0
    for index in check:
        if index.isdigit():
            number_of_digit += 1
        if index.isalpha():
            number_of_letters += 1
    return f"number_of_digit {number_of_digit} number_of_letters {number_of_letters}"



second_sentence = "Hello 122"
new_sentence = "HELLO_hi"


def number_upper_lower(check_input):
    check_lower = 0
    check_upper = 0
    for index in check_input:
        if index.islower():
            check_lower += 1
        if index.isupper():
            check_upper += 1
    return f"check_lower {check_lower} check_upper {check_upper}"


print(number_upper_lower(new_sentence))
print(number_of_letter_number_of_lower(second_sentence))
