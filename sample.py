from textwrap import wrap
from time import time
def sawp_number(alphabet, second):
    return second[0:2] + alphabet[2::] + ' ' + alphabet[0:2] + second[2::]


try:
    userInput = int(input("Enter numbers: "))
    sum_even = 0
    sum_odd = 0
    for count in range(userInput):
        if count % 2 == 0:
            sum_even += count
        else:
            sum_odd += count

    print(sum_even)
    print(sum_odd)
except ValueError:
    print("INVALID ERROR")


def decorate(fn):
    def inner(*args,**kwargs):
        print("**********")
        print(fn(*args, **kwargs))
        print("**********")

   # return inner

 @decorate
def show_name(name):
    return name


print(show_name("Solomom"))


def time_taken(fn):
    def wrap(*args, kwargs):

    ti = time()
    result =fn()
    t2 =time()
    return result

return wrap


@time_taken

def get_list(numbers)


