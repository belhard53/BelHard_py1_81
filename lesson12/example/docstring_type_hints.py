#-------------- type hints - тайпхинтинг
def f2(a:int | float, b: str, c: list[int|float]) -> bool:
    print(a)
    
f2("1", "H", [1,2])


def foo(a: list, *args: str | int, **kwargs: int) -> tuple[bool, bool]:
    print(a)
    print(args)
    print(kwargs)
    return True, False

numbers: list[int] = [1, 2, 3, 4]

data: dict[str, dict[str, str]] = {
    "name": {"min": "Alex"}
}



# --------------------------------------
# docstring

def f1(a:int, b:list) -> list:
    """
    Функция для .....
    """
    pass

def rotate(objs: list[Any], n: int) -> list[Any]:
    """Rotate list

    :param objs: list for rotate
    :param n: step
    :return: rotated list
    """
    for _ in range(abs(n)):
        if n > 0:
            objs.insert(0, objs.pop(-1))
        else:
            objs.append(objs.pop(0))
    return objs

def multiply(a: int, b: int) -> int:
    """Произведение 2 целых чисел

    :param a: Первый множитель
    :type a: int
    :param b: Второй множитель
    :type b: int
    :return: Результат произведения
    :rtype: int
    :raise TypeError: если один из множителей не число
    
    """
    return a * b

f1(1, 2)
rotate([1,2,3,4,5], 2)
multiply(2,3)
    

