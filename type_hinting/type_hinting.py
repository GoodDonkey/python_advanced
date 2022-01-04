def my_function(param: int) -> str:
    return f"param is {param}"


def func2(param: str):
    print(param)


my_function(10)
func2(my_function(20))

# python 3.9 부터는 list도 type hinting 가능.
# def dosth(param: list[int]):
#     pass