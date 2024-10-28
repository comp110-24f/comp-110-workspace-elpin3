def get_first(ls: list[str]) -> str:
    return ls[0]


def remove_first(ls: list[str]) -> None:
    ls.pop(0)


def get_and_remove_first(ls: list[str]) -> None:
    get_first(ls)
    remove_first(ls)


ls = ["H", "e", "y"]
print(get_first(ls))
remove_first(ls)
print(ls)
get_and_remove_first(ls)
print(ls)
