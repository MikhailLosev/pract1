def permutList(l: list) -> list:
    if not l:
        return [[]]
    res = []
    for e in l:
        temp = l[:]
        temp.remove(e)
        res.extend([[e] + r for r in permutList(temp)])
    return res


def main():
    data = str(input())# 1 1 2
    data = data.strip()
    data = data.split()
    data = [int(x) for x in data]
    new = []
    for i in permutList(data):
        if i not in new:
            new.append(i)
    print(new)


if __name__ == "__main__":
    main()
