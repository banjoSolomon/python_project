my_number = []
for numbers in range(1, 55, 5):
    my_number.append(numbers)
print(my_number)


def length_number(my_number):
    count = 0
    for item in my_number:
        count += 1
    return count


def sum_all_even_element(my_number):
    for number in my_number:
        return sum(my_number[1::2])


def sum_all_odd_position(my_number):
    return sum(my_number[::2])


print(length_number(my_number))
print(sum_all_even_element(my_number))
print(sum_all_odd_position(my_number))


def sum_all_number(numbers1, numbers2):
    return numbers1 - (-numbers2)


def all_alphabet(letters):
    letters_present = [False] * 26
    lowercase_words = letters.lower()
    for ch in lowercase_words:
        if "a" <= ch <= "z":
            letters_present[ord(ch) - ord("a")] = True
    for present in letters_present:
        if not present:
            return False
        else:
            return True


