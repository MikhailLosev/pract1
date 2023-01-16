import itertools


def func(list_: list) -> set:
    list2 = []
    res = itertools.permutations(list_)
    for i in res:
        list2.append(i)
    return set(list2)


def main():
    list_ = str(input())
    list_ = list_.strip()
    list_ = list_.split()
    list_ = [int(x) for x in list_]

    print(func(list_))


if __name__ == "__main__":
    main()
