
def take_input(value):
    value = int(input("Enter an integer: "))


def unsigned_int():
    # output = convert_by_weights()
    # print(output)

    pass


def signed_int():
    # extract msb
    # remove msb bit from og list
    # convert remaining n-1 bits by weight
    # add sign
    pass


def unsigned_1s():
    # invert
    # convert bits by weight
    pass


def signed_1s():
    # extract msb
    # invert n bits
    # add sign
    # conversion by weights
    # add sign
    pass


def unsigned_2s():
    # invert
    # add 1
    # conversion by weight
    pass


def signed_2s():
    # extract msb
    # invert n bits
    # add 1
    # convert n bits
    # add sign
    # convert by weights
    pass


def magnitude():
    # extract msb
    # convert n-1 bits
    # add sign
    # conversion by weights
    pass


def to_excess_7_binary():
    # input: excess-7 decimal
    # add 7
    # conversion to binary
    # invert n bits
    # add 1
    pass


def excess_7_decimal():
    # input: excess-7 binary
    # conversion by weights
    # minus 7
    pass


def convert_by_weights():
    # output var
    # reverse the list
    # for every element of the list from 0 to end : ( (2 ^ n) * bit_value ),  where bit_value is the value of that bit on its given index, and n is the index of that element in the list
    # increment every output of element to output var
    pass


def invert():
    # fetch every element from the list by for loop , arguement: num in reversed(numbers): , where reversed is actually a method of accessing a list elements in reverse order, built in
    # append every element to a new list

    # starting_range = length of list - 1
    # ending_range = -1 : ending range is -1 because loop ends 1 entry before the given number ... just like <
    # decrement of -1 for every iteration of the loop
    # element is the element of list at given index
    # append element to the new list

    # while the og list:
    #   reversed_arr . append () = og_arr . pop ()

    # def reverse_with_loop(arr):
    # reversed_arr = []
    # Count down from len(arr) - 1 down to 0
    # for i in range(len(arr) - 1, -1, -1):
    #    reversed_arr.append(arr[i])
    # return reversed_arr
    pass


def add_1():
    # get reversed list
    # start from 0 (virtually end element of og list)
    # if the given element is 1, output of that will be 0,
    # and move to next element, if element is 0, output of that element is 1
    # ... skip other elements ...
    # add other elements of the og list as it is
    pass


def extract_msb():
    # og list, the element at index 0,
    # get that element,
    # if element if 1, sign = minus
    # else sign = plus
    pass
