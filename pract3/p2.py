import itertools
def main():
    list = [0]
    list2 = []
    res = itertools.permutations(list)
    for i in res:
        list2.append(i)
    print(list2)

if __name__ == "__main__":
    main()
