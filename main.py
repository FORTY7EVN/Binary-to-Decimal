
def take_input():
    value = input("Enter a binary integer: ").strip()
    if not value or any(bit not in "01" for bit in value):
        raise ValueError("Enter a binary number containing only 0 and 1.")
    return [int(bit) for bit in value]


def convert(arr):
    result = 0
    power = 0
    for index in range(len(arr) - 1, -1, -1):
        result = result + ((2**power) * arr[index])
        power += 1
    return result


def invert(arr):
    return [1 - bit for bit in arr]


def add_1(arr):
    for index in range(len(arr) - 1, -1, -1):
        if arr[index] == 0:
            arr[index] = 1
            break
        arr[index] = 0
    return arr


def unsigned_int(arr):
    return convert(arr)


def signed_int(arr):
    if arr[0] == 1:
        return -convert(arr[1:])
    else:
        return convert(arr[1:])


def unsigned_1s(arr):
    return convert(invert(arr))


def signed_1s(arr):
    sign = arr[0]
    if sign == 1:
        return -convert(invert(arr[1:]))
    else:
        return convert(arr[1:])


def unsigned_2s(arr):
    return convert(add_1(invert(arr)))


def signed_2s(arr):
    if arr[0] == 1:
        return -convert(add_1(invert(arr[1:])))
    else:
        return convert(arr[1:])


def magnitude(arr):
    return convert(arr[1:])


def to_excess_7_binary(value):
    return [int(bit) for bit in format(value + 7, "b")]


def excess_7_decimal(arr):
    return convert(arr) - 7


def test():
    arr = take_input()
    conversions = {
        "unsigned integer": unsigned_int(arr),
        "signed integer": signed_int(arr),
        "unsigned 1's complement": unsigned_1s(arr),
        "signed 1's complement": signed_1s(arr),
        "unsigned 2's complement": unsigned_2s(arr),
        "signed 2's complement": signed_2s(arr),
        "magnitude": magnitude(arr),
        "excess-7 decimal": excess_7_decimal(arr),
    }

    for name, value in conversions.items():
        print(f"{name}: {value}")


test()
