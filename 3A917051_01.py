def get_even_squares(num_list) -> list:
    """返回list中偶數的平方值列表"""
    return [x**2 for x in num_list if x % 2 == 0]


def get_odd_cubes(num_list) -> list:
    """返回list中奇數的3次方值列表"""
    x = []
    for i in num_list:
        if i % 2 != 0:
            x.append(i**3)
    return x


def get_sliced_list(num_list) -> list:
    """利用切片返回list第五個元素到最後一個元素的列表"""
    return num_list[4:]


def format_numbers(numbers) -> list:
    """建立新列表，並格式化8字元寬度，靠右對齊"""
    return [f"{num:>8}" for num in numbers]


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = get_even_squares(num_list)
b = get_odd_cubes(num_list)
c = get_sliced_list(num_list)

f_a = format_numbers(a)
f_b = format_numbers(b)
f_c = format_numbers(c)

print(", ".join(f_a))
print(", ".join(f_a))
print(", ".join(f_c))
