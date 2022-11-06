import itertools
def main():
    list = [1,1,2]
    list2 = []
    res = itertools.permutations(list)
    for i in res:
        list2.append(i)
    print(set(list2))
if __name__ == "__main__":
    main()